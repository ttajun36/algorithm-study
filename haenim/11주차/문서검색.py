"""
문서와 검색하려는 단어가 주어졌을 때, 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.

abababa

"""

import re

s = input()
target = input()

max_count = 0
for i in range(len(s)):
    count = len(re.findall(target, s[i:]))
    if max_count < count:
        max_count = count

print(max_count)
