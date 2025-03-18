"""
ask a mark from user . 0 - 100

91-100 -> A
81 - 90 -> B
71 -80 -> C
61 - 70 -> D
0 - 60 -> fail

"""

num: int = int(input("enter your number =  "))

if num >= 91 and num <= 100:
    print("A")
elif num >= 81 and num <= 90:
    print("B")
elif num >= 71 and num <= 80:
    print("C")
elif num >= 61 and num <= 70:
    print("D")
elif num >= 0 and num <= 60:
    print("FAIL")
else:
    print("INVALID MARKS")
