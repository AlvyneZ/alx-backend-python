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
    Retrieves a value from a dictionary

    dct(Mapping): the dictionary to be searched through
    key(Any): the key of the element to be retrieved
    default(Any or None): return value if key is absent

    Returns: the element or default
    '''
    if key in dct:
        return dct[key]
    else:
        return default
