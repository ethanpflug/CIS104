dictionary = dict()
lst = list()
fname = input('Enter file name:')
handle = open(fname)

for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary:
            dictionary[words[1]] = 1
        else:
            dictionary[words[1]] += 1

for key, val in list(dictionary.items()):
    lst.append((val, key))
lst.sort(reverse = True)
for val, key in lst[:1] :
    print(key, val)
