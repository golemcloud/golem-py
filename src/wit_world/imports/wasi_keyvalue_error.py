from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some


class Error:
    """
    An error resource type for keyvalue operations.
    
    Common errors:
    - Connectivity errors (e.g. network errors): when the client cannot establish
     a connection to the keyvalue service.
    - Authentication and Authorization errors: when the client fails to authenticate
     or does not have the required permissions to perform the operation.
    - Data errors: when the client sends incompatible or corrupted data.
    - Resource errors: when the system runs out of resources (e.g. memory).
    - Internal errors: unexpected errors on the server side.
    
    Currently, this provides only one function to return a string representation
    of the error. In the future, this will be extended to provide more information
    about the error.
    Soon: switch to `resource error { ... }`
    """
    
    def trace(self) -> str:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



