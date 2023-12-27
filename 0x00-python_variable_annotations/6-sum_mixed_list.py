#!/usr/bin/env python3
"""
6-sum_mixed_list.py - Provides a method for summing
 the elements of a list of floats and ints
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sums up the float and int elements of a list

    mxd_list (List[Union[float, int]]): list of floats
     and ints to be summed

    Returns: the sum of the elements
    """
    return float(sum(mxd_list))
