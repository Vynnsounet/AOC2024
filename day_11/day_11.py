#!/bin/python3

input = [890, 0, 1, 935698, 68001, 3441397, 7221, 27]
ex_input = [125, 17]
ex2_input = [0, 1, 10, 99, 999]


def split_number(input, i):
    c = str(input[i])
    fh, lh = int(c[: len(c) // 2]), int(c[len(c) // 2 :])
    input[i] = lh
    input.insert(i, fh)


def apply_rules(input):
    numbers_to_split = []

    for i in range(len(input)):
        if input[i] == 0:
            input[i] = 1
        elif len(str(input[i])) % 2 == 0:
            numbers_to_split.append(i)
        else:
            input[i] *= 2024

    for i in range(len(numbers_to_split)):
        split_number(input, numbers_to_split[i])
        for j in range(len(numbers_to_split)):
            numbers_to_split[j] += 1


def solve(input):
    for _ in range(75):
        apply_rules(input)


solve(input)
print(len(input))
