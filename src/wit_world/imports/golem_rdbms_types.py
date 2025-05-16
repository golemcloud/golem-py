from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some


@dataclass
class Uuid:
    high_bits: int
    low_bits: int


@dataclass
class IpAddress_Ipv4:
    value: Tuple[int, int, int, int]


@dataclass
class IpAddress_Ipv6:
    value: Tuple[int, int, int, int, int, int, int, int]


IpAddress = Union[IpAddress_Ipv4, IpAddress_Ipv6]


@dataclass
class MacAddress:
    octets: Tuple[int, int, int, int, int, int]

@dataclass
class Date:
    year: int
    month: int
    day: int

@dataclass
class Time:
    hour: int
    minute: int
    second: int
    nanosecond: int

@dataclass
class Timestamp:
    date: Date
    time: Time

@dataclass
class Timestamptz:
    timestamp: Timestamp
    offset: int

@dataclass
class Timetz:
    time: Time
    offset: int


