"""
enter a number = 64
enter a number = 30
enter a number = 54
enter a number = 33
enter a number = 34
enter a number = 0


"""

total = 0
while True:
    number = int(input("enter a number = "))
    if number == 0:
        break
    total += 1

print(total)
