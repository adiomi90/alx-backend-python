#!/usr/bin/env python3
"""This script waits for a random n time delay"""

import asyncio
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
