def count_change(money, coins):
    import sys
    sys.setrecursionlimit(10**4)
    coins.sort()

    def backtraking(k, count):
        global num
        if num == money:
            return count + 1
        for i in range(k, len(coins)):
            num += coins[i]
            if num > money:
                num -= coins[i]
                break
            count = backtraking(i, count)
            num -= coins[i]
        return count

    global num
    num = 0
    return backtraking(0, 0)