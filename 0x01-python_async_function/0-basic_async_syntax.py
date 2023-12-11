#!/usr/bin/env python3
''' Description: Introduction to asynchronous programming in Python.   
    Author: Tinotenda
                asynchronous coroutine that takes in an integer arg
                 (max_delay, with a default value of 10) named wait_random
                 that waits for a random delay between 0 and max_delay
                 (included and float value) seconds and eventually returns it
    Args: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Delays execution for a random duration between 0 and max_delay (inclusive, float value),
    then returns the delay duration.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
