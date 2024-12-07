#!/bin/python3


def parse_input(filename):
    d = {}
    with open(filename, "r") as f:
        for l in f.readlines():
            key, values = l.strip().split(":")
            d[int(key)] = list(map(int, values.split()))
    return d


def __is_result2(numbers, possible_results, acc):
    if numbers:
        __is_result2(numbers[1:], possible_results, acc * numbers[0])
        __is_result2(numbers[1:], possible_results, acc + numbers[0])
        __is_result2(numbers[1:], possible_results, int(str(acc) + str(numbers[0])))
    else:
        possible_results.append(acc)


def __is_result(numbers, possible_results, acc):
    if numbers:
        __is_result(numbers[1:], possible_results, acc * numbers[0])
        __is_result(numbers[1:], possible_results, acc + numbers[0])
    else:
        possible_results.append(acc)


def is_result(goal, numbers):
    res = []
    __is_result(numbers[1:], res, numbers[0])
    return goal in res


def is_result2(goal, numbers):
    res = []
    __is_result2(numbers[1:], res, numbers[0])
    return goal in res


def solve(filename):
    d = parse_input(filename)
    res = 0
    for k, v in d.items():
        if is_result(k, v):
            res += k
    return res


def solve2(filename):
    d = parse_input(filename)
    res = 0
    for k, v in d.items():
        if is_result2(k, v):
            res += k
    return res


print(solve("day_7_input.txt"))
print(solve2("day_7_input.txt"))
