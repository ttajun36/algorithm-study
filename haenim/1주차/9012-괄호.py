from collections import deque

n = int(input())

for i in range(n):
    stack = deque()
    parentheses = input()

    for parenthesis in parentheses:

        if parenthesis == "(":
            stack.append(parenthesis)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(1)
                break

    if stack:
        print("NO")
    else:
        print("YES")
