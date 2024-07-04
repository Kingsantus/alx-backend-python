#!/usr/bin/env python3
"""
Compute the square of an int/float
"""
from typing import List, Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Compute the square of v."""
    return k, v ** 2
