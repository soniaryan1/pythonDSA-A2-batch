# make a function named checkoddeven which takes a integer as a arguement
# if even ,print EVEN , else print ODD


# def checkOddEven():
#     if num % 2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")


# num: int = int(input("enter your num = "))
# checkOddEven()
def checkOddEven(num: int):
    if num % 2 == 0:
        print(f"{num}is a even number")
    else:
        print(f"{num} is a odd number")


checkOddEven(3)
