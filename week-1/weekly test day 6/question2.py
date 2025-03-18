"""
given three angles of a triangle , determine whether it is an acute , obtuse , or right angled triangle .


"""

angle1: float = float(input("enter the first angle in degrees = "))
angle2: float = float(input("enter the second angle in degrees = "))
angle3: float = float(input("enter the third angle in degrees = "))

sum_of_angles = angle1 + angle2 + angle3

# check the type of triangle

if sum_of_angles == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        triangle_type = "right-angled"
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        triangle_type = "acute-angled"
    else:
        triangle_type = "obtuse-angled"
    print(f"the triangle is {triangle_type}")
else:
    print("invalid , sum of angles in a triangle should be 180 degrees")
