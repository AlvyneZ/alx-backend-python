#!/usr/bin/env python3
"""
100-safe_first_element.py - Provides a method for
 retrieving the first element of a Sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Retrieves the first element of a sequence if it exists

    lst(Sequence): the sequence

    Returns: first element or None
    '''
    if lst:
        return lst[0]
    else:
        return None
