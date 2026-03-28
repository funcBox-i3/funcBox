_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
_SMALL_PRIMES_SET = frozenset(_SMALL_PRIMES)


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check for primality. Must be a plain integer.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If n is not an integer (or is a bool).

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
