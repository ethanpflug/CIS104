import re

hand = open('regex_sum_1648170.txt')
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall('([0-9]+)', line)

    if len(extract) < 1:
        continue

    for i in range(len(extract)):
        num = int(extract[i])
        numlist.append(num)

print(sum(numlist))

