from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some


class LoadSnapshot(Protocol):

    @abstractmethod
    def load(self, bytes: bytes) -> None:
        """
        Tries to load a user-defined snapshot, setting up the worker's state based on it.
        The function can return with a failure to indicate that the update is not possible.
        
        Raises: `wit_world.types.Err(wit_world.imports.str)`
        """
        raise NotImplementedError


class OplogProcessor(Protocol):
    pass

class SaveSnapshot(Protocol):

    @abstractmethod
    def save(self) -> bytes:
        """
        Saves the component's state into a user-defined snapshot
        """
        raise NotImplementedError


