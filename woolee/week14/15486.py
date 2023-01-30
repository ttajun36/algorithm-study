N = int(input())
dp = [0] * (N + 2)
for day in range(1, N + 1):
    t, p = map(int, input().split(' '))
    # print(day, t, p)
    dp[day] = max(dp[day], dp[day-1]) # 일단 현재 금액
    if day + t <= N + 1:
        # dp[i]는 i 일에 일이 없고, 그때 벌 수 있는 최대 금액
        dp[day + t] = max(dp[day + t], dp[day] + p) # 원래 기억했던 거랑 벌게되는 값을 비교
    # print(dp[1:])
print(max(dp))