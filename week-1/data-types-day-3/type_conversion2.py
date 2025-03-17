"""
int-> bool
 truthy -> 1 ,5 ,8 , -6
 falsey -> 0

float -> bool
 truthy -> 2.4 , 45.35 ,
 falsy -> 0.00


 str -> bool
 truthy -> " " , " . " , "jkfvjjiviji" ,"376487"
 falsy -> ""




"""

# int -> bool
a = bool(5)
print(a)
p = bool(-4)
print(p)
c = bool(0)
print(c)

# float -> bool

b = bool(5.67)
print(b)
x = bool(0.56)
print(x)
d = bool(0.00)
print(d)


# str -> bool
a = bool(" ")
print(a)
b = bool(".")
print(b)
c = bool("")
print(c)
