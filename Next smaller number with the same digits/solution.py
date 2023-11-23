def next_smaller(n):
    num = list(map(int, str(n)))
    for i in range(len(num) - 2, -1, -1):
        for j in range(len(num) - 1, i, -1):
            if i == 0 and num[j] == 0:
                break
            if num[i] > num[j]:
                temp = num[j]
                num[j] = 10
                return int(''.join(map(str, num[:i] + [temp] + sorted(num[i:], reverse = True)[1:])))
    return -1