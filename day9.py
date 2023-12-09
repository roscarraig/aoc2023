#!/usr/bin/env python3

import util
import sys


def rownext(line):
    rows = [[int(x) for x in line.strip().split(" ")]]

    while set(rows[-1]) != set([0]):
        rows.append([rows[-1][i + 1] - rows[-1][i] for i in range(len(rows[-1]) - 1)])

    rows[-1].append(0)
    rows[-1].insert(0, 0)

    for j in range(len(rows) - 2, -1, -1):
        rows[j].append(rows[j][-1] + rows[j + 1][-1])
        rows[j].insert(0, rows[j][0] - rows[j + 1][0])

    return rows[0][0], rows[0][-1]


def main():
    part1 = 0
    part2 = 0

    for line in util.lines_from_file(sys.argv[1]):
        a, b = rownext(line)
        part1 += b
        part2 += a

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
