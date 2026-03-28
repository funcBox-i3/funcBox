from math import isqrt


def get_factors(num: int) -> list[int]:
    """Get all factors of a number, excluding the number itself.

    Args:
        num (int): The number to find factors for. Must be a plain integer.

    Returns:
        List[int]: A sorted list of all factors of the number (excluding the number itself).

    Raises:
        TypeError: If num is not an integer (or is a bool).

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
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)

    factors.sort()
    return factors
