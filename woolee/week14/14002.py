from collections import deque


N = int(input())
array = list(map(int, input().split(' ')))
dp = [1] * N # dp[i]는 array[i]가 마지막인 부분수열의 LIS 값
for i in range(1, N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[j]+1, dp[i])
sub = deque()
print(dp)
count = max(dp)
for idx in range(N-1, -1, -1):
    if dp[idx] == count:
        sub.appendleft(array[idx])
        count -= 1
print(max(dp))
print(" ".join([str(x) for x in list(sub)]))