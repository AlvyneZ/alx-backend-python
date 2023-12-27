#!/usr/bin/env python3
"""
9-element_length.py - Provides a method for getting the
 lengths of elements of sequences in an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Gets the lengths of elements of sequences
     in an iterable object

    lst(Iterable[Sequence]): an iterable for an object of
     sequences whose element count is needed

    Returns: a list of tuples of the sequences in the original
     iterable and their element counts
    """
    return [(i, len(i)) for i in lst]
