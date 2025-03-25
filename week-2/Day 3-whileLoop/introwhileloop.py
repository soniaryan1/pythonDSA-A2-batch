"""

Loops are two types
1.while
2.for

while condition


"""

# i = 1
# while i <= 10:

#     print(f"{i}.print helloworld")
#     i = i + 1

# i = 1
# table = int(input("Enter table:-"))
# while i <= 10:
#     # print(f"{table}X{i}={table * i}")
#     print(table * i)
#     i = i + 1


i = 1
while i <= 100:
    if i % 5 == 0 and i % 20 != 0:
        # print(i)
        pass
    elif i % 20 != 0:
        print(i, end=" ")

    i = i + 1
