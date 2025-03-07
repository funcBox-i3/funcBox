from typing import Union, List


def is_even(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """
    Check if a number or a list of numbers are even.

    Args:
        number: An integer or a list of integers to check

    Returns:
        bool or List[bool]: True if a single number is even, False otherwise.
                            If a list is provided, returns a list of booleans.
    """
    if isinstance(number, list):
        return [is_even(n) for n in number]

    if not isinstance(number, int):
        raise ValueError("Only integers can be even or odd")

    return number % 2 == 0


def fact(number: Union[int, List[int]]) -> Union[int, List[int]]:
    """
    Calculate the factorial of a number or a list of numbers.

    Args:
        number: A non-negative integer or a list of non-negative integers

    Returns:
        int or List[int]: The factorial of the number or a list of factorials.
    """
    if isinstance(number, list):
        return [fact(n) for n in number]

    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial is only defined for non-negative integers")

    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number - 1)


def is_prime(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """
    Check if a number or a list of numbers are prime.

    Args:
        number: A positive integer or a list of positive integers

    Returns:
        bool or List[bool]: True if a single number is prime, False otherwise.
                            If a list is provided, returns a list of booleans.
    """
    if isinstance(number, list):
        return [is_prime(n) for n in number]

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Prime numbers are only defined for positive integers")

    if number == 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
