import sys


N = list(sys.stdin.readline().rstrip())
"""
dp[i] 는 N[i] 부터 만들어지는 부분문자열의 암호코드 경우의 수
25114
'4'인 dp[4] = 1, 14는 '1', '4' 와 '14' 두가지. dp[3] = 2
114는  '1' '1' '4', '1' '14', '11' '4' dp[2] = 3.
5114는 '5' '11' '4', '5' '1' '1' '4', '5' '1' '14' dp[3] = 3
만일 맨 앞이 1이거나 맨 앞이 2이고 그 다음이 6 이하인 경우
바로 아래 두 항의 합이 dp 값이 되고
그렇지 않으면 바로 아래 항 값이 그대로 넘어옴     
"""
dp = [0] * len(N)
if N[-1] == '0':
    dp[-1] = 0
else:
    dp[len(N)-1] = 1
for i in range(len(N)-2, -1, -1):
    if N[i] == '0': # 맨 앞이 0이면 만일 최초 입력 값의 맨 앞이 0이면 이걸로 거를 수 있음
        continue # 안함 -> 201인 경우 2 + 01, 20 + 1인데 01은 안하니까 0으로 남음. 따라서 20 + 1만 함
    if N[i] == '1': # 맨 앞이 1이면
        dp[i] += dp[i+1]
        if i + 2 < len(N):
            dp[i] += dp[i+2]
        else:
            dp[i] += 1
    elif i + 1 < len(N) and N[i] == '2' and (int(N[i+1]) <= 6): 
        dp[i] += dp[i+1]
        if i + 2 < len(N):
            dp[i] += dp[i+2]
        else:
            dp[i] += 1
    else:
        dp[i] = dp[i+1]
    # print(dp)
print(dp[0] % 1000000)