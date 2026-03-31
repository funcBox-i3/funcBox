from __future__ import annotations

import bisect
import math
from itertools import compress

__all__ = ["primes"]


def primes(start: int = 2, limit: int | None = None) -> list[int]:
    """Generate prime numbers in an inclusive range.

    Args:
        start: Inclusive lower bound. Defaults to ``2``.
        limit: Inclusive upper bound.

    Returns:
        Prime numbers between ``start`` and ``limit``.

    Raises:
        TypeError: If ``start`` or ``limit`` is not a plain integer.
        ValueError: If ``limit`` is missing or if bounds are invalid.

    Examples:
        >>> primes(2, 10)
        [2, 3, 5, 7]
        >>> primes(10, 20)
        [11, 13, 17, 19]

    """
    if limit is None:
        msg = "Limit must be provided"
        raise ValueError(msg)
    if isinstance(limit, bool) or not isinstance(limit, int):
        msg = f"limit must be an integer, got {type(limit).__name__!r}"
        raise TypeError(msg)
    if isinstance(start, bool) or not isinstance(start, int):
        msg = f"start must be an integer, got {type(start).__name__!r}"
        raise TypeError(msg)
    if limit < 2:
        msg = "Limit must be at least 2"
        raise ValueError(msg)
    if start < 2:
        msg = "Start must be at least 2"
        raise ValueError(msg)
    if start > limit:
        return []

    if limit < 3:
        all_primes = [2]
    else:
        size = (limit + 1) // 2
        sieve = bytearray(b"\x01" * size)
        sieve[0] = 0

        for i in range(1, math.isqrt(limit) // 2 + 1):
            if sieve[i]:
                step = 2 * i + 1
                start_idx = 2 * i * (i + 1)
                sieve[start_idx::step] = bytes((size - start_idx + step - 1) // step)

        all_primes = [2]
        all_primes.extend(compress(range(3, 2 * size, 2), sieve[1:]))

    if start <= 2:
        return all_primes
    return all_primes[bisect.bisect_left(all_primes, start) :]
