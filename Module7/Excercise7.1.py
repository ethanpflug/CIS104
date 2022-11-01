with open('mbox-short.txt') as fname:
    for line in fname:
        line = line.rstrip()
        print(line.upper())
