#!/usr/bin/env python3
""" These are the Complex types - list of the floats """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
        Will take a list input_list of floats as arg
        and return their sum as a float.
    """

    return sum(input_list)