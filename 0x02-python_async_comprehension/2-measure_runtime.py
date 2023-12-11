#!/usr/bin/env python3
"""
2-measure_runtime.py - Provides a method for
 measuring the run time for concurrent async comprehensions
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the run time for concurrently running
     async comprehensions

    Returns: The run time in seconds
    """

    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed: float = time.perf_counter() - start
    return elapsed
