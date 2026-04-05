from __future__ import annotations

__all__ = ["truncate"]


def truncate(
    text: str,
    max_length: int,
    suffix: str = "...",
    *,
    word_boundary: bool = False,
) -> str:
    """Shorten *text* to at most *max_length* characters, appending *suffix*.

    The total length of the returned string (including the suffix) never
    exceeds *max_length*.  If *text* already fits, it is returned unchanged.

    When *word_boundary* is ``True`` the cut is walked back to the last
    whitespace so words are never split mid-token.

    Args:
        text: The source string to truncate.
        max_length: Maximum length of the returned string (inclusive of the
            suffix).  Must be a positive integer and at least as long as
            *suffix*.
        suffix: The ellipsis-style indicator appended after the cut.
            Defaults to ``"..."``.
        word_boundary: When ``True``, snap the cut back to the last
            whitespace so no word is split.  Defaults to ``False``.

    Returns:
        The (possibly truncated) string.

    Raises:
        TypeError: If ``text`` is not a ``str``, ``suffix`` is not a ``str``,
            or ``max_length`` is not a plain ``int``.
        ValueError: If ``max_length`` is not positive, or is shorter than
            ``suffix``.

    Examples:
        >>> truncate("Hello, world!", 8)
        'Hello...'
        >>> truncate("Hello, world!", 13)
        'Hello, world!'
        >>> truncate("Hello, world!", 10, suffix="…")
        'Hello, wo…'
        >>> truncate("The quick brown fox", 12, word_boundary=True)
        'The quick...'
        >>> truncate("Hi", 5)
        'Hi'

    """
    if not isinstance(text, str):
        msg = f"text must be a str, got {type(text).__name__!r}"
        raise TypeError(msg)
    if not isinstance(suffix, str):
        msg = f"suffix must be a str, got {type(suffix).__name__!r}"
        raise TypeError(msg)
    if not isinstance(max_length, int) or isinstance(max_length, bool):
        msg = f"max_length must be an int, got {type(max_length).__name__!r}"
        raise TypeError(msg)
    if max_length <= 0:
        msg = f"max_length must be positive, got {max_length!r}"
        raise ValueError(msg)
    if max_length < len(suffix):
        msg = (
            f"max_length ({max_length}) must be >= len(suffix) ({len(suffix)})"
        )
        raise ValueError(msg)

    if len(text) <= max_length:
        return text

    cut = max_length - len(suffix)

    if word_boundary:
        # rfind is a single C-level scan — faster than regex for this case
        boundary = text.rfind(" ", 0, cut)
        if boundary > 0:
            cut = boundary

    return text[:cut] + suffix
