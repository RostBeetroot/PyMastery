text = input("Enter random numbers: ")

for char in range(len(text)):
    if not char % 3 == 0:
        print(text[char], end="")
