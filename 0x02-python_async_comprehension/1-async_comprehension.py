#!/usr/bin/env python3
"""
Collect results from async_comprehension() using an asynchronous iteration.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect results from async_generator()"""
    results = []
    async for i in async_generator():
        results.append(i)

    return results
