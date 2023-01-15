import sys


N, M = map(int, sys.stdin.readline().rstrip().split(' '))
board_input = list()
for _ in range(N):
    board_input.append(list(sys.stdin.readline().rstrip()))

answer = 2 ** 32 - 1
for start_y in range(N - 7):
    for start_x in range(M - 7):
        board = [board_input[line][start_x : start_x + 8] for line in range(start_y, start_y + 8)]
        # board[0][0] 확인
        if board[0][0] == 'W':
            count = 0
            for y in range(8):
                for x in range(8):
                    if y % 2 == 1:
                        if x % 2 == 1 and board[y][x] == "B":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "W":
                            count += 1
                    else:
                        if x % 2 == 1 and board[y][x] == "W":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "B":
                            count += 1
            answer = min(answer, count)
            
            count = 0
            for y in range(8):
                for x in range(8):
                    if y % 2 == 1:
                        if x % 2 == 1 and board[y][x] == "W":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "B":
                            count += 1
                    else:
                        if x % 2 == 1 and board[y][x] == "B":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "W":
                            count += 1
            answer = min(answer, count)
            
        else:
            count = 0
            for y in range(8):
                for x in range(8):
                    if y % 2 == 1:
                        if x % 2 == 1 and board[y][x] == "W":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "B":
                            count += 1
                    else:
                        if x % 2 == 1 and board[y][x] == "B":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "W":
                            count += 1
            answer = min(answer, count)
            
            count = 0
            for y in range(8):
                for x in range(8):
                    if y % 2 == 1:
                        if x % 2 == 1 and board[y][x] == "B":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "W":
                            count += 1
                    else:
                        if x % 2 == 1 and board[y][x] == "W":
                            count += 1
                        elif x % 2 == 0 and board[y][x] == "B":
                            count += 1
            answer = min(answer, count)
print(answer)