def hamming(n):
    answer = [1]
    base = [2, 3, 5]
    exp = [0, 0, 0]
    num = [2, 3, 5]
    for _ in range(n - 1):
        x = min(num)
        answer.append(x)
        for i, k in enumerate(num):
            if k == x:
                exp[i] += 1
                num[i] = base[i] * answer[exp[i]]
    return answer[-1]