#!/usr/bin/env python3
"""
7-to_kv.py - Provides a method for creating a
 tuple of a string and number (int or float)
"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    Creates a tuple of a string and square of number

    k(str): String for tuple first element
    v(int or float): Number to be squared

    Returns: the created tuple
    """
    return (k, float(v ** 2))
