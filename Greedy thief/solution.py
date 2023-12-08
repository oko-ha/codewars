from preloaded import Item

def greedy_thief( items:list[Item], n:int) -> list[Item] :
    dp = [[[0, []] for _ in range(n + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for j in range(n + 1):
            if j >= items[i - 1].weight:
                if dp[i - 1][j][0] > dp[i - 1][j - items[i - 1].weight][0] + items[i - 1].price:
                    dp[i][j][0] = dp[i - 1][j][0]
                    dp[i][j][1] = dp[i - 1][j][1]
                else:
                    dp[i][j][0] = dp[i - 1][j - items[i - 1].weight][0] + items[i - 1].price
                    dp[i][j][1] = dp[i - 1][j - items[i - 1].weight][1] + [items[i - 1]]
            else:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = dp[i - 1][j][1]
    return dp[-1][-1][-1]