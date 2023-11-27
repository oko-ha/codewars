def path_finder(maze):
    from collections import deque
    maze = maze.split('\n')
    N = len(maze)

    queue = deque([(0, 0)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    while queue:
        nx, ny = queue.popleft()
        if nx == N - 1 and ny == N - 1:
            return True
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                if maze[x][y] == '.':
                    visited[x][y] = True
                    queue.append((x, y))
    return False