from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import host
from ..imports import golem_rpc_types
from ..imports import oplog
from ..imports import poll
from ..imports import wall_clock

@dataclass
class DurableExecutionState:
    is_live: bool
    persistence_level: host.PersistenceLevel

class OplogEntryVersion(Enum):
    V1 = 0
    V2 = 1

@dataclass
class PersistedDurableFunctionInvocation:
    timestamp: wall_clock.Datetime
    function_name: str
    response: bytes
    function_type: oplog.WrappedFunctionType
    entry_version: OplogEntryVersion

@dataclass
class PersistedTypedDurableFunctionInvocation:
    timestamp: wall_clock.Datetime
    function_name: str
    response: golem_rpc_types.ValueAndType
    function_type: oplog.WrappedFunctionType
    entry_version: OplogEntryVersion

class LazyInitializedPollable:
    
    def __init__(self) -> None:
        """
        Creates a `pollable` that is never ready until it gets attached to a real `pollable` implementation
        using `set-lazy-initialized-pollable`.
        """
        raise NotImplementedError

    def set(self, pollable: poll.Pollable) -> None:
        """
        Sets the underlying `pollable` for a pollable created with `create-lazy-initialized-pollable`.
        """
        raise NotImplementedError
    def subscribe(self) -> poll.Pollable:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



def observe_function_call(iface: str, function: str) -> None:
    """
    Observes a function call (produces logs and metrics)
    """
    raise NotImplementedError

def begin_durable_function(function_type: oplog.WrappedFunctionType) -> int:
    """
    Marks the beginning of a durable function.
    
    There must be a corresponding call to `end-durable-function` after the function has
    performed its work (it can be ended in a different context, for example after an async
    pollable operation has been completed)
    """
    raise NotImplementedError

def end_durable_function(function_type: oplog.WrappedFunctionType, begin_index: int, forced_commit: bool) -> None:
    """
    Marks the end of a durable function
    
    This is a pair of `begin-durable-function` and should be called after the durable function
    has performed and persisted or replayed its work. The `begin-index` should be the index
    returned by `begin-durable-function`.
    
    Normally commit behavior is decided by the executor based on the `function-type`. However, in special
    cases the `forced-commit` parameter can be used to force commit the oplog in an efficient way.
    """
    raise NotImplementedError

def current_durable_execution_state() -> DurableExecutionState:
    """
    Gets the current durable execution state
    """
    raise NotImplementedError

def persist_durable_function_invocation(function_name: str, request: bytes, response: bytes, function_type: oplog.WrappedFunctionType) -> None:
    """
    Writes a record to the worker's oplog representing a durable function invocation
    """
    raise NotImplementedError

def persist_typed_durable_function_invocation(function_name: str, request: golem_rpc_types.ValueAndType, response: golem_rpc_types.ValueAndType, function_type: oplog.WrappedFunctionType) -> None:
    """
    Writes a record to the worker's oplog representing a durable function invocation
    
    The request and response are defined as pairs of value and type, which makes it
    self-describing for observers of oplogs. This is the recommended way to persist
    third-party function invocations.
    """
    raise NotImplementedError

def read_persisted_durable_function_invocation() -> PersistedDurableFunctionInvocation:
    """
    Reads the next persisted durable function invocation from the oplog during replay
    """
    raise NotImplementedError

def read_persisted_typed_durable_function_invocation() -> PersistedTypedDurableFunctionInvocation:
    """
    Reads the next persisted durable function invocation from the oplog during replay, assuming it
    was created with `persist-typed-durable-function-invocation`
    """
    raise NotImplementedError

