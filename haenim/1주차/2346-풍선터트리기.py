from collections import deque

n = int(input())
dq = deque([(idx, int(num)) for idx, num in enumerate(input().split())])

idx = 0

answer = []
while dq:
    idx, elem = dq.popleft()
    answer.append(str(idx + 1))

    if elem < 0:
        dq.rotate(-elem)
    else:
        dq.rotate(-elem + 1)

print(" ".join(answer))
