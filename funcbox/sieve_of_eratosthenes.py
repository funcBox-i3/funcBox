import bisect
import math
from itertools import compress


def primes(start: int = 2, limit: int | None = None) -> list[int]:
    """Efficiently generate all prime numbers between start and limit using the Sieve of Eratosthenes algorithm.

    Args:
        start (int): The lower bound for finding prime numbers (inclusive). Defaults to 2.
        limit (int): The upper bound for finding prime numbers (inclusive)

    Returns:
        List[int]: A list of all prime numbers from start to the given limit

    Raises:
        ValueError: If limit is less than 2 or start is less than 2

    Examples:
        >>> primes(2, 10)
        [2, 3, 5, 7]
        >>> primes(10, 20)
        [11, 13, 17, 19]

    """
    if limit is None:
        msg = "Limit must be provided"
        raise ValueError(msg)
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
