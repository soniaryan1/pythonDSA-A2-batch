#  BREAK , CONTINUE

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1


# ..
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i, end=" ")

#     i += 1


# i = 1
# while i <= 10:
#     print(i, end=" ")

#     i += 1
#     if i == 5:
#         break

# i = 0
# while i <= 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i, end=" ")
#     print("done", end=" ")


i = 1
while i <= 10:
    print(i, end=" ")
    if i == 5:
        continue
    i += 1
print("done")
