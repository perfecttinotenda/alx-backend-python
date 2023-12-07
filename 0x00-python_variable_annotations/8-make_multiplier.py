#!/usr/bin/env python3
""" This are our Complex types - funkshens"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        This will take a float multiplier as arg;
        And it will return a funkshen that multiplies a float by the multiplier.
    """
    def f(n: float) -> float:
        """ 
            This will multiply a float by the multiplier
        """
        return float(n * multiplier)

    return f