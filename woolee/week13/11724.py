import sys
from collections import deque
import pprint


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[] for  _ in range(N + 1)]
visited = [0] * (N + 1)
visited[0] = -1
stack = deque()
count = 0
for _ in range(M):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[n].append(m)
    graph[m].append(n)

# searching with dfs
# after search, count and re-search
while True:
    if 0 not in visited[1:N+1]:
        break
    else:
        count += 1
        idx = visited.index(0)
        stack.append(idx)
    while True:
        # print(visited)
        if len(stack) == 0:
            break
        v = stack.popleft()
        if visited[v] != 0:
            continue
        else:
            visited[v] = 1
            for vertex in graph[v]:
                if visited[vertex] == 0:
                    stack.append(vertex)
print(count)