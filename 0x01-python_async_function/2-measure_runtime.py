#!/usr/bin/env python3
'''
Description: Import wait_random from the previous python file and define an
             async routine called wait_n. This routine takes two int arguments:
             max_delay and n. It spawns wait_random n times with the specified
             max_delay.

             wait_n returns a list of delays (float values) in ascending order,
             without using sort() due to concurrency.
    Author: Tinotenda
    Arguments: n: int, max_delay: int = 10
'''

import asyncio
from typing import List
from asyncio import create_task

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for random delays up to max_delay, returns a list of delays."""
    spawn_list = []
    delay_list = []

    for _ in range(n):
        delayed_task = create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
