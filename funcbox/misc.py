import math


def is_prime(n: int) -> bool:
    """Efficiently check if a number is prime. Only checking potential divisors of form 6k±1 up to sqrt(n).

    Args:
        n (int): The number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False

    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fibonacci(n: int, type="int") -> int | list[int]:
    """Calculate Fibonacci numbers efficiently.

    This function can either return the nth Fibonacci number or a list of the first n Fibonacci numbers,
    depending on the type parameter. The sequence starts with F(0)=0, F(1)=1.

    Args:
        n (int): The index of Fibonacci number to calculate (0-indexed) or count of numbers for list
        type (str, optional): Output format - 'int' for single value or 'list' for sequence. Defaults to "int".

    Returns:
        Union[int, List[int]]: Either the nth Fibonacci number or a list of n Fibonacci numbers

    Raises:
        ValueError: If n is negative or type is not 'int' or 'list'

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(5)
        5
        >>> fibonacci(5, "list")
        [0, 1, 1, 2, 3]

    """
    if n < 0:
        msg = "n must be non-negative"
        raise ValueError(msg)

    if type == "int":
        if n == 0:
            return 0
        a, b = 0, 1
        for bit in range(n.bit_length() - 1, -1, -1):
            c = a * (2 * b - a)
            d = a * a + b * b
            if (n >> bit) & 1:
                a, b = d, c + d
            else:
                a, b = c, d
        return a
    if type == "list":
        if n == 0:
            return []
        if n == 1:
            return [0]
        fib_list = [0] * n
        fib_list[1] = 1
        for i in range(2, n):
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        return fib_list
    msg = "Invalid type. Use 'int' or 'list'."
    raise ValueError(msg)


def get_factors(num: int) -> list[int]:
    """Get all factors of a number, excluding the number itself.

    This function efficiently finds all factors of a given number by only
    checking potential factors up to the square root of the number and then
    calculating their pairs.

    Args:
        num (int): The number to find factors for.

    Returns:
        List[int]: A sorted list of all factors of the number (excluding the number itself).

    Examples:
        >>> get_factors(12)
        [1, 2, 3, 4, 6]
        >>> get_factors(7)
        [1]

    """
    if num <= 1:
        return []

    factors = [1]
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)

    factors.sort()
    return factors
