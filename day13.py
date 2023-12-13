#!/usr/bin/env python3

import util
import sys


def findsym(pattern, smudge=0):
    w = len(pattern[0])
    w2 = w // 2
    h = len(pattern)

    for i in range(1, w):
        if i <= w2:
            if len([j for j in range(h) if pattern[j][:i] != pattern[j][2 * i - 1:i - 1:-1]]) == smudge:
                return i
        else:
            if len([j for j in range(h) if pattern[j][2 * i - w:i] != pattern[j][w - 1: i - 1: -1]]) == smudge:
                return i
    return 0


def main():
    patterns = []
    pattern = []
    hcount = 0
    vcount = 0
    hcount2 = 0
    vcount2 = 0

    for line in util.lines_from_file(sys.argv[1]):
        if line.strip() == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())

    patterns.append(pattern)

    for pattern in patterns:
        res = findsym(pattern)
        hcount += res
        if not res:
            res = findsym(util.flip(pattern))
            vcount += res
        res = findsym(pattern, 1)
        hcount2 += res
        if not res:
            res = findsym(util.flip(pattern), 1)
            vcount2 += res

    print(f"Part 1: {hcount + 100 * vcount}")
    print(f"Part 2: {hcount2 + 100 * vcount2}")


if __name__ == '__main__':
    main()
