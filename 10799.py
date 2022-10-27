#10799  [BOJ] 쇠막대기 / 실버 2 / 40분
arr= list(input())
ans = 0
stack = []

for i in range(len(arr)):
  if arr[i] == '(':
    stack.append('(')
  else:
    if arr[i-1]=='(':
      stack.pop()
      ans += len(stack)
    else:
      stack.pop()
      ans+=1

print(ans)