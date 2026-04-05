from __future__ import annotations

__all__ = ["is_null_or_blank"]


def is_null_or_blank(value: object) -> bool:
    """Return ``True`` if *value* is ``None`` or a whitespace-only string.

    Mirrors the common ``isNullOrBlank`` / ``isNullOrWhiteSpace`` helper
    found in many other languages.  ``str.strip()`` is intentionally avoided
    in the hot-path: ``str.isspace()`` is a single C-level scan that never
    allocates a new string object, making it measurably faster on large
    inputs.

    Args:
        value: The value to check.  Any type is accepted; only ``None`` and
            ``str`` instances can return ``True``.

    Returns:
        ``True`` if *value* is ``None``, an empty string (``""``), or a
        string containing only whitespace characters.  ``False`` for every
        non-``None`` non-``str`` type and for strings with at least one
        non-whitespace character.

    Examples:
        >>> is_null_or_blank(None)
        True
        >>> is_null_or_blank("")
        True
        >>> is_null_or_blank("   ")
        True
        >>> is_null_or_blank("\\t\\n")
        True
        >>> is_null_or_blank("hello")
        False
        >>> is_null_or_blank("  hi  ")
        False
        >>> is_null_or_blank(0)
        False
        >>> is_null_or_blank([])
        False

    """
    if value is None:
        return True
    if isinstance(value, str):
        # Empty string: `not value` is O(1) — avoids calling isspace on "".
        # isspace() on a non-empty string is a pure C scan with no allocation.
        return not value or value.isspace()
    return False
