def circle(radius: float) -> float:
    return 3.14 * radius * radius


def reactangle(length: float = 9, bredth: float = 9) -> None:
    return length * bredth


def triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def square(side: float) -> float:
    return side**2


print(reactangle(2, 4))
print(square(4))
