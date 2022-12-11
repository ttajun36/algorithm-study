import sys


N = int(sys.stdin.readline().rstrip())
times = map(int, sys.stdin.readline().rstrip().split(" "))
total_time = 0
# 합의 최솟 값 구하기
# 1 2 3 4 5 => 1+ 1+2 + 1+2+3 + 1+2+3+4 + 1+2+3+4+5
# 5 4 3 2 1 => 5+ 5+4 + 5+4+3 ... 5+4+3+2+1
# 가장 작은 수가 자주 더해져야하고
# 가장 큰수가 가장 드물게 더해져야한다
# 오름차순으로 정렬하고 맨 끝에서 하나씩 빼면서 더하면됨
times = sorted(times)
while True:
    if len(times) == 0:
        break
    total_time += sum(times)
    times.pop()
print(total_time)