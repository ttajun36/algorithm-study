import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split(' ')))
original = P.copy()
S = list(map(int, sys.stdin.readline().rstrip().split(' ')))
G = [0, 1, 2] * (N // 3)
new = [0] * N
count = 0

while P != G:
    for i in range(N):
        new[S[i]] = P[i]
    
    P = new
    new = [0] * N
    count += 1
    if original == P:
        count = -1
        break
print(count)