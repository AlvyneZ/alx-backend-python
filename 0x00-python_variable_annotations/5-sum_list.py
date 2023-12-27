#!/usr/bin/env python3
"""
5-sum_list.py - Provides a method for summing
 the elements of a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up the float elements of a list

    input_list (List[float]): list of floats to be summed

    Returns: the sum of the floats
    """
    return float(sum(input_list))
