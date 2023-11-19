def solve(s, ops):
    arr = [[[0, 0] for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] == 't':
            arr[i][i] = [1, 0]
        else:
            arr[i][i] = [0, 1]

    def backtracking(start, end):
        if arr[start][end] != [0, 0]:
            return arr[start][end]
        temp = [0, 0]
        for i in range(start, end):
            left = backtracking(start, i)
            right = backtracking(i + 1, end)

            if ops[i] == '&':
                temp[0] += left[0] * right[0]
                temp[1] += left[0] * right[1] + left[1] * right[0] + left[1] * right[1]
            elif ops[i] == '|':
                temp[0] += left[0] * right[1] + left[1] * right[0] + left[0] * right[0]
                temp[1] += left[1] * right[1]
            else:
                temp[0] += left[0] * right[1] + left[1] * right[0]
                temp[1] += left[0] * right[0] + left[1] * right[1]
        arr[start][end] = temp
        return temp
    
    return backtracking(0, len(ops))[0]