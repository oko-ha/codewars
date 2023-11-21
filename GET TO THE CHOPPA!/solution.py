from preloaded import Node, print_grid # Use print_grid function to visualize a given path on the given grid. 

def find_shortest_path(grid:list, start_node:Node, end_node:Node):
    from collections import deque
    
    if not grid: return []
    
    queue = deque([(start_node, [start_node])])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    visited[0][0] = True
    while queue:
        n_node, path = queue.popleft()
        nx, ny = n_node.position.x, n_node.position.y
        if grid[nx][ny] is end_node:
            return path
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y].passable:
                visited[x][y] = True
                queue.append((grid[x][y], path + [grid[x][y]]))