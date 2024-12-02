#!/bin/python3


def parse_input(filename):
    l1, l2 = [], []
    with open(filename, "r") as f:
        for e in f.readlines():
            el1, el2 = e.split("   ")
            el1, el2 = int(el1), int(el2)
            l1.append(el1)
            l2.append(el2)
    return l1, l2


def solve_1(l1, l2):
    res = 0
    for el1, el2 in zip(sorted(l1), sorted(l2)):
        res += abs(el1 - el2)
    return res


def solve_2(l1, l2):
    res = 0
    for e in l1:
        res += e * l2.count(e)
    return res


l1, l2 = parse_input("day_1_input.txt")
print(f"{solve_1(l1, l2):=}")
print(f"{solve_2(l1, l2):=}")
