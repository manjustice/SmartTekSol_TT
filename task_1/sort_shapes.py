import math


def calculate_area(shape: list | tuple | int | float) -> float:
    if isinstance(shape, (list, tuple)):
        return shape[0] * shape[1]
    if isinstance(shape, (int, float)):
        return math.pi * (shape ** 2)

    raise ValueError(f"{type(shape)} is not the right shape")


def sort_shapes_by_area(shapes: list) -> list:
    return sorted(shapes, key=calculate_area)


if __name__ == "__main__":
    sequence = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
    right_sequence = [[1.342, 3.212], 1.23, [4.23, 6.43], 3.444]

    assert sort_shapes_by_area(sequence) == right_sequence
