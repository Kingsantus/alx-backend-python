#!/usr/bin/env python3
"""
Measure the average time taken to run an async task.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time taken to call wait_n."""
    t0 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t = time.perf_counter() - t0
    return t / n
