"""
(((()())(())()))(())


쇠막대기 사이에 있는 레이저 개수를 스택에 저장

1. (는 그냥 스택에 추가
2. )를 만나면 스택에서 (를 만날 때 까지 pop
    - 그냥 ()일 경우에는 레이저이므로 스택에 레이저 개수 1 추가
    - () 사이에 다른 게 더 있다면 쇠막대기이므로 그 사이에 있는 레이저 개수를 더하고 그 개수를 다시 스택에 추가
    
3. 나눠진 막대기 개수는 쇠막대기 사이에 있는 레이저 개수 + 1 를 계속 더해주면 됨

ex)
((()())())

((() -> ((1               // 레이저 -> count 그대로
((()() -> ((11            // 레이저 -> count 그대로
((()()) -> ((11) -> (2    // 막대기 -> 사이에 레이저 개수가 2개니까 count 3증가
((()())() -> (21 ->       // 레이저 -> count 그대로
((()())()) -> (21) -> 3   // 막대기 -> 사이에 레이저 개수가 3개니까 count 4증가

"""


from collections import deque

parentheses = input()

dq = deque()

total_count = 0
for parenthesis in parentheses:
    count = 0

    # (일 경우에 그냥 스택에 추가
    if parenthesis == "(":
        dq.append(parenthesis)

    # )일 경우에
    elif parenthesis == ")":

        # (를 만날 때 까지 pop
        while True:
            elem = dq.pop()
            if elem == "(":
                # 레이저의 끝이었으면
                if count == 0:
                    dq.append(1)  # count는 증가하지 않고 사이에 있는 레이저 개수 1추가

                # 막대기의 끝이었으면
                else:
                    dq.append(count)  # 그 사이에 있던 레이저 개수 다 더해서 스택에 추가

                    # 사이에 레이저 개수가 2개면 3개로 나눠지니까 +1
                    total_count += count + 1
                break
            else:
                count += elem  # 막대기 사이에 있는 레이저 개수 계산


print(total_count)
