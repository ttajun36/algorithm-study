X = int(input())
dp = [[] for _ in range(X + 1)]
dp[1] = [1]
for i in range(2, X + 1):
    buffer = list()
    if i % 3 == 0:
        if len(buffer) == 0 or len(buffer) > len(dp[i // 3]):
            buffer = dp[i // 3]
    if i % 2 == 0:
        if len(buffer) == 0 or len(buffer) > len(dp[i // 2]):
            buffer = dp[i // 2]
    if len(buffer) == 0 or len(buffer) > len(dp[i - 1]):
            buffer = dp[i - 1]
    dp[i] = [i] + buffer
print(len(dp[X]) - 1)
print(" ".join(str(x) for x in dp[X]))