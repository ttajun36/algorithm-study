import sys


INF = sys.maxsize
N = int(sys.stdin.readline().rstrip())
board = list()
for _ in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    board.append(line)
max_dp = [0] * 3
min_dp = [INF] * 3

max_dp = board[0].copy()
min_dp = board[0].copy()
for i in range(1, N):
    max_dp_0 = max(max_dp[:2]) + board[i][0]
    max_dp_1 = max(max_dp) + board[i][1]
    max_dp_2 = max(max_dp[1:]) + board[i][2]
    
    min_dp_0 = min(min_dp[:2]) + board[i][0]
    min_dp_1 = min(min_dp) + board[i][1]
    min_dp_2 = min(min_dp[1:]) + board[i][2]
    
    max_dp[0], max_dp[1], max_dp[2] = max_dp_0, max_dp_1, max_dp_2
    min_dp[0], min_dp[1], min_dp[2] = min_dp_0, min_dp_1, min_dp_2

# print(max_dp[0], min_dp[0])
print(max(max_dp), min(min_dp))