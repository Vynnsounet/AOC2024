#!/bin/python3


def parse_input(filename):
    with open(filename, "r") as f:
        matrix = []
        for l in f.readlines():
            matrix.append(list(l.strip()))
        return matrix


def star_pattern(length):
    return [
        [(0, i) for i in range(length)],
        [(0, -i) for i in range(length)],
        [(i, 0) for i in range(length)],
        [(-i, 0) for i in range(length)],
        [(i, i) for i in range(length)],
        [(-i, i) for i in range(length)],
        [(i, -i) for i in range(length)],
        [(-i, -i) for i in range(length)],
    ]


def check_coordinates(coord, matrix):
    x, y = coord
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def is_Xmas(matrix, coords):
    x, y = coords
    diags = [(x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)]

    if matrix[x][y] == "A":
        for coords in diags:
            if not check_coordinates(coords, matrix):
                return False

        if not (
            (matrix[x + 1][y + 1] == "M" and matrix[x - 1][y - 1] == "S")
            or (matrix[x + 1][y + 1] == "S" and matrix[x - 1][y - 1] == "M")
        ):

            return False

        if not (
            (matrix[x - 1][y + 1] == "S" and matrix[x + 1][y - 1] == "M")
            or (matrix[x - 1][y + 1] == "M" and matrix[x + 1][y - 1] == "S")
        ):

            return False

        return True

    return False


def match_pattern(matrix, coordlist, origin, pattern):
    for i, (x, y) in enumerate(coordlist):
        ox, oy = origin
        nx, ny = ox + x, oy + y
        if not (check_coordinates((nx, ny), matrix) and matrix[nx][ny] == pattern[i]):
            return False
    return True


def solve(matrix):
    acc = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for l in star_pattern(4):
                acc += match_pattern(matrix, l, (i, j), "XMAS")
    return acc


def solve2(matrix):
    acc = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            acc += is_Xmas(matrix, (i, j))
    return acc


print(parse_input("day_4_input.txt"))
print(solve(parse_input("day_4_input.txt")))
print(solve2(parse_input("day_4_input.txt")))
