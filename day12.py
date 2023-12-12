#!/usr/bin/env python3

import util
import sys

already = {}


def ways(conds, lens):
    global already
    point = tuple([conds, len(lens)])

    if point in already:
        return already[point]

    if len(conds) == 0:
        if len(lens) == 0:
            already[point] = 1
            return 1
        already[point] = 0
        return 0

    if conds[0] == '.':
        return ways(conds[1:], lens)

    if len(lens) == 0:
        if '#' in conds:
            already[point] = 0
            return 0
        already[point] = 1
        return 1

    if len(conds) < lens[0]:
        already[point] = 0
        return 0

    if len(conds) < sum(lens) + len(lens) - 1:
        already[point] = 0
        return 0

    if conds[0] == '#':
        if conds[0:lens[0]].replace('?', '#') == '#'*lens[0]:
            if len(conds) == lens[0]:
                if len(lens) == 1:
                    already[point] = 1
                    return 1
                already[point] = 0
                return 0
            if conds[lens[0]] == '#':
                already[point] = 0
                return 0
            return ways(conds[lens[0] + 1:], lens[1:])
        already[point] = 0
        return 0

    if conds[0] == '?':
        res = ways(conds[1:], lens) + ways('#' + conds[1:], lens)
        already[point] = res
        return res

    print("Should not reach here", conds, lens)


def main():
    global already

    part1 = 0
    part2 = 0

    for line in util.lines_from_file(sys.argv[1]):
        already = {}
        parts = line.strip().split(' ')
        lens = [int(x) for x in parts[1].split(',')]
        part1 += ways(parts[0], lens)
        part2 += ways('?'.join([parts[0]] * 5), lens * 5)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
