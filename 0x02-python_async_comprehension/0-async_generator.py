#!/usr/bin/env python3
"""
0-async_generator.py - Provides a coroutine for
 generating 10 random numbers one at a time, each
 after a 1 second delay
"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """
    Generates a random number between 0 and 10 every second
     for 10 seconds

    Yields: A random number between 0 and 10

    Returns: none
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
