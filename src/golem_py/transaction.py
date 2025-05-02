"""
Tools to perform transactional operations using compensating actions.

Requires the following imports in the wit to work:
* import golem:api/host@1.1.6;
"""

from dataclasses import dataclass
from golem_py_bindings.bindings import types
from golem_py_bindings.bindings.types import Result, Ok, Err
from golem_py_bindings.bindings.imports.host import set_oplog_index, get_oplog_index
from typing import Callable
from .host import atomic_operation_context


@dataclass
class Operation[In, Out, Err]:
    _execute: Callable[[In], Result[Out, Err]]
    _compensate: Callable[[In, Out], Result[None, Err]]

    def execute(self, input: In) -> Result[Out, Err]:
        return self._execute(input)

    def compensate(self, input: In, result: Out) -> Result[None, Err]:
        return self._compensate(input, result)


def operation[In, Out, Err](
    execute: Callable[[In], Result[Out, Err]],
    compensate: Callable[[In, Out], Result[None, Err]],
) -> Operation[In, Out, Err]:
    return Operation(execute, compensate)


@dataclass
class FailedAndRolledBackCompletely[Err]:
    error: Err


@dataclass
class FailedAndRolledBackPartially[Err]:
    error: Err
    compensation_failure: Err


type TransactionFailure[Err] = (
    FailedAndRolledBackCompletely[Err] | FailedAndRolledBackPartially[Err]
)

type TransactionResult[Out, Err] = Result[Out, TransactionFailure[Err]]


@dataclass
class FallibleTransaction[Err]:
    compensations: list[Callable[[], Result[None, Err]]]

    def execute[In, Out](
        self, op: Operation[In, Out, Err], input: In
    ) -> Result[Out, Err]:
        result = op.execute(input)
        if isinstance(result, Ok):
            self.compensations.append(lambda: op.compensate(input, result.value))
        return result

    def _on_failure(self, failure: Err) -> TransactionFailure[Err]:
        for compensation in self.compensations[::-1]:
            comp_result = compensation()
            if isinstance(comp_result, types.Err):
                return FailedAndRolledBackPartially(failure, comp_result.value)
        return FailedAndRolledBackCompletely(failure)


def fallible_transaction[Out, Err](
    f: Callable[[FallibleTransaction[Err]], Result[Out, Err]],
) -> TransactionResult[Out, Err]:
    with atomic_operation_context():
        transaction = FallibleTransaction([])
        result = f(transaction)
        if isinstance(result, types.Err):
            return types.Err(transaction._on_failure(result.value))
        else:
            return result


@dataclass
class InfallibleTransaction:
    compensations: list[Callable[[], None]]
    begin_oplog_index: int

    def execute[In, Out](self, op: Operation[In, Out, Err], input: In) -> Out:
        result = op.execute(input)
        if isinstance(result, Ok):

            def compensation() -> None:
                comp_result = op.compensate(input, result.value)
                if isinstance(comp_result, types.Err):
                    raise ValueError(
                        "Compensating actions are not allowed to fail in infallible transaction",
                        comp_result.value,
                    )
                self.compensations.append(compensation)

            return result.value
        else:
            self._retry()
            raise ValueError("unreachable")

    def _retry(self) -> None:
        # rollback all completed operations and try again
        for compensation in self.compensations[::-1]:
            compensation()
        set_oplog_index(self.begin_oplog_index)


def infallible_transaction[Out](f: Callable[[InfallibleTransaction], Out]) -> Out:
    with atomic_operation_context():
        begin_oplog_index = get_oplog_index()
        transaction = InfallibleTransaction([], begin_oplog_index)
        return f(transaction)
