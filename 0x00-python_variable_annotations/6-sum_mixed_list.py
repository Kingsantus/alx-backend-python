#!/usr/bin/env python3
"""
Define a function that sums a list of numbers.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of numbers."""
    return sum(mxd_lst)
