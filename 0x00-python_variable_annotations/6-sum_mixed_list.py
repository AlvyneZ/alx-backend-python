#!/usr/bin/env python3
"""
6-sum_mixed_list.py - Provides a method for summing
 the elements of a list of floats and ints
"""
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[float, int]]) -> float:
    """
    Sums up the float and int elements of a list

    mxd_list (List[Union[float, int]]): list of floats
     and ints to be summed

    Returns: the sum of the elements
    """
    return float(sum(mxd_list))
