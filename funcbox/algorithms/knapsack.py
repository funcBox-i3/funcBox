from __future__ import annotations

__all__ = ["knapsack"]


def knapsack(
    weights: list[int],
    values: list[int | float],
    capacity: int,
) -> dict:
    """Solve the 0/1 knapsack problem with space-optimised DP.

    Each item can be included **at most once**.  The goal is to maximise
    the total value of selected items while keeping total weight ≤ *capacity*.

    Uses a 1-D (rolling) DP array so memory is O(capacity) rather than
    O(n × capacity).

    Args:
        weights: Non-negative integer weight of each item.
        values: Non-negative numeric value of each item.
        capacity: Non-negative integer maximum weight capacity.

    Returns:
        A dict with:

        - ``"max_value"`` – the maximum value achievable.
        - ``"selected"`` – list of 0-based indices of the chosen items.
        - ``"total_weight"`` – combined weight of the selected items.

    Raises:
        TypeError: If inputs are not lists or capacity is not an int.
        ValueError: If lists have different lengths, capacity is negative,
            or any weight/value is negative.

    Examples:
        >>> result = knapsack([2, 3, 4, 5], [3, 4, 5, 6], capacity=8)
        >>> result["max_value"]
        10
        >>> sorted(result["selected"])
        [1, 2]

        >>> knapsack([], [], capacity=10)
        {'max_value': 0, 'selected': [], 'total_weight': 0}

    """
    if not isinstance(weights, list):
        msg = f"weights must be a list, got {type(weights).__name__!r}"
        raise TypeError(msg)
    if not isinstance(values, list):
        msg = f"values must be a list, got {type(values).__name__!r}"
        raise TypeError(msg)
    if not isinstance(capacity, int) or isinstance(capacity, bool):
        msg = f"capacity must be an int, got {type(capacity).__name__!r}"
        raise TypeError(msg)
    if len(weights) != len(values):
        msg = (
            f"weights and values must have equal length; "
            f"got {len(weights)} and {len(values)}"
        )
        raise ValueError(msg)
    if capacity < 0:
        msg = f"capacity must be non-negative, got {capacity!r}"
        raise ValueError(msg)

    n = len(weights)
    for i in range(n):
        w, v = weights[i], values[i]
        if not isinstance(w, int) or isinstance(w, bool) or w < 0:
            msg = f"weights[{i}] must be a non-negative int, got {w!r}"
            raise ValueError(msg)
        if (not isinstance(v, (int, float)) or isinstance(v, bool)) or v < 0:
            msg = f"values[{i}] must be a non-negative number, got {v!r}"
            raise ValueError(msg)

    if n == 0 or capacity == 0:
        return {"max_value": 0, "selected": [], "total_weight": 0}

    # Space-optimised DP — 1D array of length capacity+1
    dp = [0] * (capacity + 1)

    for i in range(n):
        w, v = weights[i], values[i]
        if w > capacity:
            continue
        # Traverse right-to-left to ensure each item used at most once
        for c in range(capacity, w - 1, -1):
            candidate = dp[c - w] + v
            dp[c] = max(dp[c], candidate)

    max_value = dp[capacity]

    # Back-track to find selected items
    selected: list[int] = []
    remaining = capacity
    for i in range(n - 1, -1, -1):
        w, v = weights[i], values[i]
        if w <= remaining and dp[remaining] == dp[remaining - w] + v:
            selected.append(i)
            remaining -= w

    selected.reverse()
    total_weight = sum(weights[i] for i in selected)

    return {
        "max_value": max_value,
        "selected": selected,
        "total_weight": total_weight,
    }
