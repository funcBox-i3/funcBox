from __future__ import annotations

import heapq
from typing import Any

__all__ = ["dijkstra"]


def dijkstra(graph: dict, start_node: Any, end_node: Any = None) -> dict:
    """Compute shortest paths using Dijkstra's algorithm.

    Args:
        graph: Graph as an adjacency mapping ``{node: {neighbor: weight}}``.
        start_node: Source node.
        end_node: Optional destination node for early termination.

    Returns:
        A dictionary with:
        - ``"distances"``: shortest distances from ``start_node``.
        - ``"paths"``: corresponding shortest paths.

    Raises:
        ValueError: If graph structure is invalid, weights are invalid, or
            ``start_node``/``end_node`` are not present in the graph.

    Examples:
        >>> graph = {
        ...     'A': {'B': 4, 'C': 2},
        ...     'B': {'D': 5, 'E': 1},
        ...     'C': {'B': 1, 'E': 3},
        ...     'D': {'F': 2},
        ...     'E': {'D': 1, 'F': 4},
        ...     'F': {}
        ... }
        >>> result = dijkstra(graph, 'A', 'F')
        >>> result['distances']['F']
        7

    """
    if not isinstance(graph, dict):
        msg = "The graph must be a dictionary represented as an adjacency list."
        raise ValueError(msg)
    for node, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            msg = f"Adjacency list for node {node!r} must be a dict, got {type(neighbors).__name__!r}"
            raise ValueError(msg)
        for neighbor, weight in neighbors.items():
            if neighbor not in graph:
                msg = (
                    f"Neighbor {neighbor!r} of node {node!r} is not a node in the graph"
                )
                raise ValueError(msg)
            if not isinstance(weight, (int, float)) or isinstance(weight, bool):
                msg = f"Edge weight from {node!r} to {neighbor!r} must be a number, got {type(weight).__name__!r}"
                raise ValueError(msg)
            if weight < 0:
                msg = f"Edge weight from {node!r} to {neighbor!r} must be non-negative, got {weight}"
                raise ValueError(msg)
    if start_node not in graph:
        msg = "The start_node must be a node present in the graph."
        raise ValueError(msg)
    if end_node is not None and end_node not in graph:
        msg = "The end_node must be a node present in the graph."
        raise ValueError(msg)

    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    predecessors = dict.fromkeys(graph)
    priority_queue = [(0, start_node)]
    visited = set()

    def reconstruct_path(node: Any) -> list[Any]:
        path = []
        while node is not None:
            path.append(node)
            node = predecessors[node]
        return path[::-1]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if end_node is not None and current_node == end_node:
            processed_distances = {
                node: dist for node, dist in distances.items() if dist != float("inf")
            }
            processed_paths = {
                node: reconstruct_path(node) for node in processed_distances
            }
            return {"distances": processed_distances, "paths": processed_paths}

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    paths = {
        node: reconstruct_path(node) if distances[node] != float("inf") else None
        for node in graph
    }
    return {"distances": distances, "paths": paths}
