"""
a Container is a collection of objects
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import wasi_blobstore_types

class StreamObjectNames:
    """
    this defines the `stream-object-names` resource which is a representation of stream<object-name>
    """
    
    def read_stream_object_names(self, len: int) -> Tuple[List[str], bool]:
        """
        reads the next number of objects from the stream
        
        This function returns the list of objects read, and a boolean indicating if the end of the stream was reached.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def skip_stream_object_names(self, num: int) -> Tuple[int, bool]:
        """
        skip the next number of objects in the stream
        
        This function returns the number of objects skipped, and a boolean indicating if the end of the stream was reached.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
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


class Container:
    """
    this defines the `container` resource
    """
    
    def name(self) -> str:
        """
        returns container name
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def info(self) -> wasi_blobstore_types.ContainerMetadata:
        """
        returns container metadata
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def get_data(self, name: str, start: int, end: int) -> wasi_blobstore_types.IncomingValue:
        """
        retrieves an object or portion of an object, as a resource.
        Start and end offsets are inclusive.
        Once a data-blob resource has been created, the underlying bytes are held by the blobstore service for the lifetime
        of the data-blob resource, even if the object they came from is later deleted.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def write_data(self, name: str, data: wasi_blobstore_types.OutgoingValue) -> None:
        """
        creates or replaces an object with the data blob.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def list_objects(self) -> StreamObjectNames:
        """
        returns list of objects in the container. Order is undefined.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def delete_object(self, name: str) -> None:
        """
        deletes object.
        does not return error if object did not exist.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def delete_objects(self, names: List[str]) -> None:
        """
        deletes multiple objects in the container
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def has_object(self, name: str) -> bool:
        """
        returns true if the object exists in this container
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def object_info(self, name: str) -> wasi_blobstore_types.ObjectMetadata:
        """
        returns metadata for the object
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
        """
        raise NotImplementedError
    def clear(self) -> None:
        """
        removes all objects within the container, leaving the container empty.
        
        Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
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



