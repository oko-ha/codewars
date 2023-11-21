def dbl_linear(n):
    from heapq import heappop, heappush
    
    heap = [1]
    num = {1}
    for _ in range(n):
        x = heappop(heap)
        y, z = 2 * x + 1, 3 * x + 1
        heappush(heap, y)
        heappush(heap, z)
        num |= {y, z}

    return sorted(list(num))[n]