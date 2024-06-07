#!/usr/bin/env python3
"""This script contains a multiply function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiplier_func(number: float) -> float:
        """_summary_

        Args:
            number (float): _description_

        Returns:
            float: _description_
        """
        return multiplier * number

    return multiplier_func
