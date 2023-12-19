#!/usr/bin/env python3

import util
import sys


def scope(head, items):
    x = 0
    y = 0
    xl = [0]
    yl = [0]
    turns = 0
    print(head)

    for item in items:
        dir = item[0]
        dist = item[1]

        if dir == 0:
            turns += [0, -1, 0, 1][head]
            x += dist
            xl.append(x)
            head = dir
        elif dir == 1:
            turns += [1, 0, -1, 0][head]
            y += dist
            yl.append(y)
            head = dir
        elif dir == 2:
            turns += [0, 1, 0, -1][head]
            x -= dist
            xl.append(x)
            head = dir
        elif dir == 3:
            turns += [-1, 0, 1, 0][head]
            y -= dist
            yl.append(y)
            head = dir

    return [-min(xl), -min(yl), max(xl) - min(xl), max(yl) - min(yl), turns]


def main():
    part1 = 0
    part2 = 0
    dig = util.lines_from_file(sys.argv[1])
    lines = [[], []]
    head = None

    for line in dig:
        parts = line.strip().split(' ')
        dist1 = int(parts[1])
        dir1 = 'RDLU'.index(parts[0])
        dir2 = int(parts[2][7])
        if not head:
            head = [dir1, dir2]
        dist2 = int(parts[2][2:7], 16)
        lines[0].append([dir1, dist1])
        lines[1].append([dir2, dist2])

    print(scope(head[0], lines[0]))
    print(scope(head[1], lines[1]))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
