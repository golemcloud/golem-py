from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import host
from ..imports import golem_rpc_types
from ..imports import oplog

@dataclass
class AccountInfo:
    account_id: host.AccountId

class Processor(Protocol):
    """
    A processor resource is instantiated for each account having activated this oplog processor plugin.
    There are no guarantees for the number of processors running at the same time, and different entries from the same worker
    may be sent to different processor instances.
    """
    
    @abstractmethod
    def __init__(self, account_info: AccountInfo, component_id: golem_rpc_types.ComponentId, config: List[Tuple[str, str]]) -> None:
        """
        Initializes an oplog processor for a given component where the plugin was installed to.
        The `account-info` parameters contains details of the account the installation belongs to.
        The `component-id` parameter contains the identifier of the component the plugin was installed to.
        The `config` parameter contains the configuration parameters for the plugin, as specified in the plugin installation
        for the component.
        """
        raise NotImplementedError

    @abstractmethod
    def process(self, worker_id: golem_rpc_types.WorkerId, metadata: host.WorkerMetadata, first_entry_index: int, entries: List[oplog.OplogEntry]) -> None:
        """
        Called when one of the workers the plugin is activated on has written new entries to its oplog.
        The `worker-id` parameter identifies the worker.
        The `metadata` parameter contains the latest metadata of the worker.
        The `first-entry-index` parameter contains the index of the first entry in the list of `entries`.
        The `entries` parameteter always contains at least one element.
        
        Raises: `bindings.types.Err(bindings.exports.str)`
        """
        raise NotImplementedError


