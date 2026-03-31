from __future__ import annotations

from typing import Any

__all__ = ["safe_get"]

_PATH_CACHE: dict[tuple[str, str], tuple[str, ...]] = {}
_PATH_CACHE_MAX: int = 4096
_MISSING = object()


def _split_path(path: str, separator: str) -> tuple[str, ...]:
    key = (path, separator)
    cached = _PATH_CACHE.get(key)
    if cached is not None:
        return cached
    if len(_PATH_CACHE) >= _PATH_CACHE_MAX:
        _PATH_CACHE.clear()
    result = tuple(path.split(separator)) if path else ()
    _PATH_CACHE[key] = result
    return result


def _coerce_index(key: str | int) -> int | object:
    if isinstance(key, int):
        return key
    if isinstance(key, str):
        if key and (key.isdigit() or (key[0] in "+-" and key[1:].isdigit())):
            return int(key)
    return _MISSING


def safe_get(
        dictionary: dict[str, Any],
        path: str | list[str | int] | tuple[str | int, ...],
        default: Any = None,
        return_last_seen: bool = False,
        separator: str = ".",
) -> Any:
    """Fetch a value from nested dictionaries and sequences using a path.

    Args:
        dictionary: The source dictionary.
        path: Dot-separated key path (e.g. ``"user.profile.city"``), or an
            explicit key sequence (e.g. ``["user", 0, "city"]``). An empty
            string or empty sequence returns *dictionary* unchanged.
        default: Returned when any key in the path is missing or an
            intermediate value is not traversable.
        return_last_seen: When ``True``, returns the deepest successfully
            resolved value before traversal fails instead of *default*.
        separator: Delimiter used to split a string *path* (default ``"."``).
            Ignored when *path* is already a key sequence.

    Returns:
        The resolved value, or *default* / last resolved value on failure.

    Examples:
        >>> safe_get({"user": {"profile": {"city": "Chennai"}}}, "user.profile.city")
        'Chennai'
        >>> safe_get({"user": {}}, "user.profile.city", default="unknown")
        'unknown'
        >>> safe_get({"user": {"profile": {}}}, "user.profile.city", return_last_seen=True)
        {}
        >>> safe_get({"user": None}, "user.profile.city", return_last_seen=True)
        None
        >>> safe_get({"a": {0: "zero"}}, ["a", 0])
        'zero'
        >>> safe_get({"employees": [{"name": "Alice"}]}, "employees.0.name")
        'Alice'

    """
    if not path:
        return dictionary

    if isinstance(path, str):
        if not isinstance(separator, str):
            msg = f"separator must be a string, got {type(separator).__name__!r}"
            raise TypeError(msg)
        keys = _split_path(path, separator)
    elif isinstance(path, (list, tuple)):
        keys = path
    else:
        msg = f"path must be a string, list, or tuple, got {type(path).__name__!r}"
        raise TypeError(msg)

    current: Any = dictionary

    for key in keys:
        if isinstance(current, dict):
            next_value = current.get(key, _MISSING)
            if next_value is _MISSING:
                return current if return_last_seen else default
            current = next_value
            continue

        if isinstance(current, (list, tuple)):
            index = _coerce_index(key)
            if index is _MISSING:
                return current if return_last_seen else default
            if -len(current) <= index < len(current):
                current = current[index]
                continue
            return current if return_last_seen else default

        return current if return_last_seen else default

    return current
