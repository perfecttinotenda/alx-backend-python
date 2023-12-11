#!/usr/bin/env python3
""" Introduction to asynchronous programming 
    Author: Tinotenda
"""


from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime for concurrent coroutines """
    start_time = time()

    run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n