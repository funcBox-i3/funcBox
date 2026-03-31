from __future__ import annotations

from .is_prime import is_prime

__all__ = ["classify_numbers"]


def classify_numbers(numbers: list[int]) -> dict[str, list[int]]:
    """Classify integers as prime, composite, or neither.

    Args:
        numbers: Integers to classify.

    Returns:
        A dictionary with keys ``"primes"``, ``"composites"``, and
        ``"neither"``.

    Raises:
        TypeError: If ``numbers`` is not a list or contains non-integers.

    Examples:
        >>> classify_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        {'primes': [2, 3, 5, 7], 'composites': [4, 6, 8, 9], 'neither': [0, 1]}
        >>> classify_numbers([-5, 0, 1, 13, 15])
        {'primes': [13], 'composites': [15], 'neither': [-5, 0, 1]}

    """
    if not isinstance(numbers, list):
        msg = "numbers must be a list"
        raise TypeError(msg)
    for i, n in enumerate(numbers):
        if not isinstance(n, int) or isinstance(n, bool):
            msg = f"All elements must be integers; got {type(n).__name__!r} at index {i}"
            raise TypeError(msg)

    primes: list[int] = []
    composites: list[int] = []
    neither: list[int] = []
    for n in numbers:
        if n < 2:
            neither.append(n)
        elif is_prime(n):
            primes.append(n)
        else:
            composites.append(n)
    return {"primes": primes, "composites": composites, "neither": neither}
