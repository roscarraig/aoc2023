#!/usr/bin/env python3

import util
import sys


def dists(gal):
    result = 0
    for i in range(len(gal)):
        for j in range(i + 1, len(gal)):
            result += abs(gal[i][0] - gal[j][0]) + abs(gal[i][1] - gal[j][1])
    return result


def main():
    gal = []
    gal2 = []
    space = 0
    part1 = 0
    exp = 999999
    lines = util.lines_from_file(sys.argv[1])

    for j in range(len(lines)):
        if '#' not in lines[j]:
            space += 1
            continue
        off = 0

        while '#' in lines[j][off:]:
            off += lines[j][off:].index('#')
            gal.append([off, j + space])
            gal2.append([off, j + space * exp])
            off += 1

    w = len(lines[0].strip())
    h = len(lines)
    hor = [i for i in range(w) if [j for j in range(h) if lines[j][i] == '#'] == []]

    for i in range(len(gal)):
        for j in hor[::-1]:
            if gal[i][0] > j:
                gal[i][0] += 1
                gal2[i][0] += exp

    print(f"Part 1: {dists(gal)}")
    print(f"Part 2: {dists(gal2)}")


if __name__ == '__main__':
    main()
