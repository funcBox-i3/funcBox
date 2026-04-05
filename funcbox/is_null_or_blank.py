from __future__ import annotations

from collections.abc import Sized

__all__ = ["is_null_or_blank"]


def is_null_or_blank(value: object) -> bool:
    r"""Return ``True`` if *value* is ``None``, a whitespace-only string,
    or an empty collection (``list``, ``dict``, ``tuple``, ``set``,
    ``frozenset``, ``bytes``, ``bytearray``, or any other :class:`Sized`).

    The fast-path for ``None`` and ``str`` is unchanged — ``str.isspace()``
    is a single C-level scan that never allocates a new string object.
    Collection emptiness is detected via :func:`len`, which is O(1) for all
    built-in types.

    Args:
        value: The value to check.  Any type is accepted.

    Returns:
        ``True`` if *value* is:

        * ``None``
        * An empty string (``""``) or a string of only whitespace characters.
        * Any empty :class:`~collections.abc.Sized` — i.e. anything that
          supports ``len()`` and returns ``0`` (``list``, ``dict``, ``tuple``,
          ``set``, ``frozenset``, ``bytes``, ``bytearray``, custom classes,
          …).

        ``False`` otherwise.

    Examples:
        >>> is_null_or_blank(None)
        True
        >>> is_null_or_blank("")
        True
        >>> is_null_or_blank("   ")
        True
        >>> is_null_or_blank("\t\n")
        True
        >>> is_null_or_blank("hello")
        False
        >>> is_null_or_blank("  hi  ")
        False
        >>> is_null_or_blank([])
        True
        >>> is_null_or_blank([1, 2])
        False
        >>> is_null_or_blank({})
        True

    """
    if value is None:
        return True
    if isinstance(value, str):
        return not value or value.isspace()
    if isinstance(value, Sized):
        return len(value) == 0
    return False