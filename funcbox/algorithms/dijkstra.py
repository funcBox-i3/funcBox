import heapq
from typing import Any


def dijkstra(graph: dict, start_node: Any, end_node: Any = None) -> dict:
    """Compute Dijkstra's shortest path algorithm to find the shortest paths from a start node to all other nodes in a graph,
    or to a specific end node if specified.

    Args:
        graph (dict): A graph represented as an adjacency list, where keys are nodes and values are dictionaries
                      mapping neighbors to edge weights.
        start_node (Any): The node to start the pathfinding from.
        end_node (Any, optional): If specified, the algorithm will terminate early once the shortest path
                                 to this node is found. Defaults to None.

    Returns:
        dict: A dictionary containing two dictionaries:
              - 'distances': Shortest distances from the start node to each node (or just to end_node if specified).
              - 'paths': Shortest paths from the start node to each node (or just to end_node if specified).
              When end_node is specified, only distances and paths for nodes processed before finding the end_node
              will be included. Nodes not reachable will have a distance of infinity and path as None.

    Raises:
        ValueError: If the graph is not a dictionary, any node's adjacency value is not a dict,
                   any edge weight is negative or non-numeric, any neighbor is not a node in the
                   graph, start_node is not in the graph, or end_node is not in the graph.

    Examples:
        >>> graph = {
        ...     'A': {'B': 4, 'C': 2},
        ...     'B': {'D': 5, 'E': 1},
        ...     'C': {'B': 1, 'E': 3},
        ...     'D': {'F': 2},
        ...     'E': {'D': 1, 'F': 4},
        ...     'F': {}
        ... }
        >>> dijkstra(graph, 'A')
        ({'A': 0, 'B': 3, 'C': 2, 'D': 4, 'E': 4, 'F': 6}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C'], 'D': ['A', 'C', 'B', 'E', 'D'], 'E': ['A', 'C', 'E'], 'F': ['A', 'C', 'B', 'E', 'D', 'F']})        >>> dijkstra(graph, 'A', 'F')
        {'distances': {'A': 0, 'C': 2, 'B': 3, 'E': 4, 'D': 4, 'F': 6}, 'paths': {'A': ['A'], 'C': ['A', 'C'], 'B': ['A', 'C', 'B'], 'E': ['A', 'C', 'E'], 'D': ['A', 'C', 'E', 'D'], 'F': ['A', 'C', 'E', 'D', 'F']}}

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
                msg = f"Neighbor {neighbor!r} of node {node!r} is not a node in the graph"
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

    def reconstruct_path(node):
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
