pos = [0, 0]
d = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def i_am_here(path):
    import re
    global d
    for p in re.sub('(\D)|(\d+)', '\g<0> ', path).split():
        if p == 'r':
            d = (d + 1) % 4
        elif p == 'l':
            d = (d - 1) % 4
        elif p == 'R' or p == 'L':
            d = (d + 2) % 4
        else:
            pos[0] += dx[d] * int(p)
            pos[1] += dy[d] * int(p)

    return pos