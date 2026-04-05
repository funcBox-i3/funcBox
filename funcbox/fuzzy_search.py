from __future__ import annotations

from collections.abc import Sequence
from typing import Any

__all__ = ["fuzzy_search", "levenshtein_distance", "similarity"]


def levenshtein_distance(a: str, b: str) -> int:
    """Return the Levenshtein edit distance between *a* and *b*.

    Counts the minimum number of single-character **insertions**,
    **deletions**, and **substitutions** required to transform *a* into *b*.
    Transpositions of adjacent characters are counted as **two** edits
    (one deletion + one insertion).  Use :func:`osa_distance` if you want
    transpositions to cost 1 edit instead.

    The implementation uses the classic single-row DP approach with
    ``O(min(|a|, |b|))`` extra space.

    Args:
        a: First string.
        b: Second string.

    Returns:
        A non-negative integer.  ``0`` means the strings are identical.

    Raises:
        TypeError: If either argument is not a ``str``.

    Examples:
        >>> levenshtein_distance("kitten", "sitting")
        3
        >>> levenshtein_distance("hello", "hello")
        0
        >>> levenshtein_distance("dijktra", "dijkstra")
        1
        >>> levenshtein_distance("", "abc")
        3

    """
    if not isinstance(a, str):
        msg = f"a must be a str, got {type(a).__name__!r}"
        raise TypeError(msg)
    if not isinstance(b, str):
        msg = f"b must be a str, got {type(b).__name__!r}"
        raise TypeError(msg)

    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    if len(a) < len(b):
        a, b = b, a

    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            curr[j] = min(
                prev[j] + 1,
                curr[j - 1] + 1,
                prev[j - 1] + (ca != cb),
            )
        prev = curr

    return prev[-1]


def _osa_distance(a: str, b: str) -> int:
    """Return the Optimal String Alignment (OSA) distance between *a* and *b*.

    Like Levenshtein but also allows **transpositions** of two adjacent
    characters as a single edit.  This means ``"pytohn"`` → ``"python"``
    costs 1 (one transposition) instead of 2 (delete + insert).

    Note: OSA does *not* satisfy the triangle inequality, so it is not a
    true metric, but it is well-suited as a typo-tolerance heuristic.
    """
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    la, lb = len(a), len(b)
    dp = [[0] * (lb + 1) for _ in range(la + 1)]

    for i in range(la + 1):
        dp[i][0] = i
    for j in range(lb + 1):
        dp[0][j] = j

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost,
            )
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[la][lb]


def _partial_window_ratio(query: str, candidate: str) -> float:
    """Score *query* against its best-fitting window inside *candidate*.

    Slides a window of ``len(query)`` characters across *candidate* and
    returns the maximum edit-similarity found across all windows.  This
    rewards cases where *query* is cleanly contained within a longer
    *candidate* (e.g. ``"search"`` inside ``"fuzzy_search"``).

    Returns ``0.0`` if *query* is longer than *candidate*.
    """
    lq = len(query)
    lc = len(candidate)

    if lq == 0:
        return 1.0
    if lq > lc:
        return 0.0

    best = 0.0
    for start in range(lc - lq + 1):
        window = candidate[start : start + lq]
        dist = _osa_distance(query, window)
        score = 1.0 - dist / lq
        best = max(best, score)
        if best == 1.0:
            break

    return best


def similarity(query: str, candidate: str) -> float:
    """Return a similarity score in ``[0.0, 1.0]`` between *query* and *candidate*.

    The score blends three complementary signals:

    - **OSA edit-distance ratio** (weight 0.5): ``1 - osa(q, c) / max_len``.
      Rewards strings that require few edits to become equal, and correctly
      treats transpositions of adjacent characters as a *single* edit.
    - **Subsequence coverage** (weight 0.3): fraction of *query* characters
      that appear as an ordered subsequence in *candidate*.
      Rewards strings that "contain" the query in the right order.
    - **Partial-window ratio** (weight 0.2): best OSA similarity of *query*
      against any same-length window sliding across *candidate*.
      Rewards cases where the query is a clean substring of the candidate
      (e.g. ``"search"`` inside ``"fuzzy_search"``).

    Both strings are normalised to lowercase before comparison.

    Args:
        query: The reference string (e.g. the user's search term).
        candidate: The string to score against *query*.

    Returns:
        A ``float`` in ``[0.0, 1.0]``.  ``1.0`` means the strings are
        identical (case-insensitively); ``0.0`` means completely dissimilar.

    Raises:
        TypeError: If either argument is not a ``str``.

    Examples:
        >>> similarity("hello", "hello")
        1.0
        >>> similarity("pyth", "Python")      # partial prefix match
        0.8
        >>> similarity("dijktra", "dijkstra") # typo tolerance
        0.8804
        >>> similarity("pytohn", "python")    # transposition — 1 edit (OSA)
        0.7833
        >>> similarity("search", "fuzzy_search")  # substring
        0.75
        >>> similarity("abc", "xyz")
        0.0

    """
    if not isinstance(query, str):
        msg = f"query must be a str, got {type(query).__name__!r}"
        raise TypeError(msg)
    if not isinstance(candidate, str):
        msg = f"candidate must be a str, got {type(candidate).__name__!r}"
        raise TypeError(msg)

    q = query.lower()
    c = candidate.lower()

    max_len = max(len(q), len(c))
    osa_ratio = 1.0 if max_len == 0 else 1.0 - _osa_distance(q, c) / max_len

    qi = 0
    for ch in c:
        if qi < len(q) and ch == q[qi]:
            qi += 1
    subseq = qi / len(q) if q else 1.0

    partial = _partial_window_ratio(q, c)

    return round(0.5 * osa_ratio + 0.3 * subseq + 0.2 * partial, 4)


def fuzzy_search(
    query: str,
    candidates: Sequence[Any],
    *,
    threshold: float = 0.0,
    limit: int | None = None,
    key: Any = None,
) -> list[dict[str, Any]]:
    """Find the best fuzzy matches for *query* within *candidates*.

    Each candidate is scored using a blend of OSA edit-distance similarity,
    subsequence coverage, and partial-window ratio.  Results are returned
    sorted by descending score (best match first).

    This function has **zero external dependencies** — it relies entirely on
    Python's standard library.

    Args:
        query: The search string.
        candidates: A sequence of items to search through.  Items may be
            plain strings or arbitrary objects when *key* is provided.
        threshold: Minimum score (inclusive) in the range ``[0.0, 1.0]``.
            Candidates scoring below this value are excluded.  Defaults to
            ``0.0`` (all candidates are returned).
        limit: Maximum number of results to return.  ``None`` (default)
            returns all matches above the threshold.
        key: A callable that extracts the comparison string from each
            candidate item.  When ``None``, each candidate must itself be a
            string.

    Returns:
        A list of dicts, each containing:

        - ``'match'`` – the original candidate item.
        - ``'score'`` – similarity score as a ``float`` in ``[0.0, 1.0]``.

        The list is sorted by ``'score'`` descending.  An empty list is
        returned when there are no matches above the threshold.

    Raises:
        TypeError: If ``query`` is not a ``str``.
        TypeError: If ``candidates`` is not a ``Sequence`` (or is a bare
            ``str``).
        TypeError: If ``key`` is not callable (when provided).
        TypeError: If any candidate cannot be converted to ``str`` (when no
            *key* is given).
        ValueError: If ``threshold`` is not in ``[0.0, 1.0]``.
        ValueError: If ``limit`` is not a positive integer (when provided).

    Examples:
        >>> fuzzy_search("pyth", ["Python", "Ruby", "Rust", "PyPy"])
        [{'match': 'Python', 'score': ...}, {'match': 'PyPy', 'score': ...}, ...]

        >>> fuzzy_search("dijktra", ["dijkstra", "binary search", "bubble sort"])
        [{'match': 'dijkstra', 'score': ...}, ...]

        >>> people = [{"name": "Alice"}, {"name": "Alicia"}, {"name": "Bob"}]
        >>> fuzzy_search("alic", people, key=lambda p: p["name"])
        [{'match': {'name': 'Alice'}, 'score': ...}, ...]

        >>> fuzzy_search("rust", ["Python", "Ruby", "Rust"], threshold=0.5)
        [{'match': 'Rust', 'score': 1.0}]

    """
    if not isinstance(query, str):
        msg = f"query must be a str, got {type(query).__name__!r}"
        raise TypeError(msg)

    if isinstance(candidates, str):
        msg = "candidates must be a Sequence of items, not a bare str"
        raise TypeError(msg)
    if not isinstance(candidates, Sequence):
        msg = f"candidates must be a Sequence, got {type(candidates).__name__!r}"
        raise TypeError(
            msg,
        )

    if key is not None and not callable(key):
        msg = f"key must be callable, got {type(key).__name__!r}"
        raise TypeError(msg)

    if not isinstance(threshold, (int, float)) or isinstance(threshold, bool):
        msg = (
            f"threshold must be a float in [0.0, 1.0], got {type(threshold).__name__!r}"
        )
        raise TypeError(
            msg,
        )
    if not (0.0 <= threshold <= 1.0):
        msg = f"threshold must be in [0.0, 1.0], got {threshold!r}"
        raise ValueError(msg)

    if limit is not None:
        if not isinstance(limit, int) or isinstance(limit, bool):
            msg = f"limit must be a positive int, got {type(limit).__name__!r}"
            raise TypeError(msg)
        if limit <= 0:
            msg = f"limit must be a positive int, got {limit!r}"
            raise ValueError(msg)

    results: list[dict[str, Any]] = []
    for item in candidates:
        if key is not None:
            text = key(item)
            if not isinstance(text, str):
                msg = f"key must return a str, got {type(text).__name__!r}"
                raise TypeError(
                    msg,
                )
        else:
            if not isinstance(item, str):
                msg = (
                    f"each candidate must be a str when no key is provided, "
                    f"got {type(item).__name__!r}"
                )
                raise TypeError(
                    msg,
                )
            text = item

        score = similarity(query, text)
        if score >= threshold:
            results.append({"match": item, "score": round(score, 4)})

    results.sort(key=lambda r: r["score"], reverse=True)

    if limit is not None:
        results = results[:limit]

    return results
