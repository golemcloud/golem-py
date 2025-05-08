"""
Host interface for enumerating and searching for worker oplogs
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import host
from ..imports import golem_rpc_types
from ..imports import context
from ..imports import wall_clock


@dataclass
class WrappedFunctionType_ReadLocal:
    pass


@dataclass
class WrappedFunctionType_WriteLocal:
    pass


@dataclass
class WrappedFunctionType_ReadRemote:
    pass


@dataclass
class WrappedFunctionType_WriteRemote:
    pass


@dataclass
class WrappedFunctionType_WriteRemoteBatched:
    value: Optional[int]


WrappedFunctionType = Union[WrappedFunctionType_ReadLocal, WrappedFunctionType_WriteLocal, WrappedFunctionType_ReadRemote, WrappedFunctionType_WriteRemote, WrappedFunctionType_WriteRemoteBatched]


@dataclass
class PluginInstallationDescription:
    installation_id: golem_rpc_types.Uuid
    name: str
    version: str
    parameters: List[Tuple[str, str]]

@dataclass
class CreateParameters:
    timestamp: wall_clock.Datetime
    worker_id: golem_rpc_types.WorkerId
    component_version: int
    args: List[str]
    env: List[Tuple[str, str]]
    account_id: host.AccountId
    parent: Optional[golem_rpc_types.WorkerId]
    component_size: int
    initial_total_linear_memory_size: int
    initial_active_plugins: List[PluginInstallationDescription]

@dataclass
class ImportedFunctionInvokedParameters:
    timestamp: wall_clock.Datetime
    function_name: str
    request: golem_rpc_types.WitValue
    response: golem_rpc_types.WitValue
    wrapped_function_type: WrappedFunctionType

@dataclass
class LocalSpanData:
    span_id: str
    start: wall_clock.Datetime
    parent: Optional[str]
    linked_context: Optional[int]
    attributes: List[context.Attribute]
    inherited: bool

@dataclass
class ExternalSpanData:
    span_id: str


@dataclass
class SpanData_LocalSpan:
    value: LocalSpanData


@dataclass
class SpanData_ExternalSpan:
    value: ExternalSpanData


SpanData = Union[SpanData_LocalSpan, SpanData_ExternalSpan]


@dataclass
class ExportedFunctionInvokedParameters:
    timestamp: wall_clock.Datetime
    function_name: str
    request: List[golem_rpc_types.WitValue]
    idempotency_key: str
    trace_id: str
    trace_states: List[str]
    invocation_context: List[List[SpanData]]

@dataclass
class ExportedFunctionCompletedParameters:
    timestamp: wall_clock.Datetime
    response: golem_rpc_types.WitValue
    consumed_fuel: int

@dataclass
class ErrorParameters:
    timestamp: wall_clock.Datetime
    error: str

@dataclass
class JumpParameters:
    timestamp: wall_clock.Datetime
    start: int
    end: int

@dataclass
class ChangeRetryPolicyParameters:
    timestamp: wall_clock.Datetime
    retry_policy: host.RetryPolicy

@dataclass
class EndAtomicRegionParameters:
    timestamp: wall_clock.Datetime
    begin_index: int

@dataclass
class EndRemoteWriteParameters:
    timestamp: wall_clock.Datetime
    begin_index: int

@dataclass
class ExportedFunctionInvocationParameters:
    idempotency_key: str
    function_name: str
    input: Optional[List[golem_rpc_types.WitValue]]


@dataclass
class WorkerInvocation_ExportedFunction:
    value: ExportedFunctionInvocationParameters


@dataclass
class WorkerInvocation_ManualUpdate:
    value: int


WorkerInvocation = Union[WorkerInvocation_ExportedFunction, WorkerInvocation_ManualUpdate]


@dataclass
class PendingWorkerInvocationParameters:
    timestamp: wall_clock.Datetime
    invocation: WorkerInvocation


@dataclass
class UpdateDescription_AutoUpdate:
    pass


@dataclass
class UpdateDescription_SnapshotBased:
    value: bytes


UpdateDescription = Union[UpdateDescription_AutoUpdate, UpdateDescription_SnapshotBased]


@dataclass
class PendingUpdateParameters:
    timestamp: wall_clock.Datetime
    target_version: int
    update_description: UpdateDescription

@dataclass
class SuccessfulUpdateParameters:
    timestamp: wall_clock.Datetime
    target_version: int
    new_component_size: int
    new_active_plugins: List[PluginInstallationDescription]

@dataclass
class FailedUpdateParameters:
    timestamp: wall_clock.Datetime
    target_version: int
    details: Optional[str]

@dataclass
class GrowMemoryParameters:
    timestamp: wall_clock.Datetime
    delta: int

@dataclass
class CreateResourceParameters:
    timestamp: wall_clock.Datetime
    resource_id: int

@dataclass
class DropResourceParameters:
    timestamp: wall_clock.Datetime
    resource_id: int

@dataclass
class DescribeResourceParameters:
    timestamp: wall_clock.Datetime
    resource_id: int
    resource_name: str
    resource_params: List[golem_rpc_types.WitValue]

class LogLevel(Enum):
    STDOUT = 0
    STDERR = 1
    TRACE = 2
    DEBUG = 3
    INFO = 4
    WARN = 5
    ERROR = 6
    CRITICAL = 7

@dataclass
class LogParameters:
    timestamp: wall_clock.Datetime
    level: LogLevel
    context: str
    message: str

@dataclass
class ActivatePluginParameters:
    timestamp: wall_clock.Datetime
    plugin: PluginInstallationDescription

@dataclass
class DeactivatePluginParameters:
    timestamp: wall_clock.Datetime
    plugin: PluginInstallationDescription

@dataclass
class RevertParameters:
    timestamp: wall_clock.Datetime
    start: int
    end: int

@dataclass
class CancelInvocationParameters:
    timestamp: wall_clock.Datetime
    idempotency_key: str

@dataclass
class StartSpanParameters:
    timestamp: wall_clock.Datetime
    span_id: str
    parent: Optional[str]
    linked_context: Optional[str]
    attributes: List[context.Attribute]

@dataclass
class FinishSpanParameters:
    timestamp: wall_clock.Datetime
    span_id: str

@dataclass
class SetSpanAttributeParameters:
    timestamp: wall_clock.Datetime
    span_id: str
    key: str
    value: context.AttributeValue

@dataclass
class ChangePersistenceLevelParameters:
    timestamp: wall_clock.Datetime
    persistence_level: host.PersistenceLevel


@dataclass
class OplogEntry_Create:
    value: CreateParameters


@dataclass
class OplogEntry_ImportedFunctionInvoked:
    value: ImportedFunctionInvokedParameters


@dataclass
class OplogEntry_ExportedFunctionInvoked:
    value: ExportedFunctionInvokedParameters


@dataclass
class OplogEntry_ExportedFunctionCompleted:
    value: ExportedFunctionCompletedParameters


@dataclass
class OplogEntry_Suspend:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_Error:
    value: ErrorParameters


@dataclass
class OplogEntry_NoOp:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_Jump:
    value: JumpParameters


@dataclass
class OplogEntry_Interrupted:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_Exited:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_ChangeRetryPolicy:
    value: ChangeRetryPolicyParameters


@dataclass
class OplogEntry_BeginAtomicRegion:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_EndAtomicRegion:
    value: EndAtomicRegionParameters


@dataclass
class OplogEntry_BeginRemoteWrite:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_EndRemoteWrite:
    value: EndRemoteWriteParameters


@dataclass
class OplogEntry_PendingWorkerInvocation:
    value: PendingWorkerInvocationParameters


@dataclass
class OplogEntry_PendingUpdate:
    value: PendingUpdateParameters


@dataclass
class OplogEntry_SuccessfulUpdate:
    value: SuccessfulUpdateParameters


@dataclass
class OplogEntry_FailedUpdate:
    value: FailedUpdateParameters


@dataclass
class OplogEntry_GrowMemory:
    value: GrowMemoryParameters


@dataclass
class OplogEntry_CreateResource:
    value: CreateResourceParameters


@dataclass
class OplogEntry_DropResource:
    value: DropResourceParameters


@dataclass
class OplogEntry_DescribeResource:
    value: DescribeResourceParameters


@dataclass
class OplogEntry_Log:
    value: LogParameters


@dataclass
class OplogEntry_Restart:
    value: wall_clock.Datetime


@dataclass
class OplogEntry_ActivatePlugin:
    value: ActivatePluginParameters


@dataclass
class OplogEntry_DeactivatePlugin:
    value: DeactivatePluginParameters


@dataclass
class OplogEntry_Revert:
    value: RevertParameters


@dataclass
class OplogEntry_CancelInvocation:
    value: CancelInvocationParameters


@dataclass
class OplogEntry_StartSpan:
    value: StartSpanParameters


@dataclass
class OplogEntry_FinishSpan:
    value: FinishSpanParameters


@dataclass
class OplogEntry_SetSpanAttribute:
    value: SetSpanAttributeParameters


@dataclass
class OplogEntry_ChangePersistenceLevel:
    value: ChangePersistenceLevelParameters


OplogEntry = Union[OplogEntry_Create, OplogEntry_ImportedFunctionInvoked, OplogEntry_ExportedFunctionInvoked, OplogEntry_ExportedFunctionCompleted, OplogEntry_Suspend, OplogEntry_Error, OplogEntry_NoOp, OplogEntry_Jump, OplogEntry_Interrupted, OplogEntry_Exited, OplogEntry_ChangeRetryPolicy, OplogEntry_BeginAtomicRegion, OplogEntry_EndAtomicRegion, OplogEntry_BeginRemoteWrite, OplogEntry_EndRemoteWrite, OplogEntry_PendingWorkerInvocation, OplogEntry_PendingUpdate, OplogEntry_SuccessfulUpdate, OplogEntry_FailedUpdate, OplogEntry_GrowMemory, OplogEntry_CreateResource, OplogEntry_DropResource, OplogEntry_DescribeResource, OplogEntry_Log, OplogEntry_Restart, OplogEntry_ActivatePlugin, OplogEntry_DeactivatePlugin, OplogEntry_Revert, OplogEntry_CancelInvocation, OplogEntry_StartSpan, OplogEntry_FinishSpan, OplogEntry_SetSpanAttribute, OplogEntry_ChangePersistenceLevel]


class GetOplog:
    
    def __init__(self, worker_id: golem_rpc_types.WorkerId, start: int) -> None:
        raise NotImplementedError

    def get_next(self) -> Optional[List[OplogEntry]]:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError


class SearchOplog:
    
    def __init__(self, worker_id: golem_rpc_types.WorkerId, text: str) -> None:
        raise NotImplementedError

    def get_next(self) -> Optional[List[Tuple[int, OplogEntry]]]:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



