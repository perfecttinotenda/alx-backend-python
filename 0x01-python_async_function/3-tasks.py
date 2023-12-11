#!/usr/bin/env python3
'''
Description: Implement a measure_time function that calculates the average
             execution time for the wait_n(n, max_delay) asynchronous routine.
             The function takes two integers, n and max_delay, and returns the
             total execution time divided by n as a float.
Author: Tinotenda
Arguments: n: int, max_delay: int
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Calculate the average execution time for wait_n with given n and max_delay.'''
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    elapsed_time = end_time - start_time
    return elapsed_time / n