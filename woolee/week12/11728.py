import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
A = list(map(int, sys.stdin.readline().rstrip().split(" ")))
B = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(" ".join([str(x) for x in sorted(A + B)]))