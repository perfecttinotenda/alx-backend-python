#!/usr/bin/env python3

""" Thi is our mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  It will return a sum as a float. """
    return float(sum(mxd_lst))