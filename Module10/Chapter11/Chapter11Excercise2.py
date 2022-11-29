import re

rev = []
avg_rev = 0

fname = input("Enter a file: ")
handle = open(fname)

for line in handle:
    line = line.rstrip()
    rev_hold = re.findall('^New Revision: ([0-9.]+)', line)
    for val in rev_hold:
        val = int(val)
        rev = rev + [val]
revsum = sum(rev)
count = int(len(rev))
if count:
    avg_rev = revsum / count
    average = int(avg_rev)
print(average)
