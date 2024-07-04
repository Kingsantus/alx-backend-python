#!/usr/bin/env python3
"""
Define a function that returns types of the elements
"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element in lst."""
    if lst:
        return lst[0]
    else:
        return None
