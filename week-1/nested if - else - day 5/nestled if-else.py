"""
ask a number from user .
print positive , negative , equal to zero


"""

num = int(input("enter your number = "))

# if num >= 0:
#     if num == 0:
#         print("equal to zero")
#     else:
#         print("positive")
# else:
#     print("negative")
if num > 0:
    print("positive")
else:
    if num == 0:
        print("equal to zero")
    else:
        print("negative")
