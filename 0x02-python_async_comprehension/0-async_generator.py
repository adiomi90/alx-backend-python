#!/usr/bin/env python3
""" This code create async generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Yields:
        Generator[float, None, None]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
