#!/usr/bin/env python3
from typing import List

"""
This module contains a function that sums a list of floats.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
