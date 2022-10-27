#9012 [BOJ] 괄호 / 실버 4 / 10분
t=int(input())
for _ in range(t):
  x_str=input()
  arr=[]
  flag='YES'

  for x in x_str:
    if x=='(':
      arr.append(x)
    elif x==')':
      if len(arr)!=0:
        x_pop = arr.pop()
        if x_pop != '(':
          flag='NO'
          break
      else:
        flag='NO'
        break

  if len(arr)!=0:
    flag='NO'

  print(flag)