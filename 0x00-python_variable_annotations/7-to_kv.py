#!/usr/bin/env python3
""" 
    This are the Complex types - str & int/float to tuple 
"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        It will take a string k & an int OR float v as args
        And return a tuple.
    """

    return (k, v**2)