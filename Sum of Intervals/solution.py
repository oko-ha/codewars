def sum_of_intervals(intervals):
    from heapq import heapify, heappop

    length = 0
    heapify(intervals)
    start, end = heappop(intervals)
    while intervals:
        x, y = heappop(intervals)
        if end > x:
            end = max(end, y)
        else:
            length += abs(end - start)
            start, end = x, y
    length += abs(end - start)

    return length