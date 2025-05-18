"""
The Golem host API provides low level access to Golem specific features such as promises and control over
the durability and transactional guarantees the executor provides.
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import golem_rpc_types

@dataclass
class PromiseId:
    """
    A promise ID is a value that can be passed to an external Golem API to complete that promise
    from an arbitrary external source, while Golem workers can await for this completion.
    """
    worker_id: golem_rpc_types.WorkerId
    oplog_idx: int

@dataclass
class AccountId:
    """
    Represents a Golem Cloud account
    """
    value: str

@dataclass
class RetryPolicy:
    """
    Configures how the executor retries failures
    """
    max_attempts: int
    min_delay: int
    max_delay: int
    multiplier: float
    max_jitter_factor: Optional[float]


@dataclass
class PersistenceLevel_PersistNothing:
    pass


@dataclass
class PersistenceLevel_PersistRemoteSideEffects:
    pass


@dataclass
class PersistenceLevel_Smart:
    pass


PersistenceLevel = Union[PersistenceLevel_PersistNothing, PersistenceLevel_PersistRemoteSideEffects, PersistenceLevel_Smart]
"""
Configurable persistence level for workers
"""


class UpdateMode(Enum):
    """
    Describes how to update a worker to a different component version
    """
    AUTOMATIC = 0
    SNAPSHOT_BASED = 1

class FilterComparator(Enum):
    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_EQUAL = 2
    GREATER = 3
    LESS_EQUAL = 4
    LESS = 5

class StringFilterComparator(Enum):
    EQUAL = 0
    NOT_EQUAL = 1
    LIKE = 2
    NOT_LIKE = 3

class WorkerStatus(Enum):
    RUNNING = 0
    IDLE = 1
    SUSPENDED = 2
    INTERRUPTED = 3
    RETRYING = 4
    FAILED = 5
    EXITED = 6

@dataclass
class WorkerNameFilter:
    comparator: StringFilterComparator
    value: str

@dataclass
class WorkerStatusFilter:
    comparator: FilterComparator
    value: WorkerStatus

@dataclass
class WorkerVersionFilter:
    comparator: FilterComparator
    value: int

@dataclass
class WorkerCreatedAtFilter:
    comparator: FilterComparator
    value: int

@dataclass
class WorkerEnvFilter:
    name: str
    comparator: StringFilterComparator
    value: str


@dataclass
class WorkerPropertyFilter_Name:
    value: WorkerNameFilter


@dataclass
class WorkerPropertyFilter_Status:
    value: WorkerStatusFilter


@dataclass
class WorkerPropertyFilter_Version:
    value: WorkerVersionFilter


@dataclass
class WorkerPropertyFilter_CreatedAt:
    value: WorkerCreatedAtFilter


@dataclass
class WorkerPropertyFilter_Env:
    value: WorkerEnvFilter


WorkerPropertyFilter = Union[WorkerPropertyFilter_Name, WorkerPropertyFilter_Status, WorkerPropertyFilter_Version, WorkerPropertyFilter_CreatedAt, WorkerPropertyFilter_Env]


@dataclass
class WorkerAllFilter:
    filters: List[WorkerPropertyFilter]

@dataclass
class WorkerAnyFilter:
    filters: List[WorkerAllFilter]

@dataclass
class WorkerMetadata:
    worker_id: golem_rpc_types.WorkerId
    args: List[str]
    env: List[Tuple[str, str]]
    status: WorkerStatus
    component_version: int
    retry_count: int

class GetWorkers:
    
    def __init__(self, component_id: golem_rpc_types.ComponentId, filter: Optional[WorkerAnyFilter], precise: bool) -> None:
        raise NotImplementedError

    def get_next(self) -> Optional[List[WorkerMetadata]]:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



@dataclass
class RevertWorkerTarget_RevertToOplogIndex:
    value: int


@dataclass
class RevertWorkerTarget_RevertLastInvocations:
    value: int


RevertWorkerTarget = Union[RevertWorkerTarget_RevertToOplogIndex, RevertWorkerTarget_RevertLastInvocations]
"""
Target parameter for the `revert-worker` operation
"""


class ForkResult(Enum):
    """
    Indicates which worker the code is running on after `fork`
    """
    ORIGINAL = 0
    FORKED = 1


def create_promise() -> PromiseId:
    """
    Create a new promise
    """
    raise NotImplementedError

def await_promise(promise_id: PromiseId) -> bytes:
    """
    Suspends execution until the given promise gets completed, and returns the payload passed to
    the promise completion.
    """
    raise NotImplementedError

def poll_promise(promise_id: PromiseId) -> Optional[bytes]:
    """
    Checks whether the given promise is completed. If not, it returns None. If the promise is completed,
    it returns the payload passed to the promise completion.
    """
    raise NotImplementedError

def complete_promise(promise_id: PromiseId, data: bytes) -> bool:
    """
    Completes the given promise with the given payload. Returns true if the promise was completed, false
    if the promise was already completed. The payload is passed to the worker that is awaiting the promise.
    """
    raise NotImplementedError

def delete_promise(promise_id: PromiseId) -> None:
    """
    Deletes the given promise
    """
    raise NotImplementedError

def get_oplog_index() -> int:
    """
    Returns the current position in the persistent op log
    """
    raise NotImplementedError

def set_oplog_index(oplog_idx: int) -> None:
    """
    Makes the current worker travel back in time and continue execution from the given position in the persistent
    op log.
    """
    raise NotImplementedError

def oplog_commit(replicas: int) -> None:
    """
    Blocks the execution until the oplog has been written to at least the specified number of replicas,
    or the maximum number of replicas if the requested number is higher.
    """
    raise NotImplementedError

def mark_begin_operation() -> int:
    """
    Marks the beginning of an atomic operation.
    In case of a failure within the region selected by `mark-begin-operation` and `mark-end-operation`
    the whole region will be reexecuted on retry.
    The end of the region is when `mark-end-operation` is called with the returned oplog-index.
    """
    raise NotImplementedError

def mark_end_operation(begin: int) -> None:
    """
    Commits this atomic operation. After `mark-end-operation` is called for a given index, further calls
    with the same parameter will do nothing.
    """
    raise NotImplementedError

def get_retry_policy() -> RetryPolicy:
    """
    Gets the current retry policy associated with the worker
    """
    raise NotImplementedError

def set_retry_policy(new_retry_policy: RetryPolicy) -> None:
    """
    Overrides the current retry policy associated with the worker. Following this call, `get-retry-policy` will return the
    new retry policy.
    """
    raise NotImplementedError

def get_oplog_persistence_level() -> PersistenceLevel:
    """
    Gets the worker's current persistence level.
    """
    raise NotImplementedError

def set_oplog_persistence_level(new_persistence_level: PersistenceLevel) -> None:
    """
    Sets the worker's current persistence level. This can increase the performance of execution in cases where durable
    execution is not required.
    """
    raise NotImplementedError

def get_idempotence_mode() -> bool:
    """
    Gets the current idempotence mode. See `set-idempotence-mode` for details.
    """
    raise NotImplementedError

def set_idempotence_mode(idempotent: bool) -> None:
    """
    Sets the current idempotence mode. The default is true.
    True means side-effects are treated idempotent and Golem guarantees at-least-once semantics.
    In case of false the executor provides at-most-once semantics, failing the worker in case it is
    not known if the side effect was already executed.
    """
    raise NotImplementedError

def generate_idempotency_key() -> golem_rpc_types.Uuid:
    """
    Generates an idempotency key. This operation will never be replayed —
    i.e. not only is this key generated, but it is persisted and committed, such that the key can be used in third-party systems (e.g. payment processing)
    to introduce idempotence.
    """
    raise NotImplementedError

def update_worker(worker_id: golem_rpc_types.WorkerId, target_version: int, mode: UpdateMode) -> None:
    """
    Initiates an update attempt for the given worker. The function returns immediately once the request has been processed,
    not waiting for the worker to get updated.
    """
    raise NotImplementedError

def get_self_metadata() -> WorkerMetadata:
    """
    Get current worker metadata
    """
    raise NotImplementedError

def get_worker_metadata(worker_id: golem_rpc_types.WorkerId) -> Optional[WorkerMetadata]:
    """
    Get worker metadata
    """
    raise NotImplementedError

def fork_worker(source_worker_id: golem_rpc_types.WorkerId, target_worker_id: golem_rpc_types.WorkerId, oplog_idx_cut_off: int) -> None:
    """
    Fork a worker to another worker at a given oplog index
    """
    raise NotImplementedError

def revert_worker(worker_id: golem_rpc_types.WorkerId, revert_target: RevertWorkerTarget) -> None:
    """
    Revert a worker to a previous state
    """
    raise NotImplementedError

def resolve_component_id(component_reference: str) -> Optional[golem_rpc_types.ComponentId]:
    """
    Get the component-id for a given component reference.
    Returns none when no component with the specified reference exists.
    The syntax of the component reference is implementation dependent.
    
    Golem OSS: "{component_name}"
    Golem Cloud:
        1: "{component_name}" -> will resolve in current account and project
        2: "{project_name}/{component_name}" -> will resolve in current account
        3: "{account_id}/{project_name}/{component_name}"
    """
    raise NotImplementedError

def resolve_worker_id(component_reference: str, worker_name: str) -> Optional[golem_rpc_types.WorkerId]:
    """
    Get the worker-id for a given component and worker name.
    Returns none when no component for the specified reference exists.
    """
    raise NotImplementedError

def resolve_worker_id_strict(component_reference: str, worker_name: str) -> Optional[golem_rpc_types.WorkerId]:
    """
    Get the worker-id for a given component and worker name.
    Returns none when no component for the specified component-reference or no worker with the specified worker-name exists.
    """
    raise NotImplementedError

def fork(new_name: str) -> ForkResult:
    """
    Forks the current worker at the current execution point. The new worker gets the `new-name` worker name,
    and this worker continues running as well. The return value is going to be different in this worker and
    the forked worker.
    """
    raise NotImplementedError

