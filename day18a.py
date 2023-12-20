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


def connected(lines, line):
    result = []

    for item in lines:
        if item == line:
            continue
        if item[0:2] in [line[0:2], line[2:]] or item[2:] in [line[0:2], line[2:]]:
            result.append(item)
    return result


def measure(bmap):
    vmarks = sorted(list(set([x[0] for x in bmap] + [x[2] for x in bmap])))

    print(vmarks)


def plot(lines):
    x = 0
    y = 0
    result = []

    for pdir, dist in lines:
        if pdir == 0:
            result.append([x, y, x + dist, y])
            x += dist
        elif pdir == 1:
            result.append([x, y, x, y + dist])
            y += dist
        elif pdir == 2:
            result.append([x - dist, y, x, y])
            x -= dist
        elif pdir == 3:
            result.append([x, y - dist, x, y])
            y -= dist
    return result


def main():
    part1 = 0
    part2 = 0
    dig = util.lines_from_file(sys.argv[1])
    lines = [[], []]
    maps = []
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

    maps.append(plot(lines[0]))
    maps.append(plot(lines[1]))

    measure(maps[0])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
