"""
ask a number from user = 50
 - 50 to 50

ask a number from user = 10
-10 to 10


ask a number from user = -13
13 to -13

ask a number from user = -20
20 to -20

"""

number: int = int(input("enter a number = "))
start = -number
end = number

if number > 0:
    start = -number
    end = number
    while start <= end:
        print(start, end=" ")
        start += 1
else:
    start = -number
    end = number
    while start >= end:
        print(start, end=" ")
        start -= 1
