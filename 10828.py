#10828 [BOJ] 스택 / 실버 4 / 10분
import sys
n=int(sys.stdin.readline())

stack = []

for _ in range(n):
  a=sys.stdin.readline().split()
  order = a[0]

  if order == 'push':
    val = a[1]
    stack.append(val)

  elif order == 'pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())

  elif order == "size":
    print(len(stack))

  elif order == "empty":
    if len(stack) == 0:
      print(1)
    else:
      print(0)

  elif order == "top":
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])