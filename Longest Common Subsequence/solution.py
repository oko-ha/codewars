def lcs(x, y):
    x = ' ' + x
    y = ' ' + y
    dp = [[''] * len(x) for _ in range(len(y))]

    for i in range(1, len(y)):
        for j in range(1, len(x)):
            if y[i] == x[j]:
                dp[i][j] = dp[i - 1][j - 1] + y[i]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]