from __future__ import annotations

import string

__all__ = ["is_anagram"]

_PUNCT_TABLE = str.maketrans("", "", string.punctuation)


def is_anagram(
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
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("Listen", "Silent", case=True)
        True
        >>> is_anagram("a gentleman", "elegant man", spaces=True)
        True
        >>> is_anagram("Astronomer!", "Moon starer", case=True, punct=True, spaces=True)
        True

    """
    if type(str1) is not str and not isinstance(str1, str):
        msg = f"str1 must be a string, got {type(str1).__name__!r}"
        raise TypeError(msg)
    if type(str2) is not str and not isinstance(str2, str):
        msg = f"str2 must be a string, got {type(str2).__name__!r}"
        raise TypeError(msg)

    def preprocess(s: str) -> str:
        if case:
            s = s.lower()
        if punct:
            s = s.translate(_PUNCT_TABLE)
        if spaces:
            s = s.replace(" ", "")
        return s

    if not case and not spaces and not punct:
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

    str1_processed = preprocess(str1)
    str2_processed = preprocess(str2)

    if len(str1_processed) != len(str2_processed):
        return False

    return sorted(str1_processed) == sorted(str2_processed)
