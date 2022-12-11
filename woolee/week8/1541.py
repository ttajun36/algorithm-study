import sys


line = sys.stdin.readline().rstrip()
positive_value = 0
negative_value = 0
status = "plus"
word = ""
for idx in range(len(line)):
    if line[idx] != '+' and line[idx] != '-':
        word += line[idx]
    else:
        if line[idx] == '+' and status == "plus":
            positive_value += int(word)
        elif line[idx] == '-' and status == "plus":
            positive_value += int(word)
            status = "minus"
        elif status == "minus":
            negative_value += int(word)
        word = ""
if status == "plus":
    positive_value += int(word)
else:
    negative_value += int(word)
print(positive_value - negative_value)