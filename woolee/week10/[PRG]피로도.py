k = 80
dungeons = [[100, 30], [80,20], [30, 10], [40,40],[30,10]]

def search(k, taken, dungeons, count):
    if k <= 0:
        return count
     
    found = 0
    for dungeon in dungeons:
        if k >= dungeon[0]:
            found = 1
            break
    if found == 0:
        return count
     

    ret = 0
    for idx in range(len(dungeons)):
       if dungeons[idx][0] <= k and taken[idx] == 0:
          taken[idx] = 1
          print(taken)
          ret = max(ret, search(k - dungeons[idx][1], taken, dungeons, count + 1))
          taken[idx] = 0
    return ret
    
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key=lambda x : -x[0])
    answer = search(k, [0] * len(dungeons), dungeons, 0)
    return answer

print(solution(k, dungeons))