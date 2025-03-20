# print 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i = i + 1


#  print 1 to n
# ask n from user

# i: int = 1
# n = int(input("enter n = "))
# while i <= n:
#     print(i, end=" ")
#     i = i + 1


def printPattern(n: int) -> None:
    i: int = 1

    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()


printPattern(5)
printPattern(10)
printPattern(15)
printPattern(20)
