def bridge(islands):
    from heapq import heappop, heappush
    from math import sqrt

    heap = [(0, 0)]
    dp = [0] + [float("inf")] * (len(islands) - 1)
    visited = [False] * len(islands)
    answer = 0
    while heap:
        n_dist, ni = heappop(heap)
        if not visited[ni]:
            visited[ni] = True
            answer += n_dist
            nx, ny = islands[ni]
            for di in range(len(islands)):
                dx, dy = islands[di]
                if visited[di]:
                    continue
                dist = sqrt(abs(nx - dx) ** 2 + abs(ny - dy) ** 2)
                if dp[di] > dist:
                    dp[di] = dist
                    heappush(heap, (dist, di))

    return sum(dp)