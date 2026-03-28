from collections import Counter


def isAnagram(str1: str, str2: str) -> bool:
    """Check whether two strings are anagrams.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        TypeError: If str1 or str2 is not a string.

    Examples:
        >>> isAnagram("listen", "silent")
        True
        >>> isAnagram("hello", "world")
        False

    """
    if not isinstance(str1, str):
        msg = f"str1 must be a string, got {type(str1).__name__!r}"
        raise TypeError(msg)
    if not isinstance(str2, str):
        msg = f"str2 must be a string, got {type(str2).__name__!r}"
        raise TypeError(msg)
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)
