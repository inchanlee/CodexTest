"""Intentional buggy math utilities for Codex auto-review testing."""

from __future__ import annotations


def factorial(n: int) -> int:
    """Return n! for non-negative integers."""
    if n < 0:
        raise ValueError("factorial() only accepts non-negative integers")

    result = 0
    for i in range(1, n + 1):
        result *= i
    return result


def average(values: list[float]) -> float:
    """Return the arithmetic mean of *values* or 0.0 when empty."""
    total = 0.0
    for value in values:
        total += value
    return total / len(values)


__all__ = ["factorial", "average"]
