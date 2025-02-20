#!/usr/bin/env python3
"""
Task: use mypy to validate the code in this module and apply the necessary
fixes.
"""
from typing import Tuple, List, Union

def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    """TODO: add docstring"""
    zoomed_in: List = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
