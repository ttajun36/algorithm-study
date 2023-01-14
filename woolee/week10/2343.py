import sys


N, M = map(int, sys.stdin.readline().rstrip().split(' '))
movies = list(map(int, sys.stdin.readline().rstrip().split(' ')))
left, right = max(movies), sum(movies)

while left <= right:
    mid = (left + right) // 2
    count = 0
    temp = 0
    
    for i in range(N):
        if temp + movies[i] > mid:
            count += 1
            temp = 0
        temp += movies[i]
    
    count += 1 if temp else 0
    
    if count <= M:
        right = mid - 1
    else:
        left = mid + 1
print(left)