"""

requirments to get a certificate
 1. should be part of c&d
 2. minimum class attended should be 20
 3. minimum assignment submitted = 45



 are you part of c&d = yes
 enter class attended =
 enter assignment submitted =
 you are eligible for certificate

"""

user_input = input("are you a part of c&d: (yes/no) = ")
if user_input == "yes":
    user_input_class = int(input("enter number of class attended = "))
    if user_input_class >= 20:
        user_input_assignment = int(input("enter number of submitted assignment = "))
        if user_input_assignment >= 45:
            print("you are eligible for certificate")
        else:
            print("you are not eligible for certificate")
    else:
        print("you are not eligible for certificate")
else:
    print("you are not eligible for certificate")
