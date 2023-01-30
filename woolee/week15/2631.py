N = int(input())
array = list()
for _ in range(N):
    array.append(int(input()))
# print(array)
dp = [1] * N # dp[i] 는 array[i] 가 마지막인 부분 수열의 최장 연속 수열
# 최장 연속 수열 구하기
for i in range(1, N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(N - max(dp))