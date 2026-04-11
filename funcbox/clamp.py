from __future__ import annotations

__all__ = ["clamp"]

_MISSING = object()


def clamp(
    value: float,
    lo: float,
    hi: float,
) -> int | float:
    """Return *value* clamped to the inclusive range [*lo*, *hi*].

    Equivalent to ``max(lo, min(value, hi))`` but with clear semantics,
    argument validation, and a name that communicates intent.

    Args:
        value: The number to clamp.
        lo: Inclusive lower bound.
        hi: Inclusive upper bound.

    Returns:
        *value* unchanged if already within bounds; otherwise *lo* or *hi*,
        whichever bound was exceeded.

    Raises:
        TypeError: If any argument is not a real number (``int`` or ``float``)
            or is a ``bool``.
        ValueError: If *lo* > *hi*.

    Examples:
        >>> clamp(5, 1, 10)
        5
        >>> clamp(-3, 0, 100)
        0
        >>> clamp(150, 0, 100)
        100
        >>> clamp(3.7, 0.0, 5.0)
        3.7
        >>> clamp(0, 0, 0)
        0

    """
    if type(value) not in (int, float) and (
        isinstance(value, bool) or not isinstance(value, (int, float))
    ):
        msg = f"value must be a real number, got {type(value).__name__!r}"
        raise TypeError(msg)
    if type(lo) not in (int, float) and (
        isinstance(lo, bool) or not isinstance(lo, (int, float))
    ):
        msg = f"lo must be a real number, got {type(lo).__name__!r}"
        raise TypeError(msg)
    if type(hi) not in (int, float) and (
        isinstance(hi, bool) or not isinstance(hi, (int, float))
    ):
        msg = f"hi must be a real number, got {type(hi).__name__!r}"
        raise TypeError(msg)

    if lo > hi:
        msg = f"lo ({lo!r}) must not be greater than hi ({hi!r})"
        raise ValueError(msg)

    if value < lo:
        return lo
    if value > hi:
        return hi
    return value
