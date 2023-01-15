import sys


R, C = map(int, sys.stdin.readline().rstrip().split(' '))
board = [[0] * C for _ in range(R)]
rat = ()
hole = ()
water = list()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for y in range(R):
    board_input = list(sys.stdin.readline().rstrip())
    for x in range(C):
        if board_input[x] == "D":
            hole = (y, x)
        elif board_input[x] == "S":
            rat = (y, x)
        elif board_input[x] == "*":
            board[y][x] = -1
            water.append((y, x))
        elif board_input[x] == "X":
            board[y][x] = -9999
def flood(x, y):
    for i in range(4):
        nx = x +     