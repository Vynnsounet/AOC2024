#!/bin/python3


def parse_input(filename):
    with open(filename, "r") as f:
        m = []
        for l in f.readlines():
            m.append(list(map(int, l.strip())))
        return m


def inbound(coordinates, matrix):
    x, y = coordinates
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def count_trailhead(coordinates, matrix, M):
    i, j = coordinates
    if matrix[i][j] == 9 and (i, j) not in M:
        M.append((i, j))
        return 1

    neighbours = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    res = 0
    for ni, nj in filter(lambda c: inbound(c, matrix), neighbours):
        if matrix[ni][nj] == matrix[i][j] + 1:
            res += count_trailhead((ni, nj), matrix, M)
    return res


def count_trailhead2(coordinates, matrix):
    i, j = coordinates
    if matrix[i][j] == 9:
        return 1

    neighbours = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    res = 0
    for ni, nj in filter(lambda c: inbound(c, matrix), neighbours):
        if matrix[ni][nj] == matrix[i][j] + 1:
            res += count_trailhead2((ni, nj), matrix)
    return res


def solve(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                M = []
                res += count_trailhead((i, j), matrix, M)
    return res


def solve2(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                res += count_trailhead2((i, j), matrix)
    return res


m = parse_input("day_10_input.txt")
for l in m:
    print(l)
print(solve(m))
