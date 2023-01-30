N = int(input())
array = list(map(int, input().split(' ')))

found = 0

for i in range(N):
    if array[i] > 0:
        found = 1
        break

if found == 0:
    print(max(array))
    quit()

dp = [0] * N
dd = [0] * N
dp[0], dd[0] = max(0, array[0]), max(0, array[0])
for i in range(1, N):
    dp[i] = max(0, dp[i-1] + array[i])
print(dp)
for i in range(1, N):
    dd[i] = max(dd[i-1] + array[i], dp[i-1])
print(dd)
print(max(dd))