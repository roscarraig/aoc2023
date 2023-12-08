#!/usr/bin/env python3

import util
import sys
from math import lcm


def turnind(dir):
    if dir == 'L':
        return 0
    return 1


def main():
    map = {}
    part1 = 0
    part2i = 0
    lines = util.lines_from_file(sys.argv[1])
    turns = lines[0].strip()
    tlen = len(turns)
    pos = 'AAA'
    transit = True
    pmap = {}

    for line in lines[2:]:
        map[line[0:3]] = [line[7:10], line[12:15]]

    while pos != 'ZZZ':
        pos = map[pos][turnind(turns[part1%tlen])]
        part1 += 1

    print(f"Part 1: {part1}")
    mpos = []
    land = []

    for item in map:
        if item[2] == 'A':
            mpos.append(item)
            land.append(0)

    while transit:
        transit = False
        d = turnind(turns[part2i%tlen])
        part2i += 1
        for i in range(len(mpos)):
            mpos[i] = map[mpos[i]][d]
            if mpos[i][2] != 'Z':
                transit = True
            else:
                if land[i] == 0:
                    land[i] = part2i
        if len([x for x in land if x]) == len(mpos):
            break

    print(f"Part 2: {lcm(*land)}")


if __name__ == '__main__':
    main()
