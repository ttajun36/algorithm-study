"""
p 1 0 2
s 0 2 1

"""

from collections import defaultdict


n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

collect_cards = defaultdict(list)

for i in range(n):
    collect_cards[p[i]].append(i)

init = [i for i in range(n)]
shuffle = init[:]
count = 0
# print(collect_cards)

while True:
    # print(shuffle)

    finish = True
    for i in range(n):
        if shuffle[i] not in collect_cards[i % 3]:
            finish = False

    if finish:
        break

    new_shuffle = shuffle[:]
    for i in range(n):
        new_shuffle[s[i]] = shuffle[i]

    count += 1
    shuffle = new_shuffle[:]

    if init == shuffle:
        count = -1
        break

print(count)
