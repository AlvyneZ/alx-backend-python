#!/usr/bin/env python3
"""
8-make_multiplier.py - Provides a method for creating a
 function for multiplying against a certain value
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function for multiplying a float with a
     given float multiplier

    multiplier(float): the float the retun function will
     multiply its arguments to

    Returns: the function
    """
    return lambda n: n * multiplier
