#!/usr/bin/env python3
"""This script contains a max delay call"""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


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
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter() - start_time

    elapsed = perf_counter() - start_time
    return elapsed / n
