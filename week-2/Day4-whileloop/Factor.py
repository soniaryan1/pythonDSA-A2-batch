# def factor(n: int) -> None:
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             print(i, end=" ")
#         i = i + 1


# print(factor(15))


def factor(n: int) -> None:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count = count + 1
        i = i + 1
    return count


print(factor(20))


def isprime(n: int) -> bool:
    if factor(n) != 2:
        return fa
    return True


number = 5
if isprime(number) == True:
    print("it is a prime number")
else:
    print("it is not a prime number")
