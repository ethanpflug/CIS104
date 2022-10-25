text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')

numpos2 = text.find('5',numpos)


numpos3 = float(text[numpos:numpos2 + 1])
print(numpos3)
