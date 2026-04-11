from __future__ import annotations

_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
_SMALL_PRIMES_SET = frozenset(_SMALL_PRIMES)

__all__ = ["is_prime"]


def is_prime(n: int) -> bool:
    """Check whether an integer is prime.

    Args:
        n: Integer to test.

    Returns:
        ``True`` when prime, else ``False``.

    Raises:
        TypeError: If ``n`` is not a plain integer.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False

    """
    if isinstance(n, bool) or not isinstance(n, int):
        msg = f"n must be an integer, got {type(n).__name__!r}"
        raise TypeError(msg)
    if n < 2:
        return False
    if n < 1000000:
        if n in {2, 3}:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(n**0.5)
        return all(not (n % i == 0 or n % (i + 2) == 0) for i in range(5, limit + 1, 6))
    if n in _SMALL_PRIMES_SET:
        return True
    if any(n % p == 0 for p in _SMALL_PRIMES):
        return False

    r, d = 0, n - 1
    while not d & 1:
        r += 1
        d >>= 1

    for a in _SMALL_PRIMES:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
