from __future__ import annotations

from collections.abc import Sequence
from typing import Any

__all__ = ["binary_search"]


def binary_search(arr: Sequence, target: Any) -> int:
    """Search for a target value in a sorted sequence.

    Args:
        arr: Sorted sequence to search.
        target: Value to locate.

    Returns:
        Index of ``target`` if found, else ``-1``.

    Raises:
        TypeError: If ``arr`` is not a sequence.

    Examples:
        >>> binary_search([1, 3, 5, 7, 9], 7)
        3
        >>> binary_search([1, 3, 5, 7, 9], 4)
        -1

    """
    if not isinstance(arr, Sequence):
        msg = "arr must be a Sequence (e.g. list, tuple, range)"
        raise TypeError(msg)

    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
