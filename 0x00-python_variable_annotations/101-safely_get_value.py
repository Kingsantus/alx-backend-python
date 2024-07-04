#!/usr/bin/env python3
"""
Retrieve a value from a dict using its key.
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Get a value from a dict."""
    if key in dct:
        return dct[key]
    else:
        return default
