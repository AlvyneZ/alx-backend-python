#!/usr/bin/env python3
"""
4-tasks.py - Provides a coroutine for
 concurrently running multiple random delays using Tasks
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Concurrently runs n random delays each with a maximum delay
     of max_delay seconds using Tasks

    n (int): The number of concurrent random delays to spawn
    max_delay (int): The maximum delay time allowed (inclusive)

    Returns: a list of the delays that were implemented
    """

    wait_times: List[float] = []

    async def append_wait_random() -> None:
        """
        Implements a random wait and adds the wait time into a list

        Returns: none
        """
        wait_times.append(await task_wait_random(max_delay))

    await asyncio.gather(*(append_wait_random() for _ in range(n)))
    return wait_times
