import sys


sentence = sys.stdin.readline().rstrip()
sub = sys.stdin.readline().rstrip()
count = 0
while sub in sentence:
    sentence = sentence[sentence.find(sub)+len(sub):]
    count += 1
print(count)