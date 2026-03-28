from .is_prime import is_prime


def classify_numbers(numbers: list[int]) -> dict[str, list[int]]:
    """Separate a list of integers into primes, composites, and neither (0, 1, negatives).

    Args:
        numbers (list[int]): A list of integers to classify.

    Returns:
        dict[str, list[int]]: A dictionary with three keys:
            - 'primes': numbers that are prime
            - 'composites': numbers that are composite (> 1 and not prime)
            - 'neither': numbers that are neither prime nor composite (< 2)

    Raises:
        TypeError: If numbers is not a list, or any element is not an integer.

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

    primes, composites, neither = [], [], []
    for n in numbers:
        if n < 2:
            neither.append(n)
        elif is_prime(n):
            primes.append(n)
        else:
            composites.append(n)
    return {"primes": primes, "composites": composites, "neither": neither}
