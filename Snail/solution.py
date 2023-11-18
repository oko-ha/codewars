from math import ceil
def snail(snail_map):
    answer = []
    length = len(snail_map[0])
    for i in range(ceil(length / 2)):
        # right
        for j in range(i, length - i):
            answer.append(snail_map[i][j])
        # down
        for j in range(i + 1, length - i):
            answer.append(snail_map[j][length - 1 - i])
        # left
        for j in range(length - 2 - i, i - 1, -1):
            answer.append(snail_map[length - 1 - i][j])
        # up
        for j in range(length - 2 - i, i, -1):
            answer.append(snail_map[j][i])
    return answer