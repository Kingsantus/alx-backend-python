#!/usr/bin/env python3
"""
Define a function for determining the length of each sequence
in an iterable of sequences.
"""
from typing import Iterable, List, Tuple, Sequence
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Determine the length of each sequence in the iterable."""
    return [(i, len(i)) for i in lst]
