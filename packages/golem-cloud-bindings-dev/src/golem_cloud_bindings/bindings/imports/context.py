"""
Invocation context support
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import wall_clock


@dataclass
class AttributeValue_String:
    value: str


AttributeValue = Union[AttributeValue_String]
"""
Possible span attribute value types
"""


@dataclass
class Attribute:
    """
    An attribute of a span
    """
    key: str
    value: AttributeValue

class Span:
    """
    Represents a unit of work or operation
    """
    
    def started_at(self) -> wall_clock.Datetime:
        """
        Gets the starting time of the span
        """
        raise NotImplementedError
    def set_attribute(self, name: str, value: AttributeValue) -> None:
        """
        Set an attribute on the span
        """
        raise NotImplementedError
    def set_attributes(self, attributes: List[Attribute]) -> None:
        """
        Set multiple attributes on the span
        """
        raise NotImplementedError
    def finish(self) -> None:
        """
        Early finishes the span; otherwise it will be finished when the resource is dropped
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


@dataclass
class AttributeChain:
    """
    A chain of attribute values, the first element representing the most recent value
    """
    key: str
    values: List[AttributeValue]

class InvocationContext:
    """
    Represents an invocation context wich allows querying the stack of attributes
    created by automatic and user-defined spans.
    """
    
    def trace_id(self) -> str:
        """
        Gets the current trace id
        """
        raise NotImplementedError
    def span_id(self) -> str:
        """
        Gets the current span id
        """
        raise NotImplementedError
    def parent(self) -> Optional[Self]:
        """
        Gets the parent context, if any; allows recursive processing of the invocation context.
        
        Alternatively, the attribute query methods can return inherited values without having to
        traverse the stack manually.
        """
        raise NotImplementedError
    def get_attribute(self, key: str, inherited: bool) -> Optional[AttributeValue]:
        """
        Gets the value of an attribute `key`. If `inherited` is true, the value is searched in the stack of spans,
        otherwise only in the current span.
        """
        raise NotImplementedError
    def get_attributes(self, inherited: bool) -> List[Attribute]:
        """
        Gets all attributes of the current invocation context. If `inherited` is true, it returns the merged set of attributes, each
        key associated with the latest value found in the stack of spans.
        """
        raise NotImplementedError
    def get_attribute_chain(self, key: str) -> List[AttributeValue]:
        """
        Gets the chain of attribute values associated with the given `key`. If the key does not exist in any of the
        spans in the invocation context, the list is empty. The chain's first element contains the most recent (innermost) value.
        """
        raise NotImplementedError
    def get_attribute_chains(self) -> List[AttributeChain]:
        """
        Gets all values of all attributes of the current invocation context.
        """
        raise NotImplementedError
    def trace_context_headers(self) -> List[Tuple[str, str]]:
        """
        Gets the W3C Trace Context headers associated with the current invocation context
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



def start_span(name: str) -> Span:
    """
    Starts a new `span` with the given name, as a child of the current invocation context
    """
    raise NotImplementedError

def current_context() -> InvocationContext:
    """
    Gets the current invocation context
    
    The function call captures the current context; if new spans are started, the returned `invocation-context` instance will not
    reflect that.
    """
    raise NotImplementedError

def allow_forwarding_trace_context_headers(allow: bool) -> bool:
    """
    Allows or disallows forwarding of trace context headers in outgoing HTTP requests
    
    Returns the previous value of the setting
    """
    raise NotImplementedError

