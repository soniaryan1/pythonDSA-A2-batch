def circle(radius: float) -> float:
    return 3.14 * radius * radius


def reactangle(length: float = 9, bredth: float = 9) -> None:
    print(length * bredth)


def triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def square(side: float) -> float:
    return side**2


print(dir())
if __name__ == "__main__":
    print(square(100))
