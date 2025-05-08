from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import poll
from ..imports import wall_clock

@dataclass
class Uuid:
    """
    UUID
    """
    high_bits: int
    low_bits: int

@dataclass
class ComponentId:
    """
    Represents a Golem component
    """
    uuid: Uuid

@dataclass
class WorkerId:
    """
    Represents a Golem worker
    """
    component_id: ComponentId
    worker_name: str

class ResourceMode(Enum):
    OWNED = 0
    BORROWED = 1


@dataclass
class WitTypeNode_RecordType:
    value: List[Tuple[str, int]]


@dataclass
class WitTypeNode_VariantType:
    value: List[Tuple[str, Optional[int]]]


@dataclass
class WitTypeNode_EnumType:
    value: List[str]


@dataclass
class WitTypeNode_FlagsType:
    value: List[str]


@dataclass
class WitTypeNode_TupleType:
    value: List[int]


@dataclass
class WitTypeNode_ListType:
    value: int


@dataclass
class WitTypeNode_OptionType:
    value: int


@dataclass
class WitTypeNode_ResultType:
    value: Tuple[Optional[int], Optional[int]]


@dataclass
class WitTypeNode_PrimU8Type:
    pass


@dataclass
class WitTypeNode_PrimU16Type:
    pass


@dataclass
class WitTypeNode_PrimU32Type:
    pass


@dataclass
class WitTypeNode_PrimU64Type:
    pass


@dataclass
class WitTypeNode_PrimS8Type:
    pass


@dataclass
class WitTypeNode_PrimS16Type:
    pass


@dataclass
class WitTypeNode_PrimS32Type:
    pass


@dataclass
class WitTypeNode_PrimS64Type:
    pass


@dataclass
class WitTypeNode_PrimF32Type:
    pass


@dataclass
class WitTypeNode_PrimF64Type:
    pass


@dataclass
class WitTypeNode_PrimCharType:
    pass


@dataclass
class WitTypeNode_PrimBoolType:
    pass


@dataclass
class WitTypeNode_PrimStringType:
    pass


@dataclass
class WitTypeNode_HandleType:
    value: Tuple[int, ResourceMode]


WitTypeNode = Union[WitTypeNode_RecordType, WitTypeNode_VariantType, WitTypeNode_EnumType, WitTypeNode_FlagsType, WitTypeNode_TupleType, WitTypeNode_ListType, WitTypeNode_OptionType, WitTypeNode_ResultType, WitTypeNode_PrimU8Type, WitTypeNode_PrimU16Type, WitTypeNode_PrimU32Type, WitTypeNode_PrimU64Type, WitTypeNode_PrimS8Type, WitTypeNode_PrimS16Type, WitTypeNode_PrimS32Type, WitTypeNode_PrimS64Type, WitTypeNode_PrimF32Type, WitTypeNode_PrimF64Type, WitTypeNode_PrimCharType, WitTypeNode_PrimBoolType, WitTypeNode_PrimStringType, WitTypeNode_HandleType]


@dataclass
class WitType:
    nodes: List[WitTypeNode]

@dataclass
class Uri:
    value: str


@dataclass
class WitNode_RecordValue:
    value: List[int]


@dataclass
class WitNode_VariantValue:
    value: Tuple[int, Optional[int]]


@dataclass
class WitNode_EnumValue:
    value: int


@dataclass
class WitNode_FlagsValue:
    value: List[bool]


@dataclass
class WitNode_TupleValue:
    value: List[int]


@dataclass
class WitNode_ListValue:
    value: List[int]


@dataclass
class WitNode_OptionValue:
    value: Optional[int]


@dataclass
class WitNode_ResultValue:
    value: Result[Optional[int], Optional[int]]


@dataclass
class WitNode_PrimU8:
    value: int


@dataclass
class WitNode_PrimU16:
    value: int


@dataclass
class WitNode_PrimU32:
    value: int


@dataclass
class WitNode_PrimU64:
    value: int


@dataclass
class WitNode_PrimS8:
    value: int


@dataclass
class WitNode_PrimS16:
    value: int


@dataclass
class WitNode_PrimS32:
    value: int


@dataclass
class WitNode_PrimS64:
    value: int


@dataclass
class WitNode_PrimFloat32:
    value: float


@dataclass
class WitNode_PrimFloat64:
    value: float


@dataclass
class WitNode_PrimChar:
    value: str


@dataclass
class WitNode_PrimBool:
    value: bool


@dataclass
class WitNode_PrimString:
    value: str


@dataclass
class WitNode_Handle:
    value: Tuple[Uri, int]


WitNode = Union[WitNode_RecordValue, WitNode_VariantValue, WitNode_EnumValue, WitNode_FlagsValue, WitNode_TupleValue, WitNode_ListValue, WitNode_OptionValue, WitNode_ResultValue, WitNode_PrimU8, WitNode_PrimU16, WitNode_PrimU32, WitNode_PrimU64, WitNode_PrimS8, WitNode_PrimS16, WitNode_PrimS32, WitNode_PrimS64, WitNode_PrimFloat32, WitNode_PrimFloat64, WitNode_PrimChar, WitNode_PrimBool, WitNode_PrimString, WitNode_Handle]


@dataclass
class WitValue:
    nodes: List[WitNode]

@dataclass
class ValueAndType:
    value: WitValue
    typ: WitType


@dataclass
class RpcError_ProtocolError:
    value: str


@dataclass
class RpcError_Denied:
    value: str


@dataclass
class RpcError_NotFound:
    value: str


@dataclass
class RpcError_RemoteInternalError:
    value: str


RpcError = Union[RpcError_ProtocolError, RpcError_Denied, RpcError_NotFound, RpcError_RemoteInternalError]


class FutureInvokeResult:
    
    def subscribe(self) -> poll.Pollable:
        raise NotImplementedError
    def get(self) -> Optional[Result[WitValue, RpcError]]:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError


class CancellationToken:
    
    def cancel(self) -> None:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError


class WasmRpc:
    
    def __init__(self, worker_id: WorkerId) -> None:
        raise NotImplementedError

    @classmethod
    def ephemeral(cls, component_id: ComponentId) -> Self:
        raise NotImplementedError
    def invoke_and_await(self, function_name: str, function_params: List[WitValue]) -> WitValue:
        """
        Raises: `bindings.types.Err(bindings.imports.golem_rpc_types.RpcError)`
        """
        raise NotImplementedError
    def invoke(self, function_name: str, function_params: List[WitValue]) -> None:
        """
        Raises: `bindings.types.Err(bindings.imports.golem_rpc_types.RpcError)`
        """
        raise NotImplementedError
    def async_invoke_and_await(self, function_name: str, function_params: List[WitValue]) -> FutureInvokeResult:
        raise NotImplementedError
    def schedule_invocation(self, scheduled_time: wall_clock.Datetime, function_name: str, function_params: List[WitValue]) -> None:
        """
        Schedule invocation for later
        """
        raise NotImplementedError
    def schedule_cancelable_invocation(self, scheduled_time: wall_clock.Datetime, function_name: str, function_params: List[WitValue]) -> CancellationToken:
        """
        Schedule invocation for later. Call cancel on the returned resource to cancel the invocation before the scheduled time.
        """
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



def parse_uuid(uuid: str) -> Uuid:
    """
    Parses a UUID from a string
    
    Raises: `bindings.types.Err(bindings.imports.str)`
    """
    raise NotImplementedError

def uuid_to_string(uuid: Uuid) -> str:
    """
    Converts a UUID to a string
    """
    raise NotImplementedError

def extract_value(vnt: ValueAndType) -> WitValue:
    raise NotImplementedError

def extract_type(vnt: ValueAndType) -> WitType:
    raise NotImplementedError

