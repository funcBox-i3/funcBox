from __future__ import annotations

from math import isqrt

__all__ = ["get_factors"]


def get_factors(num: int) -> list[int]:
    """Return proper factors of an integer.

    Args:
        num: Integer to factor.

    Returns:
        A sorted list of factors excluding the number itself.

    Raises:
        TypeError: If ``num`` is not a plain integer.

    Examples:
        >>> get_factors(12)
        [1, 2, 3, 4, 6]
        >>> get_factors(7)
        [1]

    """
    if isinstance(num, bool) or not isinstance(num, int):
        msg = f"num must be an integer, got {type(num).__name__!r}"
        raise TypeError(msg)
    if num <= 1:
        return []

    factors = [1]
    limit = isqrt(num)
    for i in range(2, limit + 1):
        if num % i == 0:
            factors.append(i)
            other = num // i
            if i != other:
                factors.append(other)

    factors.sort()
    return factors
