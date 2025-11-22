# hw05/main.py
from collections import deque

def parse_grid(lines):
    """
    Parse grid lines into a graph, start, and target positions.
    Returns:
        graph: dict of "r,c" -> list of neighbor "r,c"
        start: "r,c" of S
        target: "r,c" of T
    """
    graph = {}
    start = target = None
    rows = len(lines)
    cols = len(lines[0])

    def pos_str(r, c):
        return f"{r},{c}"

    for r in range(rows):
        for c in range(cols):
            ch = lines[r][c]
            if ch != "#":
                node = pos_str(r, c)
                graph[node] = []
                if ch == "S":
                    start = node
                if ch == "T":
                    target = node

    # Build neighbors (4 directions)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != "#":
                node = pos_str(r, c)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] != "#":
                        graph[node].append(pos_str(nr, nc))

    return graph, start, target


def grid_shortest_path(lines):
    """Return a shortest path from S to T as a list of "r,c", or None if unreachable."""
    graph, start, target = parse_grid(lines)
    if start is None or target is None:
        return None
    if start == target:
        return [start]

    visited = set([start])
    parent = {}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == target:
                    # Reconstruct path
                    path = [target]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path
                queue.append(neighbor)

    return None
