#  10 , 20,30,40,50,60


# def pattern(n: int):
#     i = 1
#     while i <= n:
#         print(i * 10, end=" ")
#         i += 1


# pattern(12)


def pattern(n: int):
    i = 1
    number = 10
    while i <= n:
        print(number, end=" ")
        number = number + 10

        i += 1


pattern(10)
