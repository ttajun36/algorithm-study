import sys


N, S = map(int, sys.stdin.readline().rstrip().split(' '))
array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
start, end = 0, 0
amount = 0
length = sys.maxsize
while True:
    if end == N and start == end:
        break
    if amount < S:
        if end == N:
            break
        else:
            end += 1
            amount += array[end - 1]
    else:
        length = min(length, end - start)
        amount -= array[start]
        start += 1
if length ==  sys.maxsize:
    print(0)
else:
    print(length)