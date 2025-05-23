"""
A keyvalue interface that provides eventually consistent batch operations.

A batch operation is an operation that operates on multiple keys at once.

Batch operations are useful for reducing network round-trip time. For example,
if you want to get the values associated with 100 keys, you can either do 100 get
operations or you can do 1 batch get operation. The batch operation is
faster because it only needs to make 1 network call instead of 100.

A batch operation does not guarantee atomicity, meaning that if the batch
operation fails, some of the keys may have been modified and some may not.
Transactional operations are being worked on and will be added in the future to
provide atomicity.

Data consistency in a key value store refers to the gaurantee that once a
write operation completes, all subsequent read operations will return the
value that was written.

The level of consistency in batch operations is **eventual consistency**, the same
with the readwrite interface. This interface does not guarantee strong consistency,
meaning that if a write operation completes, subsequent read operations may not return
the value that was written.
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import wasi_keyvalue_types


def get_many(bucket: wasi_keyvalue_types.Bucket, keys: List[str]) -> List[Optional[wasi_keyvalue_types.IncomingValue]]:
    """
    Get the values associated with the keys in the bucket. It returns a list of
    incoming-value that can be consumed to get the value associated with the key.
    
    If any of the keys do not exist in the bucket, it returns a `none` value for
    that key in the list.
    
    Note that the key-value pairs are guaranteed to be returned in the same order
    
    MAY show an out-of-date value if there are concurrent writes to the bucket.
    
    If any other error occurs, it returns an `Err(error)`.
    
    Raises: `wit_world.types.Err(wit_world.imports.Any)`
    """
    raise NotImplementedError

def keys(bucket: wasi_keyvalue_types.Bucket) -> List[str]:
    """
    Get all the keys in the bucket. It returns a list of keys.
    
    Note that the keys are not guaranteed to be returned in any particular order.
    
    If the bucket is empty, it returns an empty list.
    
    MAY show an out-of-date list of keys if there are concurrent writes to the bucket.
    
    If any error occurs, it returns an `Err(error)`.
    
    Raises: `wit_world.types.Err(wit_world.imports.Any)`
    """
    raise NotImplementedError

def set_many(bucket: wasi_keyvalue_types.Bucket, key_values: List[Tuple[str, wasi_keyvalue_types.OutgoingValue]]) -> None:
    """
    Set the values associated with the keys in the bucket. If the key already
    exists in the bucket, it overwrites the value.
    
    Note that the key-value pairs are not guaranteed to be set in the order
    they are provided.
    
    If any of the keys do not exist in the bucket, it creates a new key-value pair.
    
    If any other error occurs, it returns an `Err(error)`. When an error occurs, it
    does not rollback the key-value pairs that were already set. Thus, this batch operation
    does not guarantee atomicity, implying that some key-value pairs could be
    set while others might fail.
    
    Other concurrent operations may also be able to see the partial results.
    
    Raises: `wit_world.types.Err(wit_world.imports.Any)`
    """
    raise NotImplementedError

def delete_many(bucket: wasi_keyvalue_types.Bucket, keys: List[str]) -> None:
    """
    Delete the key-value pairs associated with the keys in the bucket.
    
    Note that the key-value pairs are not guaranteed to be deleted in the order
    they are provided.
    
    If any of the keys do not exist in the bucket, it skips the key.
    
    If any other error occurs, it returns an `Err(error)`. When an error occurs, it
    does not rollback the key-value pairs that were already deleted. Thus, this batch operation
    does not guarantee atomicity, implying that some key-value pairs could be
    deleted while others might fail.
    
    Other concurrent operations may also be able to see the partial results.
    
    Raises: `wit_world.types.Err(wit_world.imports.Any)`
    """
    raise NotImplementedError

