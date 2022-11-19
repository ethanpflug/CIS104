name = input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    wlist = line.split()
    if line.startswith("From "):
        date = wlist[2]
        counts[date] = counts.get(date, 0) + 1
print (counts)
