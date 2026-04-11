from __future__ import annotations

from collections import deque
from collections.abc import Iterable
from typing import Any

__all__ = ["flatten"]


def flatten(nested: Iterable[Any], depth: int | None = None) -> list[Any]:
    """Recursively flatten a nested iterable into a single list.

    Strings are treated as **atomic** — they are never iterated over
    character-by-character.

    Args:
        nested: The iterable to flatten.  May contain any mix of scalars
            and nested iterables.
        depth: Maximum nesting depth to flatten.  ``None`` (default)
            means flatten fully.  ``1`` flattens only the outermost level.

    Returns:
        A flat list of elements.

    Raises:
        TypeError: If *nested* is not iterable, or *depth* is not a
            positive integer (when provided).
        ValueError: If *depth* is not a positive integer (when provided).

    Examples:
        >>> flatten([1, [2, [3, [4]]]])
        [1, 2, 3, 4]
        >>> flatten([1, [2, [3]]], depth=1)
        [1, 2, [3]]
        >>> flatten([1, "ab", [2, "cd"]])
        [1, 'ab', 2, 'cd']
        >>> flatten([])
        []

    """
    if depth is not None:
        if not isinstance(depth, int) or isinstance(depth, bool):
            msg = f"depth must be an int, got {type(depth).__name__!r}"
            raise TypeError(msg)
        if depth < 1:
            msg = f"depth must be a positive integer, got {depth!r}"
            raise ValueError(msg)

    try:
        it = iter(nested)
    except TypeError:
        msg = f"nested must be iterable, got {type(nested).__name__!r}"
        raise TypeError(msg)

    result: list[Any] = []
    # Iterative DFS via an explicit stack of (iterator, current_depth) pairs.
    # deque provides faster pop operations and better memory management for stacks.
    stack = deque([(it, 0)])
    while stack:
        cur_it, cur_depth = stack[-1]
        try:
            item = next(cur_it)
        except StopIteration:
            stack.pop()
            continue

        # Fast path for atomic/non-iterable types to reduce type-checking overhead
        _t = type(item)
        if _t is list or _t is tuple or _t is set or _t is frozenset:
            if depth is None or cur_depth < depth:
                stack.append((iter(item), cur_depth + 1))
            else:
                result.append(item)
        elif _t is str or _t is int or _t is float or _t is bool or _t is dict:
            result.append(item)
        elif isinstance(item, Iterable) and (depth is None or cur_depth < depth):
            try:
                stack.append((iter(item), cur_depth + 1))
            except TypeError:
                result.append(item)
        else:
            result.append(item)

    return result
