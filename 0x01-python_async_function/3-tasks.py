#!/usr/bin/env python3
"""
3-tasks.py - Provides a method that creates a
 Task for delaying for a random amount of time
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a Task for scheduling a delay for a random number
     of seconds between 0 and the provided maximum delay period

    max_delay (int): The maximum delay time allowed (inclusive)

    Returns: the task
    """

    return asyncio.create_task(wait_random(max_delay))
