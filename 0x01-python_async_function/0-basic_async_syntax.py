#!/usr/bin/env python3
"""
Define an async function that sleeps after a random time interval.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random delay between 0 and max_delay."""
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
