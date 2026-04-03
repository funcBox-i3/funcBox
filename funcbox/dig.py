from __future__ import annotations

from typing import Any

__all__ = ["Dig"]

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


def _resolve(
    data: dict[str, Any],
    path: str | tuple[str | int, ...],
    default: Any,
    last: bool,
) -> Any:
    if not path:
        return data

    keys = _split_path(path, ".") if isinstance(path, str) else path
    current: Any = data

    for key in keys:
        if isinstance(current, dict):
            nxt = current.get(key, _MISSING)
            if nxt is _MISSING:
                return current if last else default
            current = nxt
            continue

        if isinstance(current, (list, tuple)):
            index = _coerce_index(key)
            if index is _MISSING:
                return current if last else default
            if -len(current) <= index < len(current):
                current = current[index]
                continue
            return current if last else default

        return current if last else default

    return current


def _multi(
    data: dict[str, Any],
    paths: list,
    default: Any,
    last: bool,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for p in paths:
        if not isinstance(p, (str, tuple)):
            msg = (
                f"each path in a multi-path list must be a str or tuple, "
                f"got {type(p).__name__!r}"
            )
            raise TypeError(msg)
        key_name = p if isinstance(p, str) else repr(p)
        result[key_name] = _resolve(data, p, default, last)
    return result


class Dig:
    """Wraps a nested dictionary once for safe, repeated dot-path lookups.

    Resolves values from arbitrarily deep dictionaries and lists using
    dot-separated strings, explicit key sequences (tuples), or a list of
    paths for bulk fetching - all through a single, consistent interface.

    The behaviour of every lookup is driven by the type of ``path`` passed:

    - ``str``   - dot-separated path (e.g. ``"user.projects.0.name"``).
                  Numeric segments like ``"0"`` are automatically treated as
                  list indices when the current node is a sequence.
    - ``tuple`` - explicit key/index sequence (e.g. ``("user", 0, "name")``).
                  Use when keys contain dots or you need unambiguous integer
                  indices.
    - ``list``  - multi-path batch; each element is its own ``str`` or
                  ``tuple`` path. Returns a ``dict`` mapping every path string
                  to its resolved value. ``default`` and ``last`` apply to
                  every entry uniformly.

    Args:
        data: The source dictionary to wrap. Must be a plain ``dict``.

    Raises:
        TypeError: If ``data`` is not a ``dict``.

    Examples:
        >>> from funcbox import Dig
        >>> data = {
        ...     "user": {
        ...         "name": "Aditya Prasad S",
        ...         "handle": "Pu94X",
        ...         "age": 19,
        ...         "address": {"city": "Kanyakumari", "zip": "629000"},
        ...         "projects": [
        ...             {"name": "funcBox",  "stars": 42, "lang": "Python"},
        ...             {"name": "InfiniKit", "stars": 18, "lang": "Kotlin"},
        ...         ],
        ...     }
        ... }
        >>> d = Dig(data)
        >>> d("user.name")
        'Aditya Prasad S'
        >>> d("user.handle")
        'Pu94X'
        >>> d("user.address.city")
        'Kanyakumari'
        >>> d("user.missing", default="N/A")
        'N/A'
        >>> d("user.projects.0.name")
        'funcBox'
        >>> d(["user.name", "user.handle", "user.age"])
        {'user.name': 'Aditya Prasad S', 'user.handle': 'Pu94X', 'user.age': 19}
        >>> addr = d.scope("user.address")
        >>> addr("city")
        'Kanyakumari'
        >>> addr(["city", "zip"])
        {'city': 'Kanyakumari', 'zip': '629000'}

    """

    __slots__ = ("_data",)

    def __init__(self, data: dict[str, Any]) -> None:
        if not isinstance(data, dict):
            msg = f"Dig requires a dict, got {type(data).__name__!r}"
            raise TypeError(msg)
        self._data = data

    def __call__(
        self,
        path: str | tuple[str | int, ...] | list,
        default: Any = None,
        last: bool = False,
    ) -> Any:
        """Resolve ``path`` against the wrapped dictionary.

        Args:
            path: The path to resolve. See class-level docs for type behaviour.
            default: Returned when resolution fails at any key in the path.
                Defaults to ``None``. In multi-path mode, applied to every
                failing entry.
            last: When ``True``, returns the deepest successfully resolved
                value instead of ``default`` on failure. In multi-path mode,
                applied to every entry.

        Returns:
            The resolved value, ``default`` on failure, or a ``dict[str, Any]``
            when ``path`` is a list.

        Raises:
            TypeError: If ``path`` is not a ``str``, ``tuple``, or ``list``;
                or if a multi-path list entry is not a ``str`` or ``tuple``.

        Examples:
            >>> d = Dig({"user": {"name": "Aditya Prasad S", "handle": "Pu94X"}})
            >>> d("user.name")
            'Aditya Prasad S'
            >>> d("user.email", default="not set")
            'not set'
            >>> d("user.email", last=True)
            {'name': 'Aditya Prasad S', 'handle': 'Pu94X'}
            >>> d(["user.name", "user.handle"])
            {'user.name': 'Aditya Prasad S', 'user.handle': 'Pu94X'}

        """
        if isinstance(path, list):
            return _multi(self._data, path, default, last)
        if isinstance(path, (str, tuple)):
            return _resolve(self._data, path, default, last)
        msg = f"path must be a str, tuple, or list, got {type(path).__name__!r}"
        raise TypeError(msg)

    def __getitem__(
        self,
        path: str | tuple[str | int, ...] | list,
    ) -> Any:
        """Subscript shorthand for ``Dig(path)``, returning ``None`` on failure.

        Examples:
            >>> d = Dig({"user": {"name": "Aditya Prasad S"}})
            >>> d["user.name"]
            'Aditya Prasad S'

        """
        return self(path)

    def __contains__(self, path: str | tuple[str | int, ...]) -> bool:
        """Return ``True`` if ``path`` resolves to an existing key.

        A key whose value is explicitly ``None`` is still treated as present
        and returns ``True``.

        Examples:
            >>> d = Dig({"user": {"name": "Pu94X", "email": None}})
            >>> "user.name" in d
            True
            >>> "user.email" in d
            True
            >>> "user.age" in d
            False

        """
        return _resolve(self._data, path, _MISSING, False) is not _MISSING

    def scope(self, path: str | tuple[str | int, ...]) -> Dig:
        """Return a new ``Dig`` rooted at the sub-dictionary at ``path``.

        Useful for avoiding repeated path prefixes when reading multiple values
        from the same nested node.

        Args:
            path: A dot-separated string or key sequence pointing to the target
                sub-dictionary node.

        Returns:
            A new ``Dig`` instance wrapping the resolved sub-dictionary.

        Raises:
            KeyError: If ``path`` does not resolve to any value.
            TypeError: If the value at ``path`` is not a ``dict``.

        Examples:
            >>> d = Dig({"user": {"address": {"city": "Kanyakumari", "zip": "629000"}}})
            >>> addr = d.scope("user.address")
            >>> addr("city")
            'Kanyakumari'
            >>> addr["zip"]
            '629000'
            >>> addr(["city", "zip"])
            {'city': 'Kanyakumari', 'zip': '629000'}

        """
        sub = _resolve(self._data, path, _MISSING, False)
        if sub is _MISSING:
            msg = f"path {path!r} does not exist in the wrapped dict"
            raise KeyError(msg)
        if not isinstance(sub, dict):
            msg = f"scope() requires a dict at {path!r}, got {type(sub).__name__!r}"
            raise TypeError(msg)
        return Dig(sub)

    def __repr__(self) -> str:
        keys = list(self._data.keys())
        preview = keys[:3]
        suffix = ", ..." if len(keys) > 3 else ""
        return f"Dig({{{', '.join(repr(k) for k in preview)}{suffix}}})"
