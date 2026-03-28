from collections.abc import Sequence
from typing import Any


def binary_search(arr: Sequence, target: Any) -> int:
    """Search for a target value in a sorted list.

    Args:
        arr (Sequence): A sorted sequence to search through (list, tuple, range, etc).
        target (Any): The value to search for.

    Returns:
        int: The index of the target if found, -1 otherwise.

    Raises:
        TypeError: If arr is not a list.

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
