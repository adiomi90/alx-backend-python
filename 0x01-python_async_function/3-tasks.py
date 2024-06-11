#!/usr/bin/env python3
"""this script has a task method"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine
    with the given max_delay.

    Parameters:
    max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    asyncio.Task: An asyncio.Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
