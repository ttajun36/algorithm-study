#2346 [BOJ] 풍선터트리기 / 실버3 / 30분
n=int(input())
arr = list(map(int,input().split()))
result = []
idx =0

index = [ x for x in range(1,n+1)]

temp = arr.pop(0)
result.append(index.pop(idx))

while arr : 
  if temp < 0:
    idx= (idx+temp)% len(arr)
  else:
    idx = (idx + (temp -1)) % len(arr)
  temp = arr.pop(idx)
  result.append(index.pop(idx))

for i in result:
  print(i, end= ' ')
