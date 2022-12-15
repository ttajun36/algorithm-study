import sys


N, K = map(int, sys.stdin.readline().rstrip().split(' '))
array_A = list(map(int, sys.stdin.readline().rstrip().split(',')))
for _ in range(K):
    array_B = list()
    for idx in range(len(array_A) - 1):
        array_B.append(array_A[idx + 1] - array_A[idx])
    array_A = array_B
print(",".join(str(x) for x in array_A))