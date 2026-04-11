from __future__ import annotations

__all__ = ["fibonacci"]


def fibonacci(n: int, output_type: str = "int") -> int | list[int]:
    """Compute Fibonacci values.

    Args:
        n: Index of the term to return (for ``"int"``) or number of terms
            to generate (for ``"list"``).
        output_type: ``"int"`` to return a single term, ``"list"`` to return
            the sequence prefix.

    Returns:
        The nth Fibonacci number or a list of Fibonacci numbers.

    Raises:
        TypeError: If ``n`` is not an integer or ``output_type`` is not a string.
        ValueError: If ``n`` is negative or ``output_type`` is invalid.

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
        if n < 100:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
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
        if n == 2:
            return [0, 1]
        fib_list: list[int] = [0] * n
        fib_list[1] = 1
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
            fib_list[i] = b
        return fib_list
    msg = "output_type must be 'int' or 'list'"
    raise ValueError(msg)
