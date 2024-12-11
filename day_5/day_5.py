#!/bin/python3


class DGraph:

    def __init__(self, n, labels=None) -> None:
        self.deg = n
        if labels:
            self.labels = labels
        self.adj = [[] for _ in range(n)]

    def add_edge(self, l1, l2):
        i1, i2 = self.labels.index(l1), self.labels.index(l2)
        self.adj[i1].append(i2)


def parse_input(filename):
    edges, lists = [], []
    labels = set()
    b = False
    with open(filename, "r") as f:
        for l in f.readlines():
            if l == "\n":
                b = True
            if b:
                lists.append(l.strip().split())
            else:
                curr = l.strip().split("|")
                for e in curr:
                    labels.add(e)
                edges.append(curr)
    G = DGraph(len(labels), list(labels))
    for e in edges:
        G.add_edge(*e)

    return G, lists


parse_input("day_5_input.txt")
