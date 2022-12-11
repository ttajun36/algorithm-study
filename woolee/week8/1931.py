import sys

MAX_INT = 2**31 - 1
N = int(sys.stdin.readline().rstrip())
meeting_list = list()
for _ in range(N):
    meeting = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    meeting.append(meeting[1] - meeting[0])
    meeting_list.append(meeting)
meeting_list.sort(key=lambda x : (x[0], x[2]))
# print(meeting_list)

# 시작 지점 부터 weight가 가장 작은 회의를 진행함
# 처음 시작 지점은 0.
# weight는 시작지점과 시작시간의 차이 + 회의 시간
start = 0
start_idx = -1
count = 0
while True:
    weight = MAX_INT
    # 루프가 한번 돌면, 다음으로 선택된 회의가 새로운 시작지점이 됨.
    # 어느 지점에서 시작지점부터 풀회의를 한 가중치보다 한시간만 했는데도 가중치가 더 크게나옴
    for idx in range(start_idx + 1, len(meeting_list)):
        meeting = meeting_list[idx]
        # 이미 찾은 게 있는데 거리가 weight보다 크다 => 더 이상 찾을 필요가 없음
        if meeting[0] - start > weight:
            break
        if meeting[0] < start:
            continue
        value = meeting[0] - start + meeting[2]
        if weight > value:
            weight = value
            start_idx = idx
        elif weight == value:
            continue
    # weight 값이 변하지 않으면 회의를 선택 못한 것으로 판단.
    # 더 이상 회의를 진행할 수 없으므로 루프를 종료
    if weight == MAX_INT:
        break
    else:
        # print(meeting_list[start_idx])
        start = meeting_list[start_idx][1] # 가장 가치있는 판단을 한 미팅의 종료 시점을 시작지점으로
        count += 1
print(count)