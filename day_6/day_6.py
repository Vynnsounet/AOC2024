#!/bin/python3


directions = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


def parse_input(filename):
    with open(filename, "r") as f:
        matrix = []
        position = None
        for l in f.readlines():
            matrix.append(list(l.strip()))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] in directions:
                    position = i, j

        return matrix, position


def turn_right(direction):
    match direction:
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"
        case "^":
            return ">"


def in_bound(matrix, position):
    x, y = position
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def next_position(position, direction):
    x, y = position
    i, j = directions[direction]
    return x + i, y + j


def solve(matrix, position):
    positions = [position]
    x, y = position
    d = matrix[x][y]
    position = next_position(position, d)
    while in_bound(matrix, position):
        nx, ny = position
        if matrix[nx][ny] == "#":
            d = turn_right(d)
            position = next_position(positions[-1], d)
        else:
            if position not in positions:
                positions.append(position)
            position = next_position(position, d)
    return len(positions)


matrix, p = parse_input("day_6_input.txt")
print(solve(matrix, p))
