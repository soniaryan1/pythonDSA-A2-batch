# # comment


# # def add(a, b):
# #     return f"{a}+{b}={a+b}"


# # def sub(a, b):
# #     return f"{a}-{b}={a-b}"


# # first = int(input("Enter your 1st number:- "))
# # second = int(input("Enter your 2nd number:- "))

# # x = add(a=first, b=second)
# # print(x)

# # x = sub(a=first, b=second)
# # print(x)


# def printStatement(name, age):
#     return f"my name is {name}\nmy age is {age}"


# x = input("Enter your name:- ")
# y = int(input("Enter your age:- "))
# print(printStatement(x, y))


# convert int to str
# a = 15
# a = float(a)
# print(a)
# print(type(a))

# Conditional Statements

# if
# if else
# if elif else

# # if
# if 18 < 19:
#     print("small")

# # if else
# if 18 < 10:
#     print("small")
# else:
#     print("Big")

# if elif else

# number = float(input("Enter your Number:- "))
# percent = number / 5
# print(percent)

# if percent > 60 and percent < 100:
#     print("First")
# elif percent > 45 and percent < 60:
#     print("seond")
# elif percent > 30 and percent < 45:
#     print("Third")
# else:
#     print("fail")

# times = float(input("enter your number"))

# if times > 6 and times < 12:
#     print("good morning")

# elif times > 12 and times < 16:
#     print("good afternoon")

# elif times > 16 and times < 20:
#     print("good evening")

# elif times > 20 and times < 24:
#     print("good night")

# else:
#     print("invalid")


# x = input("Enter:- ")
# if x == "yes":
#     print("Train")
# elif x == "no":
#     print("flight")
# else:
#     print("enter yes ya no only")


# operation = input("enter operation :- ")

# if operation == "+":
#     a = float(input("enter your first number :- "))
#     b = float(input("enter your second number :- "))
#     print(a + b)

# elif operation == "-":
#     a = float(input("enter your first number :- "))
#     b = float(input("enter your second number :- "))
#     print(a - b)

# elif operation == "*":
#     a = float(input("enter your first number :- "))
#     b = float(input("enter your second number :- "))
#     print(a * b)

# elif operation == "/":
#     a = float(input("enter your first number :- "))
#     b = float(input("enter your second number :-"))
#     print(a / b)

# else:
#     print("invalid")


# table = int(input("Enter your num:- "))

# for i in range(1, 10 + 1, 1):
#     print(f"{table}X{i}={table*i}")
#     i += 1
table = int(input("enter your number :- "))
for i in range(1, 10 + 1, 1):
    print(f"{table}*{i}={table*i}")
    i += 1
