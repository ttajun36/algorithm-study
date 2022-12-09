import sys


def recursion(w_start, h_start, width, height):
    # 기저조건 : board가 2x2인 경우
    if width == 2 and height == 2:
        result = ""
        for h in range(h_start, h_start+height):
            for w in range(w_start, w_start+width):
                result += board[h][w]
        if result == "1111":
            return "1"
        elif result == "0000":
            return "0"
        return "(" + result + ")"

    
    result = ""
    w_mid = w_start + width // 2
    h_mid = h_start + height // 2
    result += recursion(w_start, h_start, width // 2, height // 2) # 좌상단
    result += recursion(w_mid, h_start, width // 2, height // 2) # 우상단 
    result += recursion(w_start, h_mid, width // 2, height // 2) # 좌하단
    result += recursion(w_mid, h_mid, width // 2, height // 2) # 우하단
    if result == "1111":
        return "1"
    elif result == "0000":
        return "0"
    return "(" + result + ")"

N = int(sys.stdin.readline().rstrip())
board = list()
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
# print(board)
print(recursion(0, 0, N, N))