"""
Types used by blobstore
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import streams

@dataclass
class ContainerMetadata:
    """
    information about a container
    """
    name: str
    created_at: int

@dataclass
class ObjectMetadata:
    """
    information about an object
    """
    name: str
    container: str
    created_at: int
    size: int

@dataclass
class ObjectId:
    """
    identifier for an object that includes its container name
    """
    container: str
    object: str

class OutgoingValue:
    """
    A data is the data stored in a data blob. The value can be of any type
    that can be represented in a byte array. It provides a way to write the value
    to the output-stream defined in the `wasi-io` interface.
    Soon: switch to `resource value { ... }`
    """
    
    @classmethod
    def new_outgoing_value(cls) -> Self:
        raise NotImplementedError
    def outgoing_value_write_body(self) -> streams.OutputStream:
        """
        Raises: `placeholder_world.types.Err(None)`
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


class IncomingValue:
    """
    A incoming-value is a wrapper around a value. It provides a way to read the value
    from the input-stream defined in the `wasi-io` interface.
    
    The incoming-value provides two ways to consume the value:
    1. `incoming-value-consume-sync` consumes the value synchronously and returns the
    value as a list of bytes.
    2. `incoming-value-consume-async` consumes the value asynchronously and returns the
    value as an input-stream.
    Soon: switch to `resource incoming-value { ... }`
    """
    
    def incoming_value_consume_sync(self) -> bytes:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def incoming_value_consume_async(self) -> streams.InputStream:
        """
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def size(self) -> int:
        raise NotImplementedError
    def __enter__(self) -> Self:
        """Returns self"""
        return self
                                
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        """
        Release this resource.
        """
        raise NotImplementedError



