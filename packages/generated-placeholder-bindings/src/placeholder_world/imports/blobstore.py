"""
wasi-cloud Blobstore service definition
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import container
from ..imports import wasi_blobstore_types


def create_container(name: str) -> container.Container:
    """
    creates a new empty container
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

def get_container(name: str) -> container.Container:
    """
    retrieves a container by name
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

def delete_container(name: str) -> None:
    """
    deletes a container and all objects within it
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

def container_exists(name: str) -> bool:
    """
    returns true if the container exists
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

def copy_object(src: wasi_blobstore_types.ObjectId, dest: wasi_blobstore_types.ObjectId) -> None:
    """
    copies (duplicates) an object, to the same or a different container.
    returns an error if the target container does not exist.
    overwrites destination object if it already existed.
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

def move_object(src: wasi_blobstore_types.ObjectId, dest: wasi_blobstore_types.ObjectId) -> None:
    """
    moves or renames an object, to the same or a different container
    returns an error if the destination container does not exist.
    overwrites destination object if it already existed.
    
    Raises: `placeholder_world.types.Err(placeholder_world.imports.str)`
    """
    raise NotImplementedError

