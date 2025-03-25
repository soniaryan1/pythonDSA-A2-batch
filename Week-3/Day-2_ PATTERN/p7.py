"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

# for i in range(1, 6, 1):
#     for j in range(i, 5, 1):
#         print(" ", end=" ")
#     for k in range(1, i * 2):
#         print("*", end=" ")
#     print()

for i in range(1, 6, 1):
    for j in range(i, 5, 1):
        print(" ", end=" ")
    for k in range(1, i + 1, 1):
        print("*", end=" ")
    for l in range(1, i, 1):
        print("*", end=" ")
    print()
