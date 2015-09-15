"""Stub file for the 'thread' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import Any, List, Tuple, Dict, GenericType

LockType = ...  # type: lock
error = ...  # type: object

def _count() -> int: ...

def allocate() -> lock: ...

def allocate_lock() -> lock: ...

def exit() -> Any:
    raise SystemExit()

def exit_thread() -> Any:
    raise SystemExit()

def get_ident() -> int: ...

def interrupt_main() -> None: ...

def stack_size(*args, **kwargs) -> int:
    raise ValueError()

def start_new(*args, **kwargs) -> int:
    raise MemoryError()
    raise TypeError()

def start_new_thread(*args, **kwargs) -> int:
    raise MemoryError()
    raise TypeError()


class _local(object):
    pass

class _localdummy(object):
    pass

class lock(object):
    def __enter__(*args, **kwargs) -> bool: ...
    def __exit__(*args, **kwargs) -> None: ...
    def acquire(*args, **kwargs) -> bool: ...
    def acquire_lock(*args, **kwargs) -> bool: ...
    def locked() -> bool: ...
    def locked_lock() -> bool: ...
    def release() -> None: ...
    def release_lock() -> None: ...
