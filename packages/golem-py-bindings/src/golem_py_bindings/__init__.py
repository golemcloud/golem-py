import sys
import importlib

"""
Registers the bindiings that should be used by golem_py. Make sure this is called before any other golem_py import.
"""


def register_bindings(world_name: str) -> None:
    # componentize-py generates bindings under a world name. Import them here and make them available under a well known name.
    sys.modules["golem_py_bindings.bindings.exports"] = importlib.import_module(
        ".exports", world_name
    )
    sys.modules["golem_py_bindings.bindings.exports.run"] = importlib.import_module(
        ".exports.run", world_name
    )

    sys.modules["golem_py_bindings.bindings.imports"] = importlib.import_module(
        ".imports", world_name
    )
    sys.modules["golem_py_bindings.bindings.imports.error"] = importlib.import_module(
        ".imports.error", world_name
    )
    sys.modules["golem_py_bindings.bindings.imports.monotonic_clock"] = (
        importlib.import_module(".imports.monotonic_clock", world_name)
    )
    sys.modules["golem_py_bindings.bindings.imports.outgoing_handler"] = (
        importlib.import_module(".imports.outgoing_handler", world_name)
    )
    sys.modules["golem_py_bindings.bindings.imports.poll"] = importlib.import_module(
        ".imports.poll", world_name
    )
    sys.modules["golem_py_bindings.bindings.imports.streams"] = importlib.import_module(
        ".imports.streams", world_name
    )
    sys.modules["golem_py_bindings.bindings.imports.types"] = importlib.import_module(
        ".imports.types", world_name
    )

    sys.modules["golem_py_bindings.bindings.types"] = importlib.import_module(
        ".types", world_name
    )
