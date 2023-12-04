def count_patterns_from(firstPoint, length):
    from collections import deque
    graph = {
        'A' : {'B', 'D', 'F', 'H', 'E'},
        'B' : {'A', 'C', 'D', 'F', 'G', 'I', 'E'},
        'C' : {'B', 'F', 'D', 'H', 'E'},
        'D' : {'A', 'G', 'B', 'H', 'C', 'I', 'E'},
        'E' : {'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'},
        'F' : {'C', 'I', 'B', 'H', 'A', 'G', 'E'},
        'G' : {'D', 'H', 'B', 'F', 'E'},
        'H' : {'G', 'I', 'D', 'F', 'A', 'C', 'E'},
        'I' : {'H', 'F', 'D', 'B', 'E'}
        }
    
    ex_graph = {
        'A' : {'B' : 'C', 'D' : 'G', 'E' : 'I'},
        'B' : {'E' : 'H'},
        'C' : {'B' : 'A', 'F' : 'I', 'E' : 'G'},
        'D' : {'E' : 'F'},
        'E' : {},
        'F' : {'E' : 'D'},
        'G' : {'D' : 'A', 'H' : 'I', 'E' : 'C'},
        'H' : {'E' : 'B'},
        'I' : {'H' : 'G', 'F' : 'C', 'E' : 'A'}
    }

    count = 0
    queue = deque([(1, graph[firstPoint], {firstPoint})])
    while queue:
        cnt, path, visit = queue.popleft()
        if cnt == length:
            count += 1
        else:
            for dx in (path - visit):
                temp = set()
                for x, y in ex_graph[dx].items():
                    if x in visit:
                        temp.add(y)
                queue.append((cnt + 1, graph[dx] | temp, visit | {dx}))

    return count