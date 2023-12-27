#!/usr/bin/env python3
"""
101-safely_get_value.py - Provides a method for
 retrieving a value from a dictionary
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
DefType = Union[T, None]
RetType = Union[Any, T]


def safely_get_value(
        dct: Mapping, key: Any, default: DefType = None
        ) -> RetType:
    '''
    Retrieves the first element of a sequence if it exists

    lst(Sequence): the sequence

    Returns: first element or None
    '''
    if key in dct:
        return dct[key]
    else:
        return default
