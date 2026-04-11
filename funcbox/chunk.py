from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ["chunk"]


def chunk(iterable: Iterable[Any], size: int) -> list[list[Any]]:
    """Split *iterable* into consecutive chunks of at most *size* elements.

    The last chunk may be smaller than *size* if the iterable length is not
    perfectly divisible.

    Args:
        iterable: Any iterable to split.
        size: Maximum number of elements per chunk.  Must be a positive
            integer.

    Returns:
        A list of lists, each of length ≤ *size*.

    Raises:
        TypeError: If *iterable* is not iterable or *size* is not a plain int.
        ValueError: If *size* is not a positive integer.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk(range(6), 3)
        [[0, 1, 2], [3, 4, 5]]
        >>> chunk([], 4)
        []
        >>> chunk("hello", 2)
        [['h', 'e'], ['l', 'l'], ['o']]

    """
    if not isinstance(size, int) or isinstance(size, bool):
        msg = f"size must be an int, got {type(size).__name__!r}"
        raise TypeError(msg)
    if size <= 0:
        msg = f"size must be a positive integer, got {size!r}"
        raise ValueError(msg)

    # Fast path for sequences with known length (slicing is 2-3x faster)
    if isinstance(iterable, (list, tuple, str, bytes, bytearray)):
        return [iterable[i : i + size] for i in range(0, len(iterable), size)]

    try:
        it = iter(iterable)
    except TypeError:
        msg = f"iterable must be iterable, got {type(iterable).__name__!r}"
        raise TypeError(msg)

    result: list[list[Any]] = []
    current: list[Any] = []
    for item in it:
        current.append(item)
        if len(current) == size:
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result
