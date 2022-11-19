handle = open('cheeses.txt')

cheeses = []
for line in handle:
    linecheeses = line.split()
    for cheese in linecheeses:
        cheeses.append(cheese)

cheeses.sort()
print(cheeses)
