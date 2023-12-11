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

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Rtn exe on time for a wait_n given `n` and `max_delay`. '''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n