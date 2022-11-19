name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    wlist = line.split()
    if line.startswith('From:'):
        name = wlist[1]
        counts[name] = counts.get(name,0) + 1

bigcount = -1
bigword = None
for word,count in counts.items():
    if bigcount is 0 or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)
