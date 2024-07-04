#!/usr/bin/env python3
"""
Defines a function that returns a function that multiplies
its argument with a certain value.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a func that multiplies its argument by the given float."""
    def callable_multiplied(x: float) -> float:
        """Multiply `x` by `multiplier`"""
        return x * multiplier
    return callable_multiplied
