#!/usr/bin/env python3
"""this script has n times delays on each call"""

import asyncio
from typing import List
task_wait_random = __import__("task_wait_random").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Parameters:
    n (int): The number of times to spawn task_wait_random.
    max_delay (int): The maximum delay in seconds for task_wait_random.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Manual sort
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
