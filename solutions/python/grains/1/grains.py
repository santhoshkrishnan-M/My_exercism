def square(square_number):
    if square_number < 1 or square_number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (square_number - 1)


def total():
    return sum(2 ** (square - 1) for square in range(1, 65))