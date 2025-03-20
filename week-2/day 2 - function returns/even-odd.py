"""
make a fnction named checkoddeven
which take 1 integer as a arguement

if integer is even , then return true
else return false


"""

# def checkoddeven(num: int):
#     if num % 2 == 0:
#         print("true")
#     else:
#         print("false")


# checkoddeven(6)


# def checkoddeven(num: int):
#     if num % 2 == 0:
#         return True
#     return False


# print(checkoddeven(6))
# print(checkoddeven(9))
# print(checkoddeven(1))


def checkoddeven(num: int):
    return num % 2 == 0


print(checkoddeven(6))
print(checkoddeven(9))
print(checkoddeven(1))
