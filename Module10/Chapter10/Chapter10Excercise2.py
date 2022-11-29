dictonary = dict()
lst = list()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue
    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dictonary:
        dictonary[hour] = 1
    else:
        dictonary[hour] += 1

            
for key, val in list(dictonary.items()):
    lst.append((key, val))

lst.sort()                             

for key, val in lst:
    print(key, val)
