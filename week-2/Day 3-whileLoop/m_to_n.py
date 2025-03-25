"""
ask m from user
ask n from user

m to n
n to m

m = 5
n = 10
5
"""

m = int(input("enter m = "))
n = int(input("enter n = "))

if m < n:
    i = m
    while i <= n:
        print(i, end=" ")
        i = i + 1
else:
    i = n
    while i <= m:
        print(i, end=" ")
        i += 1
