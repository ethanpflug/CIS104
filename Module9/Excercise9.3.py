name = input("Enter file:")
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
dictionary = dict()

for line in handle:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary:
            dictionary[words[2]] = 1
        else:
            dictionary[words[2]] +=1
print (dictionary)
