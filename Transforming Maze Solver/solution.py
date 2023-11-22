def maze_solver(ar):
    from heapq import heappop, heappush

    arr = [[0] * len(ar[0]) for _ in range(len(ar))]
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == 'B':
                sx, sy = i, j
                arr[i][j] = 0
            elif ar[i][j] == 'X':
                ex, ey = i, j
                arr[i][j] = 0
            else:
                arr[i][j] = ar[i][j]

    def rotate(num, i):
        for _ in range(i):
            num *= 2
            if num > 15: num -= 15
        return num

    
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    nwall, dwall = [8, 4, 2, 1], [2, 1, 8, 4]
    p = ['N', 'W', 'S', 'E']

    
    heap = [(0, sx, sy, '')]
    visited = [[[False] * 4 for _ in range(len(ar[0]))] for _ in range(len(ar))]
    visited[sx][sy][0] = True

    while heap:
        cnt, nx, ny, path = heappop(heap)
        if (nx, ny) == (ex, ey):
            return path.split()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                if not visited[x][y][cnt % 4]:
                    if not (nwall[i] & rotate(arr[nx][ny], cnt % 4)):
                        if not (dwall[i] & rotate(arr[x][y], cnt % 4)):
                            visited[x][y][cnt % 4] = True
                            heappush(heap, (cnt, x, y, path + p[i]))
        if not visited[nx][ny][(cnt + 1) % 4]:
            visited[nx][ny][(cnt + 1) % 4] = True
            heappush(heap, (cnt + 1, nx, ny, path + ' '))
                    
    return None