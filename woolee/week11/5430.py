import sys
from collections import deque


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    direction = 1
    error = 0
    size = int(input())
    array = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    for function in p:
        if function == "R":
            direction *= -1
        if function == "D":
            if size == 0:
                error = 1
                break
            if direction == 1:
                array.popleft()
                size -= 1
            else:
                array.pop()
                size -= 1
    if direction == -1:
        array.reverse()
    if error == 1:
        print("error")
    else:
        print("[" + ",".join([str(x) for x in list(array)]) + "]")