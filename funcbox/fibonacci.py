def fibonacci(n: int, output_type: str = "int") -> int | list[int]:
    """Calculate Fibonacci numbers efficiently.

    Args:
        n (int): The index of Fibonacci number to calculate (0-indexed) or count of numbers for list.
        output_type (str, optional): Output format - 'int' for single value or 'list' for sequence. Defaults to "int".

    Returns:
        Union[int, List[int]]: Either the nth Fibonacci number or a list of n Fibonacci numbers.

    Raises:
        TypeError: If n is not an integer or output_type is not a string.
        ValueError: If n is negative or output_type is not 'int' or 'list'.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(5)
        5
        >>> fibonacci(5, "list")
        [0, 1, 1, 2, 3]

    """
    if isinstance(n, bool) or not isinstance(n, int):
        msg = f"n must be an integer, got {type(n).__name__!r}"
        raise TypeError(msg)
    if not isinstance(output_type, str):
        msg = f"output_type must be a string, got {type(output_type).__name__!r}"
        raise TypeError(msg)
    if n < 0:
        msg = "n must be non-negative"
        raise ValueError(msg)

    if output_type == "int":
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
    if output_type == "list":
        if n == 0:
            return []
        if n == 1:
            return [0]
        fib_list = [0] * n
        fib_list[1] = 1
        for i in range(2, n):
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        return fib_list
    msg = "Invalid output_type. Use 'int' or 'list'."
    raise ValueError(msg)
