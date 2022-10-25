fruit = input("Enter a fruit:")
index = -1
frlen = len(fruit) * -1

while True:
    if index == frlen - 1:
        break
    letter = fruit[index]
    print(letter)
    index = index - 1
