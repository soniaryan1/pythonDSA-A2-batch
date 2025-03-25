# 1 2 4  816 32 64 128 ...uto n times


def pattern(n: int):
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = number * 2
        i += 1


pattern(3)
