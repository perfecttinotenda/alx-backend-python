#!/usr/bin/env python3
'''
Description: Implement a measure_time function that calculates the average
             execution time for the wait_n(n, max_delay) asynchronous routine.
             The function takes two integers, n and max_delay, and returns the
             total execution time divided by n as a float.
Author: Tinotenda
Arguments: n: int, max_delay: int
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    '''Rtrns an async.task obj.'''
    return asyncio.create_task(wait_random(max_delay))