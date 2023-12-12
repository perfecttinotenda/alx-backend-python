#!/usr/bin/env python3
''' 
Description: An asynchronous coroutine named async_generator that yields random 
      numbers between 0 & 10. It runs for 10 iterations with a 1-second 
      delay between each. Uses asyncio for asynchronous operations & the 
      random module for num generation.
'''

from asyncio import sleep
from random import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    ''' 
    Generator that yields rand val between 0 & 10 every second, 
    running for 10 iterations.
    '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()
