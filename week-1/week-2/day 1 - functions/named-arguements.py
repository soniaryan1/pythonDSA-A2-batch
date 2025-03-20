def totalMarks(
    physics: int,
    chemistry: int,
    maths: int,
    computer: int,
    english: int,
    hindi: int,
):

    print(f"{physics = }")
    print(f"{chemistry = }")
    print(f"{maths = }")
    print(f"{computer = }")
    print(f"{english = }")
    print(f"{hindi = }")

    print(f"{physics = }")
    total = physics + chemistry + maths + computer + english + hindi
    print(f"total marks = {total}")


# totalMarks(25, 39, 80, 90, 99, 100)
# totalMarks(hindi=78, english=50, maths=99, computer=98, physics=88, chemistry=77)
# totalMarks(99, 88, computer=88, maths=88, hindi=77, english=99)
totalMarks(55, 79, 87, 97, 87, 56)
