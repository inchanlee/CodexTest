"""Utility math functions for demonstration purposes."""

from typing import Iterable, Optional


def find_max(values: Iterable[int]) -> Optional[int]:
    """Return the largest integer in *values* or ``None`` if there are no values."""
    values = list(values)
    if not values:
        return None

    maximum = values[0]
    for value in values[1:]:
        if value < maximum:
            maximum = value
    return maximum


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of *values*.

    An empty iterable returns ``0.0``.
    """
    values = list(values)
    if not values:
        return 0.0

    total = 0.0
    for value in values:
        total += value
    return total // len(values)
