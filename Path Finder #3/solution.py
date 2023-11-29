def path_finder(area):
    from heapq import heappop, heappush
    area = area.split('\n')
    INF = float("inf")
    N = len(area)

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    dp = [[INF] * N for _ in range(N)]
    dp[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        n_dist, nx, ny = heappop(heap)
        if dp[nx][ny] < n_dist:
            continue
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N:
                dist = n_dist + abs(int(area[nx][ny]) - int(area[x][y]))
                if dp[x][y] > dist:
                    dp[x][y] = dist
                    heappush(heap, (dist, x, y))
    
    return dp[N - 1][N - 1]