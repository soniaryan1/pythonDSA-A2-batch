"""
ask m and n from user .
print m to n.

"""

m: int = int(input(" enter your m number = "))
n: int = int(input(" enter your n number = "))

i: int = m
while i <= n:
    print(i, end=" ")
    i = i + 1
