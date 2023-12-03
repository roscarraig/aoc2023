#!/usr/bin/env python3

import sys

import util


def adjacent(i, j, x1, x2, y):
    if i in range(x1 - 1, x2 + 2) and j in range(y - 1, y + 2):
        return True
    return False


def isbeside(design, x1, x2, y, w, h):
    exclude = util.digits + ['.']
    box = ''
    if x1 > 0:
        i1 = x1 - 1
    else:
        i1 = x1
    if x2 < w - 1:
        i2 = x2 + 1
    else:
        i2 = x2
    if y > 0:
        j1 = y - 1
    else:
        j1 = y
    if y < h - 1:
        j2 = y + 1
    else:
        j2 = y
    for j in range(j1, j2 + 1):
        box += design[j][i1:i2 + 1]
    for c in exclude:
        box = box.replace(c, '')
    if '*' in box:
        return 2
    elif len(box) > 0:
        return 1
    return 0


def main():
    part1 = 0
    part2 = 0
    design = [x.strip() for x in util.lines_from_file(sys.argv[1])]
    h = len(design)
    w = len(design[0])
    gears = []

    for y in range(h):
        x = 0
        while x < w:
            if design[y][x] in util.digits:
                t = int(design[y][x])
                x1 = x
                x += 1
                while x < w and design[y][x] in util.digits:
                    t *= 10
                    t += int(design[y][x])
                    x += 1
                x2 = x - 1
                v = isbeside(design, x1, x2, y, w, h)
                if v:
                    part1 += t
                if v == 2:
                    gears.append([t, x1, x2, y])
            else:
                x += 1
    for y in range(h):
        x = 0
        while x < w and '*' in design[y][x:]:
            x += design[y][x:].index('*')
            count = 0
            product = 1
            for item in gears:
                if adjacent(x, y, item[1], item[2], item[3]):
                    count += 1
                    product *= item[0]
            if count == 2:
                part2 += product
            x += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
