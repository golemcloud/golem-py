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
class DbColumnType_Boolean:
    pass


@dataclass
class DbColumnType_Tinyint:
    pass


@dataclass
class DbColumnType_Smallint:
    pass


@dataclass
class DbColumnType_Mediumint:
    pass


@dataclass
class DbColumnType_Int:
    pass


@dataclass
class DbColumnType_Bigint:
    pass


@dataclass
class DbColumnType_TinyintUnsigned:
    pass


@dataclass
class DbColumnType_SmallintUnsigned:
    pass


@dataclass
class DbColumnType_MediumintUnsigned:
    pass


@dataclass
class DbColumnType_IntUnsigned:
    pass


@dataclass
class DbColumnType_BigintUnsigned:
    pass


@dataclass
class DbColumnType_Float:
    pass


@dataclass
class DbColumnType_Double:
    pass


@dataclass
class DbColumnType_Decimal:
    pass


@dataclass
class DbColumnType_Date:
    pass


@dataclass
class DbColumnType_Datetime:
    pass


@dataclass
class DbColumnType_Timestamp:
    pass


@dataclass
class DbColumnType_Time:
    pass


@dataclass
class DbColumnType_Year:
    pass


@dataclass
class DbColumnType_Fixchar:
    pass


@dataclass
class DbColumnType_Varchar:
    pass


@dataclass
class DbColumnType_Tinytext:
    pass


@dataclass
class DbColumnType_Text:
    pass


@dataclass
class DbColumnType_Mediumtext:
    pass


@dataclass
class DbColumnType_Longtext:
    pass


@dataclass
class DbColumnType_Binary:
    pass


@dataclass
class DbColumnType_Varbinary:
    pass


@dataclass
class DbColumnType_Tinyblob:
    pass


@dataclass
class DbColumnType_Blob:
    pass


@dataclass
class DbColumnType_Mediumblob:
    pass


@dataclass
class DbColumnType_Longblob:
    pass


@dataclass
class DbColumnType_Enumeration:
    pass


@dataclass
class DbColumnType_Set:
    pass


@dataclass
class DbColumnType_Bit:
    pass


@dataclass
class DbColumnType_Json:
    pass


DbColumnType = Union[DbColumnType_Boolean, DbColumnType_Tinyint, DbColumnType_Smallint, DbColumnType_Mediumint, DbColumnType_Int, DbColumnType_Bigint, DbColumnType_TinyintUnsigned, DbColumnType_SmallintUnsigned, DbColumnType_MediumintUnsigned, DbColumnType_IntUnsigned, DbColumnType_BigintUnsigned, DbColumnType_Float, DbColumnType_Double, DbColumnType_Decimal, DbColumnType_Date, DbColumnType_Datetime, DbColumnType_Timestamp, DbColumnType_Time, DbColumnType_Year, DbColumnType_Fixchar, DbColumnType_Varchar, DbColumnType_Tinytext, DbColumnType_Text, DbColumnType_Mediumtext, DbColumnType_Longtext, DbColumnType_Binary, DbColumnType_Varbinary, DbColumnType_Tinyblob, DbColumnType_Blob, DbColumnType_Mediumblob, DbColumnType_Longblob, DbColumnType_Enumeration, DbColumnType_Set, DbColumnType_Bit, DbColumnType_Json]


@dataclass
class DbColumn:
    ordinal: int
    name: str
    db_type: DbColumnType
    db_type_name: str


@dataclass
class DbValue_Boolean:
    value: bool


@dataclass
class DbValue_Tinyint:
    value: int


@dataclass
class DbValue_Smallint:
    value: int


@dataclass
class DbValue_Mediumint:
    value: int


@dataclass
class DbValue_Int:
    value: int


@dataclass
class DbValue_Bigint:
    value: int


@dataclass
class DbValue_TinyintUnsigned:
    value: int


@dataclass
class DbValue_SmallintUnsigned:
    value: int


@dataclass
class DbValue_MediumintUnsigned:
    value: int


@dataclass
class DbValue_IntUnsigned:
    value: int


@dataclass
class DbValue_BigintUnsigned:
    value: int


@dataclass
class DbValue_Float:
    value: float


@dataclass
class DbValue_Double:
    value: float


@dataclass
class DbValue_Decimal:
    value: str


@dataclass
class DbValue_Date:
    value: golem_rdbms_types.Date


@dataclass
class DbValue_Datetime:
    value: golem_rdbms_types.Timestamp


@dataclass
class DbValue_Timestamp:
    value: golem_rdbms_types.Timestamp


@dataclass
class DbValue_Time:
    value: golem_rdbms_types.Time


@dataclass
class DbValue_Year:
    value: int


@dataclass
class DbValue_Fixchar:
    value: str


@dataclass
class DbValue_Varchar:
    value: str


@dataclass
class DbValue_Tinytext:
    value: str


@dataclass
class DbValue_Text:
    value: str


@dataclass
class DbValue_Mediumtext:
    value: str


@dataclass
class DbValue_Longtext:
    value: str


@dataclass
class DbValue_Binary:
    value: bytes


@dataclass
class DbValue_Varbinary:
    value: bytes


@dataclass
class DbValue_Tinyblob:
    value: bytes


@dataclass
class DbValue_Blob:
    value: bytes


@dataclass
class DbValue_Mediumblob:
    value: bytes


@dataclass
class DbValue_Longblob:
    value: bytes


@dataclass
class DbValue_Enumeration:
    value: str


@dataclass
class DbValue_Set:
    value: str


@dataclass
class DbValue_Bit:
    value: List[bool]


@dataclass
class DbValue_Json:
    value: str


@dataclass
class DbValue_Null:
    pass


DbValue = Union[DbValue_Boolean, DbValue_Tinyint, DbValue_Smallint, DbValue_Mediumint, DbValue_Int, DbValue_Bigint, DbValue_TinyintUnsigned, DbValue_SmallintUnsigned, DbValue_MediumintUnsigned, DbValue_IntUnsigned, DbValue_BigintUnsigned, DbValue_Float, DbValue_Double, DbValue_Decimal, DbValue_Date, DbValue_Datetime, DbValue_Timestamp, DbValue_Time, DbValue_Year, DbValue_Fixchar, DbValue_Varchar, DbValue_Tinytext, DbValue_Text, DbValue_Mediumtext, DbValue_Longtext, DbValue_Binary, DbValue_Varbinary, DbValue_Tinyblob, DbValue_Blob, DbValue_Mediumblob, DbValue_Longblob, DbValue_Enumeration, DbValue_Set, DbValue_Bit, DbValue_Json, DbValue_Null]
"""
Value descriptor for a single database value
"""


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
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def query_stream(self, statement: str, params: List[DbValue]) -> DbResultStream:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def execute(self, statement: str, params: List[DbValue]) -> int:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def commit(self) -> None:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def rollback(self) -> None:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
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
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def query(self, statement: str, params: List[DbValue]) -> DbResult:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def query_stream(self, statement: str, params: List[DbValue]) -> DbResultStream:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def execute(self, statement: str, params: List[DbValue]) -> int:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
        """
        raise NotImplementedError
    def begin_transaction(self) -> DbTransaction:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.mysql.Error)`
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



