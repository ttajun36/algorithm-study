import sys


N, K = map(int, sys.stdin.readline().rstrip().split(' '))
buckets = [0] * 1000001
right = -1
for _ in range(N):
    g, x = map(int, sys.stdin.readline().rstrip().split(' '))
    buckets[x] = g
    right = max(right, x)
jar = 0
for i in range(0, K * 2 + 1):
    if i <= 1000000:
        jar += buckets[i]
# print(jar)
maximum = jar
for i in range(K + 1, right - K + 1):
    jar -= buckets[i - K - 1]
    if i + K <= 1000000:
        jar += buckets[i + K]
    maximum = max(maximum, jar)
print(maximum)