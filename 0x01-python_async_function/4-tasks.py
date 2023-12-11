#!/usr/bin/env python3
'''
Description: Repurpose the code from wait_n into a new function task_wait_n.
             The primary distinction lies in the use of task_wait_random
             instead of wait_random.
Author: Tinotenda
Arguments: n: int, max_delay: int = 10
'''

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Exe task_wait_random & retrieve a sorted_list of delays.s.'''
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
