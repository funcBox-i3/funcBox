from __future__ import annotations

from typing import Any

__all__ = ["deep_merge"]


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge *override* into *base*, returning a new dict.

    Unlike ``{**base, **override}`` (which is a *shallow* merge), this
    function recurses into nested dicts so that deeply nested keys are
    merged rather than overwritten.

    Rules:

    - If the same key exists in **both** dicts and **both** values are
      dicts, the sub-dicts are merged recursively.
    - In all other cases the value from *override* wins.
    - Neither *base* nor *override* is mutated.

    Args:
        base: The starting dictionary.  Values here are used when *override*
            does not supply a matching key.
        override: Dictionary whose values take precedence.  Keys not present
            in *base* are added to the result.

    Returns:
        A new dict representing the deep merge of *base* and *override*.

    Raises:
        TypeError: If either argument is not a ``dict``.

    Examples:
        >>> base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
        >>> override = {"db": {"port": 5433, "name": "prod"}, "debug": True}
        >>> deep_merge(base, override)
        {'db': {'host': 'localhost', 'port': 5433, 'name': 'prod'}, 'debug': True}

        >>> deep_merge({"a": 1}, {"b": 2})
        {'a': 1, 'b': 2}

        >>> deep_merge({"x": {"y": 1}}, {"x": "flat"})
        {'x': 'flat'}

    """
    if type(base) is not dict and not isinstance(base, dict):
        msg = f"base must be a dict, got {type(base).__name__!r}"
        raise TypeError(msg)
    if type(override) is not dict and not isinstance(override, dict):
        msg = f"override must be a dict, got {type(override).__name__!r}"
        raise TypeError(msg)

    # Fast path for empty base or override
    if not base:
        return override.copy()
    if not override:
        return base.copy()

    # Fast path: use native dictionary update, then manually recurse on shared dict keys
    result = {**base, **override}
    for key, ov_val in override.items():
        if key in base:
            base_val = base[key]
            if type(base_val) is dict and type(ov_val) is dict:
                result[key] = deep_merge(base_val, ov_val)

    return result
