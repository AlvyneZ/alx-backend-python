#!/usr/bin/python3
"""
0-basic_async_syntax.py - Provides a coroutine for
 delaying for a random amount of time
"""

import asyncio
from random import uniform


async def wait_random(max_delay: float = 10) -> float:
    """
    Delays for a random number of seconds between 0 and the
     provided maximum delay period

    max_delay (float): The maximum delay time allowed (inclusive)

    Returns: the delay that was implemented
    """

    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
