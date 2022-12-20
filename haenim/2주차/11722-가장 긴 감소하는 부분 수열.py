"""
dp[i] : i 까지의 가장 긴 감소하는 부분 수열의 길이

앞쪽 숫자들이랑 비교하면서 앞쪽 숫자가 더 클 때만 i까지의 가장 긴 감소하는 부분 수열의 길이 업데이트

nums 60, 10, 50, 20, 30, 20, 10
dp   1 , 1 , 1 , 1,  1,  1,  1
dp   1,  2 , ... 
dp   1 , 2 , 2, ....
dp   1 , 2 , 2,  3, ...
dp   1 , 2 , 2 , 3,  3 ...


"""

n = int(input())
nums = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        # 자신의 앞쪽 숫자와 비교
        if nums[j] > nums[i]:
            # 자신보다 앞쪽의 숫자가 크면 나와 그 숫자는 감소하는 부분 순열이 된다.
            # 그렇다면 앞쪽의 숫자의 부분 수열의 길이에 1을 더하면 자신의 부분 수열의 길이가 된다.
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
