"""
A generic keyvalue interface for WASI.
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import streams

class Bucket:
    """
    A bucket is a collection of key-value pairs. Each key-value pair is stored
    as a entry in the bucket, and the bucket itself acts as a collection of all
    these entries.
    
    It is worth noting that the exact terminology for bucket in key-value stores
    can very depending on the specific implementation. For example,
    1. Amazon DynamoDB calls a collection of key-value pairs a table
    2. Redis has hashes, sets, and sorted sets as different types of collections
    3. Cassandra calls a collection of key-value pairs a column family
    4. MongoDB calls a collection of key-value pairs a collection
    5. Riak calls a collection of key-value pairs a bucket
    6. Memcached calls a collection of key-value pairs a slab
    7. Azure Cosmos DB calls a collection of key-value pairs a container
    
    In this interface, we use the term `bucket` to refer to a collection of key-value
    Soon: switch to `resource bucket { ... }`
    """
    
    @classmethod
    def open_bucket(cls, name: str) -> Self:
        """
        Opens a bucket with the given name.
        
        If any error occurs, including if the bucket does not exist, it returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
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


class OutgoingValue:
    """
    A value is the data stored in a key-value pair. The value can be of any type
    that can be represented in a byte array. It provides a way to write the value
    to the output-stream defined in the `wasi-io` interface.
    Soon: switch to `resource value { ... }`
    """
    
    @classmethod
    def new_outgoing_value(cls) -> Self:
        raise NotImplementedError
    def outgoing_value_write_body_async(self) -> streams.OutputStream:
        """
        Writes the value to the output-stream asynchronously.
        If any other error occurs, it returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
        """
        raise NotImplementedError
    def outgoing_value_write_body_sync(self, value: bytes) -> None:
        """
        Writes the value to the output-stream synchronously.
        If any other error occurs, it returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
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
    from the `input-stream` defined in the `wasi-io` interface.
    
    The incoming-value provides two ways to consume the value:
    1. `incoming-value-consume-sync` consumes the value synchronously and returns the
       value as a `list<u8>`.
    2. `incoming-value-consume-async` consumes the value asynchronously and returns the
       value as an `input-stream`.
    In addition, it provides a `incoming-value-size` function to get the size of the value.
    This is useful when the value is large and the caller wants to allocate a buffer of
    the right size to consume the value.
    Soon: switch to `resource incoming-value { ... }`
    """
    
    def incoming_value_consume_sync(self) -> bytes:
        """
        Consumes the value synchronously and returns the value as a list of bytes.
        If any other error occurs, it returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
        """
        raise NotImplementedError
    def incoming_value_consume_async(self) -> streams.InputStream:
        """
        Consumes the value asynchronously and returns the value as an `input-stream`.
        If any other error occurs, it returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
        """
        raise NotImplementedError
    def incoming_value_size(self) -> int:
        """
        The size of the value in bytes.
        If the size is unknown or unavailable, this function returns an `Err(error)`.
        
        Raises: `wit_world.types.Err(wit_world.imports.Any)`
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



