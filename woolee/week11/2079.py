import sys
from math import floor


# dp[i]는 word[i]까지의 부분 리스트 중 팰린드롬의 최소 개수
word = sys.stdin.readline().rstrip()
dp = [0] * (len(word) + 1)
# a, b, c 하나만 있어도 팰린드롬 취급
# anaban이면 a => 1 an => 2, ana => 1
# anab => 2, anaba => a, n, aba or ana, b, a anaban => a, naban
# dp[i] 는 dp[0]부터 dp[i-1] 값과 나머지 문자열이 팰린드롬인지를 확인하여
# 가장 작은 값을 대입하면 될 듯



for right in range(1, len(word)+1): # subword의 길이
    minimum = sys.maxsize # int 최대 값
    # 일단 전체가 펠린드롬인지 체크
    subword = word[:right]
    found = 1
    for idx in range(floor(right / 2)):
        if subword[idx] != subword[-1-idx]:
            found = 0
            break
    if found == 0:
        minimum = sys.maxsize
        for j in range(1, right):
            # a (navolimilana), an avolimilana, ana volimilana...
            found = 1
            subword = word[j:right]
            # print(word[:j], subword)
            for idx in range(floor(len(subword) / 2)):
                if subword[idx] != subword[-1-idx]:
                    found = 0
                    break
            if found == 1:
                minimum = min(minimum, dp[j] + 1)
            else:
                minimum = min(minimum, dp[j] + len(subword))
        dp[right] = minimum
    else:
        dp[right] = 1
print(dp[-1])