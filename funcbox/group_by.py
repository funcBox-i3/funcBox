from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ["group_by"]


def group_by(
    iterable: Iterable[Any],
    key: Any,
) -> dict[Any, list[Any]]:
    """Group elements of *iterable* by a key function or attribute name.

    Unlike :func:`itertools.groupby`, this function does **not** require the
    input to be sorted first — it collects all groups in a single pass and
    returns a plain ``dict`` where each key maps to a list of matching items.

    Args:
        iterable: Any iterable of items to group.
        key: One of:

            - A **callable** invoked on each item to produce the group key
              (e.g. ``lambda x: x["status"]``).
            - A **string** used as a dict-key (``item[key]``) or attribute
              name (``item.key``), tried in that order.

    Returns:
        A ``dict`` mapping each distinct key to a list of items that
        produced that key.  Insertion order of first-seen keys is preserved
        (Python 3.7+).

    Raises:
        TypeError: If *iterable* is not iterable or *key* is not a str or
            callable.

    Examples:
        >>> words = ["apple", "ant", "banana", "bear", "cherry"]
        >>> group_by(words, lambda w: w[0])
        {'a': ['apple', 'ant'], 'b': ['banana', 'bear'], 'c': ['cherry']}

        >>> people = [{"name": "Alice", "dept": "Eng"}, {"name": "Bob", "dept": "HR"},
        ...           {"name": "Carol", "dept": "Eng"}]
        >>> group_by(people, "dept")
        {'Eng': [{'name': 'Alice', 'dept': 'Eng'}, {'name': 'Carol', 'dept': 'Eng'}], 'HR': [{'name': 'Bob', 'dept': 'HR'}]}

        >>> group_by(range(10), lambda n: n % 3)
        {0: [0, 3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

    """
    if not callable(key) and not isinstance(key, str):
        msg = f"key must be a callable or a str, got {type(key).__name__!r}"
        raise TypeError(msg)

    try:
        it = iter(iterable)
    except TypeError:
        msg = f"iterable must be iterable, got {type(iterable).__name__!r}"
        raise TypeError(msg)

    result: dict[Any, list[Any]] = {}

    if callable(key):
        for item in it:
            k = key(item)
            try:
                result[k].append(item)
            except KeyError:
                result[k] = [item]
    else:
        # String key: try dict lookup first, then attribute access
        for item in it:
            try:
                k = item[key]
            except (KeyError, TypeError):
                try:
                    k = getattr(item, key)
                except AttributeError:
                    msg = f"item {item!r} has no key or attribute {key!r}"
                    raise KeyError(msg)
            try:
                result[k].append(item)
            except KeyError:
                result[k] = [item]

    return result
