#!/usr/bin/env python3
"""
    Here we will duck type an iterable obj
"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        This will show element length
    """
    return [(i, len(i)) for i in lst]