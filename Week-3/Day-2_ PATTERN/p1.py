"""
@ @ @ @ *
@ @ @ * *
@ @ * * *
@ * * * *
* * * * *

"""

# for i in range(5, 0, -1):
#     for j in range(i, 1, -1):
#         print("@", end=" ")
#     for k in range(6 - i):
#         print("*", end=" ")
#     print()

for i in range(1, 6, 1):
    for j in range(i, 5, 1):
        print(" ", end=" ")
    for k in range(1, i + 1, 1):
        print(k, end=" ")
    print()
