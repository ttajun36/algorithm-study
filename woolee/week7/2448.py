import sys


def recursion(top, l_bot, r_bot):
    # 기저 조건 : 높이가 3인 경우
    if (l_bot[0] - top[0]) == 2:
        board[top[0]][top[1]] = '*'
        board[top[0] + 1][(top[1] + l_bot[1]) // 2] = "*"
        board[top[0] + 1][(top[1] + r_bot[1]) // 2] = "*"
        board[top[0] + 2][l_bot[1] : r_bot[1]] = "*****"
        return
    
    mid_1 = ((top[0] + l_bot[0]) // 2, (top[1] + l_bot[1]) // 2 + 1)
    mid_2 = ((top[0] + r_bot[0]) // 2, (top[1] + r_bot[1]) // 2)
    mid_3 = (l_bot[0], top[1])
    # 중앙 상단
    recursion(top, mid_1, mid_2)
    # 좌하단
    recursion((mid_1[0] + 1, mid_1[1] - 1), l_bot, mid_3)
    # 우하단
    recursion((mid_2[0] + 1, mid_2[1]), (mid_3[0], mid_3[1] + 1), r_bot)
    return

N = int(sys.stdin.readline().rstrip())
# 기저 조건은 line이 3인 경우
"""
  *
 * *
*****
line이 3인 경우에는 위의 3각형을 그리게 됨.

미리 board를 깔아두고 * 위치를 찾아 들어가자
"""
board = [[' '] * (2 * N)  for _ in range(N)]
top = (0, (2 * N - 1) // 2)
l_bot = (N-1, 0)
r_bot = (N-1, 2 * N - 1)
# print(top)
# print(l_bot)
# print(r_bot)
recursion(top, l_bot, r_bot)
# print(board)
for line in range(len(board)):
    sys.stdout.write("".join(board[line][:-1]))
    sys.stdout.write("\n")
