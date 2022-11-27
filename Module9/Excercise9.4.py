dictionary = dict()
maximum = 0
max_address = ''
name = input('Enter file:')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)

for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From:':
        continue

    if words[1] not in dictionary:
        dictionary[words[1]] = 1
    else:
        dictionary[words[1]] += 1
for address in dictionary:
    if dictionary[address] > maximum:
        maximum = dictionary[address]
        max_address = address
print(max_address, maximum)
