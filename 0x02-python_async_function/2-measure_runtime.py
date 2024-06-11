#!/usr/bin/env python3
"""This script contains a max delay call"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').await_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    float: The average time per call.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
