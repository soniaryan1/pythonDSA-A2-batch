"""

make 2 functions.
add() - it will take 3 intigers - return the additional

checkoddeven()- it will take 1 integer , check if odd or even

"""


def add(num1: int, num2: int, num3: int):
    total = num1 + num2 + num3
    return total


def checkoddeven(num: int):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")


t = add(2, 6, 4)
checkoddeven(t)
