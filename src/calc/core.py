"""Tiny calculator library used as RepoPilot test material."""


def total(values):
    """Return the sum of all values, including negative ones (refunds)."""
    # Planted bug: negative values are skipped.
    return sum(v for v in values if v > 0)


def maximum(values):
    """Return the largest value, or None for an empty list."""
    if not values:
        return None
    return max(values)
