"""
ask a number from user.


if div by 3 -> foo
if div by 5 -> bar
if div by both 3 and 5 -> foobar
foofoobarbar



"""

num = float(input("enter your number = "))

if num % 3 == 0 and num % 5 == 0:
    print("foobar")
elif num % 3 == 0:
    print("foo")
elif num % 5 == 0:
    print("bar")
else:
    print("foofoobarbar")

# foobaar
