import sys


costs = list()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    cost = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    costs.append(cost)
    
dp = costs[0].copy()
for i in range(1, N):
    dp_0 = min(dp[1], dp[2]) + costs[i][0]
    dp_1 = min(dp[0], dp[2]) + costs[i][1]
    dp_2 = min(dp[0], dp[1]) + costs[i][2]
    dp = [dp_0, dp_1, dp_2]
print(min(dp))