#!/usr/bin/env python3
"""
1-async_comprehension.py - Provides a coroutine for
 collecting 10 randomly generated numbers
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects randomly generated numbers into a list

    Returns: A list of the generated numbers
    """

    return [num async for num in async_generator()]
