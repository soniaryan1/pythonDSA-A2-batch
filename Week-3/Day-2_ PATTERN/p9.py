"""
* * * * *
  * * *
    *

"""

for i in range(4, 1, -1):
    for j in range(i, 4, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
