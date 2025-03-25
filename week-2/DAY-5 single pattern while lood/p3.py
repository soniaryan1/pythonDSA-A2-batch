# 1  11 111 1111 11111


def pattern(n: int):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = num * 10 + 1
        i += 1


pattern(10)
