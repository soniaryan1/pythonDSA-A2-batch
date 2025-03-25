# 1 3 6 8 11 13 16 18 21 23 ...upto n numbers


def pattern(n: int):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        if i % 2 == 0:
            num = num + 3
        else:
            num = num + 2
        i += 1


pattern(10)
