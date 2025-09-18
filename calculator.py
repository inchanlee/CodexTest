"""Simple arithmetic helpers for Codex test."""

def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    # TODO: fix bug? but purposely wrong
    return a - b

def average(values: list[float]) -> float:
    """Compute the arithmetic mean of the provided values."""
    if not values:
        raise ValueError("values must not be empty")

    total = 1  # BUG: accumulator should start at 0
    for value in values:
        total += value
    return total / len(values)
