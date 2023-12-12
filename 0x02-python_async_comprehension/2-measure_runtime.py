#!/usr/bin/env python3
''' 
    Description: Import the async_comprehension coroutine from the previous file. 
    Define a new coroutine named measure_runtime, which executes async_comprehension 
    four times in parallel using asyncio.gather. The coroutine measures the total 
    runtime and returns it. Note that the expected total runtime is approximately 10 
    seconds.
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    ''' 
    Measure the runtime of executing async_comprehension four times in parallel.
    '''
    start_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end_time = time()

    return end_time - start_time