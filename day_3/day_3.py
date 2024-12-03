#!/bin/python3

import re


def mul(x, y):
    return x * y


def solve(filename):
    with open(filename, "r") as f:
        expressions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", f.read())
        return sum([eval(expr) for expr in expressions])


def solve2(filename):
    with open(filename, "r") as f:
        expressions = re.findall(
            r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do(n't)?\(\))", f.read()
        )
        ex, acc = True, 0
        for elm in expressions:
            match elm:
                case _, "do()", _:
                    ex = True
                case _, "don't()", _:
                    ex = False
                case expr, _, _:
                    if ex:
                        acc += eval(expr)
        return acc


print(solve("day_3_input.txt"))
print(solve2("day_3_input.txt"))
