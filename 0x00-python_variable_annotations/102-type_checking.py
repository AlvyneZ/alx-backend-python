#!/usr/bin/env python3
"""
102-type_checking.py - Provides a method for
 repeating tuple elements in a list
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Repeats tuple elements and places them in a list

    lst(Tuple): tuple of elements to be repeated
    factor(int): number of times to repeat the elements

    Returns: the list of repeated elements
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
