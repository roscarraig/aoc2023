#!/usr/bin/env python3

import util
import sys


def beam(x, y, bdir, cave, seen):
    while True:
        if x < 0 or y < 0 or x >= len(cave[0]) or y >= len(cave):
            return
        if (x, y) in seen:
            if seen[(x, y)] & bdir:
                return
            seen[(x, y)] |= bdir
        else:
            seen[(x, y)] = bdir

        if cave[y][x] == '.':
            if bdir == 1:
                x += 1
            elif bdir == 2:
                y += 1
            elif bdir == 4:
                x -= 1
            elif bdir == 8:
                y -= 1
        elif cave[y][x] == '\\':
            if bdir == 1:
                bdir = 2
                y += 1
            elif bdir == 2:
                bdir = 1
                x += 1
            elif bdir == 4:
                bdir = 8
                y -= 1
            elif bdir == 8:
                bdir = 4
                x -= 1
        elif cave[y][x] == '/':
            if bdir == 1:
                bdir = 8
                y -= 1
            elif bdir == 2:
                bdir = 4
                x -= 1
            elif bdir == 4:
                bdir = 2
                y += 1
            elif bdir == 8:
                bdir = 1
                x += 1
        elif cave[y][x] == '|':
            if bdir in [1, 4]:
                beam(x, y - 1, 8, cave, seen)
                bdir = 2
                y += 1
            elif bdir == 2:
                y += 1
            elif bdir == 8:
                y -= 1
        elif cave[y][x] == '-':
            if bdir in [2, 8]:
                beam(x - 1, y, 4, cave, seen)
                bdir = 1
                x += 1
            elif bdir == 1:
                x += 1
            elif bdir == 4:
                x -= 1


def main():
    part1 = 0
    part2 = []
    cave =  [x.strip() for x in util.lines_from_file(sys.argv[1])]
    h = len(cave)
    w = len(cave[0])
    seen = {}
    beam(0, 0, 1, cave, seen)
    part1 = len(seen)
    res = ''
    for j in range(len(cave)):
        for i in range(len(cave[0])):
            if (i, j) in seen:
                res += '#'
            else:
                res += ' '
            res += cave[j][i]
        res += "\n"

    for i in range(w):
        seen = {}
        beam(i, 0, 2, cave, seen)
        part2.append(len(seen))
        seen = {}
        beam(i, h - 1, 8, cave, seen)
        part2.append(len(seen))
    for i in range(h):
        seen = {}
        beam(0, i, 1, cave, seen)
        part2.append(len(seen))
        seen = {}
        beam(w - 1, i, 4, cave, seen)
        part2.append(len(seen))

    print(f"Part 1: {part1}")
    print(f"Part 2: {max(part2)}")


if __name__ == '__main__':
    main()
