from sys import stdin


word = stdin.readline().rstrip()
count = 0
idx = 0
while True:
    if idx > len(word) - 1:
        print(count)
        break
    else:
        if word[idx] == 'c':
            if idx + 1 < len(word) and word[idx + 1] == "=":
                count += 1
                idx += 2
            elif idx + 1 < len(word) and word[idx + 1] == "-":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        elif word[idx] == 'd':
            if idx + 2 < len(word) and word[idx + 1] == "z" and word[idx + 2] == "=":
                count += 1
                idx += 3
            elif idx + 1 < len(word) and word[idx + 1] == "-":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        elif word[idx] == 'l':
            if idx + 1 < len(word) and word[idx + 1] == "j":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        elif word[idx] == 'n':
            if idx + 1 < len(word) and word[idx + 1] == "j":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        elif word[idx] == 's':
            if idx + 1 < len(word) and word[idx + 1] == "=":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        elif word[idx] == 'z':
            if idx + 1 < len(word) and word[idx + 1] == "=":
                count += 1
                idx += 2
            else:
                count += 1
                idx += 1    
        else:
            count += 1
            idx += 1