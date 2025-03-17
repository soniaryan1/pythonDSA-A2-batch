# name = "soni"
# age = 20
# gender = "female"
# address = "gisara"

# print("my name is",name ,end=""
# print("my age is",age,end="")
# print("my gender is",gender ,end="")
# print ("my addressis",address)


def printstatement(name, age, gender, address):
    return f" my name is {name}\nmy age is {age}\n my gender is {gender}\n my address is {address}"


x = input("enter your name")
y = int(input("enter your age"))
z = input("enter your gender")
v = input("enter your address")

print(printstatement(x, y, z, v))
