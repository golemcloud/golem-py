from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import golem_rdbms_types


@dataclass
class Error_ConnectionFailure:
    value: str


@dataclass
class Error_QueryParameterFailure:
    value: str


@dataclass
class Error_QueryExecutionFailure:
    value: str


@dataclass
class Error_QueryResponseFailure:
    value: str


@dataclass
class Error_Other:
    value: str


Error = Union[Error_ConnectionFailure, Error_QueryParameterFailure, Error_QueryExecutionFailure, Error_QueryResponseFailure, Error_Other]


@dataclass
class Interval:
    months: int
    days: int
    microseconds: int


@dataclass
class Int4bound_Included:
    value: int


@dataclass
class Int4bound_Excluded:
    value: int


@dataclass
class Int4bound_Unbounded:
    pass


Int4bound = Union[Int4bound_Included, Int4bound_Excluded, Int4bound_Unbounded]



@dataclass
class Int8bound_Included:
    value: int


@dataclass
class Int8bound_Excluded:
    value: int


@dataclass
class Int8bound_Unbounded:
    pass


Int8bound = Union[Int8bound_Included, Int8bound_Excluded, Int8bound_Unbounded]



@dataclass
class Numbound_Included:
    value: str


@dataclass
class Numbound_Excluded:
    value: str


@dataclass
class Numbound_Unbounded:
    pass


Numbound = Union[Numbound_Included, Numbound_Excluded, Numbound_Unbounded]



@dataclass
class Tsbound_Included:
    value: golem_rdbms_types.Timestamp


@dataclass
class Tsbound_Excluded:
    value: golem_rdbms_types.Timestamp


@dataclass
class Tsbound_Unbounded:
    pass


Tsbound = Union[Tsbound_Included, Tsbound_Excluded, Tsbound_Unbounded]



@dataclass
class Tstzbound_Included:
    value: golem_rdbms_types.Timestamptz


@dataclass
class Tstzbound_Excluded:
    value: golem_rdbms_types.Timestamptz


@dataclass
class Tstzbound_Unbounded:
    pass


Tstzbound = Union[Tstzbound_Included, Tstzbound_Excluded, Tstzbound_Unbounded]



@dataclass
class Datebound_Included:
    value: golem_rdbms_types.Date


@dataclass
class Datebound_Excluded:
    value: golem_rdbms_types.Date


@dataclass
class Datebound_Unbounded:
    pass


Datebound = Union[Datebound_Included, Datebound_Excluded, Datebound_Unbounded]


@dataclass
class Int4range:
    start: Int4bound
    end: Int4bound

@dataclass
class Int8range:
    start: Int8bound
    end: Int8bound

@dataclass
class Numrange:
    start: Numbound
    end: Numbound

@dataclass
class Tsrange:
    start: Tsbound
    end: Tsbound

@dataclass
class Tstzrange:
    start: Tstzbound
    end: Tstzbound

@dataclass
class Daterange:
    start: Datebound
    end: Datebound

@dataclass
class EnumerationType:
    name: str

@dataclass
class Enumeration:
    name: str
    value: str

@dataclass
class Composite:
    name: str
    values: List[Any]

@dataclass
class Domain:
    name: str
    value: Any


@dataclass
class ValueBound_Included:
    value: Any


@dataclass
class ValueBound_Excluded:
    value: Any


@dataclass
class ValueBound_Unbounded:
    pass


ValueBound = Union[ValueBound_Included, ValueBound_Excluded, ValueBound_Unbounded]


@dataclass
class ValuesRange:
    start: ValueBound
    end: ValueBound

@dataclass
class Range:
    name: str
    value: ValuesRange


@dataclass
class DbValue_Character:
    value: int


@dataclass
class DbValue_Int2:
    value: int


@dataclass
class DbValue_Int4:
    value: int


@dataclass
class DbValue_Int8:
    value: int


@dataclass
class DbValue_Float4:
    value: float


@dataclass
class DbValue_Float8:
    value: float


@dataclass
class DbValue_Numeric:
    value: str


@dataclass
class DbValue_Boolean:
    value: bool


@dataclass
class DbValue_Text:
    value: str


@dataclass
class DbValue_Varchar:
    value: str


@dataclass
class DbValue_Bpchar:
    value: str


@dataclass
class DbValue_Timestamp:
    value: golem_rdbms_types.Timestamp


@dataclass
class DbValue_Timestamptz:
    value: golem_rdbms_types.Timestamptz


@dataclass
class DbValue_Date:
    value: golem_rdbms_types.Date


@dataclass
class DbValue_Time:
    value: golem_rdbms_types.Time


@dataclass
class DbValue_Timetz:
    value: golem_rdbms_types.Timetz


@dataclass
class DbValue_Interval:
    value: Interval


@dataclass
class DbValue_Bytea:
    value: bytes


@dataclass
class DbValue_Json:
    value: str


@dataclass
class DbValue_Jsonb:
    value: str


@dataclass
class DbValue_Jsonpath:
    value: str


@dataclass
class DbValue_Xml:
    value: str


@dataclass
class DbValue_Uuid:
    value: golem_rdbms_types.Uuid


@dataclass
class DbValue_Inet:
    value: golem_rdbms_types.IpAddress


@dataclass
class DbValue_Cidr:
    value: golem_rdbms_types.IpAddress


@dataclass
class DbValue_Macaddr:
    value: golem_rdbms_types.MacAddress


@dataclass
class DbValue_Bit:
    value: List[bool]


@dataclass
class DbValue_Varbit:
    value: List[bool]


@dataclass
class DbValue_Int4range:
    value: Int4range


@dataclass
class DbValue_Int8range:
    value: Int8range


@dataclass
class DbValue_Numrange:
    value: Numrange


@dataclass
class DbValue_Tsrange:
    value: Tsrange


@dataclass
class DbValue_Tstzrange:
    value: Tstzrange


@dataclass
class DbValue_Daterange:
    value: Daterange


@dataclass
class DbValue_Money:
    value: int


@dataclass
class DbValue_Oid:
    value: int


@dataclass
class DbValue_Enumeration:
    value: Enumeration


@dataclass
class DbValue_Composite:
    value: Composite


@dataclass
class DbValue_Domain:
    value: Domain


@dataclass
class DbValue_Array:
    value: List[Any]


@dataclass
class DbValue_Range:
    value: Range


@dataclass
class DbValue_Null:
    pass


DbValue = Union[DbValue_Character, DbValue_Int2, DbValue_Int4, DbValue_Int8, DbValue_Float4, DbValue_Float8, DbValue_Numeric, DbValue_Boolean, DbValue_Text, DbValue_Varchar, DbValue_Bpchar, DbValue_Timestamp, DbValue_Timestamptz, DbValue_Date, DbValue_Time, DbValue_Timetz, DbValue_Interval, DbValue_Bytea, DbValue_Json, DbValue_Jsonb, DbValue_Jsonpath, DbValue_Xml, DbValue_Uuid, DbValue_Inet, DbValue_Cidr, DbValue_Macaddr, DbValue_Bit, DbValue_Varbit, DbValue_Int4range, DbValue_Int8range, DbValue_Numrange, DbValue_Tsrange, DbValue_Tstzrange, DbValue_Daterange, DbValue_Money, DbValue_Oid, DbValue_Enumeration, DbValue_Composite, DbValue_Domain, DbValue_Array, DbValue_Range, DbValue_Null]


class LazyDbValue:
    
    def __init__(self, value: DbValue) -> None:
        raise NotImplementedError

    def get(self) -> DbValue:
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
class CompositeType:
    name: str
    attributes: List[Tuple[str, Any]]

@dataclass
class DomainType:
    name: str
    base_type: Any

@dataclass
class RangeType:
    name: str
    base_type: Any


@dataclass
class DbColumnType_Character:
    pass


@dataclass
class DbColumnType_Int2:
    pass


@dataclass
class DbColumnType_Int4:
    pass


@dataclass
class DbColumnType_Int8:
    pass


@dataclass
class DbColumnType_Float4:
    pass


@dataclass
class DbColumnType_Float8:
    pass


@dataclass
class DbColumnType_Numeric:
    pass


@dataclass
class DbColumnType_Boolean:
    pass


@dataclass
class DbColumnType_Text:
    pass


@dataclass
class DbColumnType_Varchar:
    pass


@dataclass
class DbColumnType_Bpchar:
    pass


@dataclass
class DbColumnType_Timestamp:
    pass


@dataclass
class DbColumnType_Timestamptz:
    pass


@dataclass
class DbColumnType_Date:
    pass


@dataclass
class DbColumnType_Time:
    pass


@dataclass
class DbColumnType_Timetz:
    pass


@dataclass
class DbColumnType_Interval:
    pass


@dataclass
class DbColumnType_Bytea:
    pass


@dataclass
class DbColumnType_Uuid:
    pass


@dataclass
class DbColumnType_Xml:
    pass


@dataclass
class DbColumnType_Json:
    pass


@dataclass
class DbColumnType_Jsonb:
    pass


@dataclass
class DbColumnType_Jsonpath:
    pass


@dataclass
class DbColumnType_Inet:
    pass


@dataclass
class DbColumnType_Cidr:
    pass


@dataclass
class DbColumnType_Macaddr:
    pass


@dataclass
class DbColumnType_Bit:
    pass


@dataclass
class DbColumnType_Varbit:
    pass


@dataclass
class DbColumnType_Int4range:
    pass


@dataclass
class DbColumnType_Int8range:
    pass


@dataclass
class DbColumnType_Numrange:
    pass


@dataclass
class DbColumnType_Tsrange:
    pass


@dataclass
class DbColumnType_Tstzrange:
    pass


@dataclass
class DbColumnType_Daterange:
    pass


@dataclass
class DbColumnType_Money:
    pass


@dataclass
class DbColumnType_Oid:
    pass


@dataclass
class DbColumnType_Enumeration:
    value: EnumerationType


@dataclass
class DbColumnType_Composite:
    value: CompositeType


@dataclass
class DbColumnType_Domain:
    value: DomainType


@dataclass
class DbColumnType_Array:
    value: Any


@dataclass
class DbColumnType_Range:
    value: RangeType


DbColumnType = Union[DbColumnType_Character, DbColumnType_Int2, DbColumnType_Int4, DbColumnType_Int8, DbColumnType_Float4, DbColumnType_Float8, DbColumnType_Numeric, DbColumnType_Boolean, DbColumnType_Text, DbColumnType_Varchar, DbColumnType_Bpchar, DbColumnType_Timestamp, DbColumnType_Timestamptz, DbColumnType_Date, DbColumnType_Time, DbColumnType_Timetz, DbColumnType_Interval, DbColumnType_Bytea, DbColumnType_Uuid, DbColumnType_Xml, DbColumnType_Json, DbColumnType_Jsonb, DbColumnType_Jsonpath, DbColumnType_Inet, DbColumnType_Cidr, DbColumnType_Macaddr, DbColumnType_Bit, DbColumnType_Varbit, DbColumnType_Int4range, DbColumnType_Int8range, DbColumnType_Numrange, DbColumnType_Tsrange, DbColumnType_Tstzrange, DbColumnType_Daterange, DbColumnType_Money, DbColumnType_Oid, DbColumnType_Enumeration, DbColumnType_Composite, DbColumnType_Domain, DbColumnType_Array, DbColumnType_Range]


class LazyDbColumnType:
    
    def __init__(self, value: DbColumnType) -> None:
        raise NotImplementedError

    def get(self) -> DbColumnType:
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
class DbColumn:
    ordinal: int
    name: str
    db_type: DbColumnType
    db_type_name: str

@dataclass
class DbRow:
    """
    A single row of values
    """
    values: List[DbValue]

@dataclass
class DbResult:
    columns: List[DbColumn]
    rows: List[DbRow]

class DbResultStream:
    """
    A potentially very large and lazy stream of rows:
    """
    
    def get_columns(self) -> List[DbColumn]:
        raise NotImplementedError
    def get_next(self) -> Optional[List[DbRow]]:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError


class DbTransaction:
    
    def query(self, statement: str, params: List[DbValue]) -> DbResult:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def query_stream(self, statement: str, params: List[DbValue]) -> DbResultStream:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def execute(self, statement: str, params: List[DbValue]) -> int:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def commit(self) -> None:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def rollback(self) -> None:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
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


class DbConnection:
    
    @classmethod
    def open(cls, address: str) -> Self:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def query(self, statement: str, params: List[DbValue]) -> DbResult:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def query_stream(self, statement: str, params: List[DbValue]) -> DbResultStream:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def execute(self, statement: str, params: List[DbValue]) -> int:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
        """
        raise NotImplementedError
    def begin_transaction(self) -> DbTransaction:
        """
        Raises: `bindings.types.Err(bindings.imports.postgres.Error)`
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



