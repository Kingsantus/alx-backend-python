#!/usr/bin/env python3
"""
Measure the time needed to run async_comprehension() 4 times.
"""
import asyncio
import time

async_comprehension = \
    __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the time taken to run async_comprehension() four times."""
    t0 = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return time.perf_counter() - t0
