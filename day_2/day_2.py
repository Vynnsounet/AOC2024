#!/bin/python3


def parse_input(filename):
    reports = []
    with open(filename, "r") as f:
        for e in f.readlines():
            reports.append(list(map(int, e.split())))
    return reports


def check_report2(report):
    i = 0
    while i < len(report) - 1 and report[i] < report[i + 1]:
        if abs(report[i] - report[i + 1]) > 3:
            return False

    if i <= len(report) - 1:
        return False

    i = 0
    while i < len(report) - 1 and report[i] > report[i + 1]:
        if abs(report[i] - report[i + 1]) > 3:
            return False

    return i <= len(report) - 1


def check_report(report):
    sorted_report = list(sorted(report))
    rsorted_report = list(reversed(sorted_report))
    if report == sorted_report or report == rsorted_report:
        for i in range(len(report) - 1):
            if (e := abs(report[i] - report[i + 1])) < 1 or e > 3:
                return False
        return True
    return False


def solve_1(reports):
    res = 0
    for l in reports:
        res += check_report(l)
    return res


def solve_2(l1, l2):
    res = 0
    for e in l1:
        res += e * l2.count(e)
    return res


l1, l2 = parse_input("day_1_input.txt")
print(f"{solve_1(l1, l2):=}")
# print(f"{solve_2(l1, l2):=}")
