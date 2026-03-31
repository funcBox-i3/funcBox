from __future__ import annotations

import re
from collections import Counter

__all__ = ["isAnagram"]

_NON_WORD_RE = re.compile(r"[^\w]")
_NON_WORD_SPACE_RE = re.compile(r"[^\w\s]")


def isAnagram(
        str1: str,
        str2: str,
        case: bool = False,
        spaces: bool = False,
        punct: bool = False,
) -> bool:
    """Check whether two strings are anagrams.

    Args:
        str1: First string.
        str2: Second string.
        case: When ``True``, compare case-insensitively.
        spaces: When ``True``, ignore spaces.
        punct: When ``True``, ignore punctuation.

    Returns:
        ``True`` if the strings are anagrams, else ``False``.

    Raises:
        TypeError: If ``str1`` or ``str2`` is not a string.

    Examples:
        >>> isAnagram("listen", "silent")
        True
        >>> isAnagram("Listen", "Silent", case=True)
        True
        >>> isAnagram("a gentleman", "elegant man", spaces=True)
        True
        >>> isAnagram("Astronomer!", "Moon starer", case=True, punct=True, spaces=True)
        True

    """
    if not isinstance(str1, str):
        msg = f"str1 must be a string, got {type(str1).__name__!r}"
        raise TypeError(msg)
    if not isinstance(str2, str):
        msg = f"str2 must be a string, got {type(str2).__name__!r}"
        raise TypeError(msg)

    def preprocess(s: str) -> str:
        if case:
            s = s.lower()
        if punct and spaces:
            s = _NON_WORD_RE.sub("", s)
        elif punct:
            s = _NON_WORD_SPACE_RE.sub("", s)
        elif spaces:
            s = s.replace(" ", "")
        return s

    str1_processed = preprocess(str1)
    str2_processed = preprocess(str2)

    if len(str1_processed) != len(str2_processed):
        return False

    return Counter(str1_processed) == Counter(str2_processed)
