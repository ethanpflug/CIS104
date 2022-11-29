import re

count = 0

expre = input("Enter a regular expression: ")
reg_expre = str(expre)
fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    line = line.rstrip()

    if re.findall(reg_expre, line) != []:
        count += 1
print(fname + " had " + str(count) + ' lines that matched ' + reg_expre)
