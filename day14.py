#!/usr/bin/env python3

import util
import sys


def cycle(bmap, justnorth=False):
    h = len(bmap)
    w = len(bmap[0])

    # North
    for j in range(h):
        for i in range(w):
            if bmap[j][i] == 'O' and j > 0:
                y = j
                while y > 0 and bmap[y - 1][i] == '.':
                    y -= 1
                if y != j:
                    bmap[j][i] = '.'
                    bmap[y][i] = 'O'
    if justnorth:
        return

    # West
    for i in range(w):
        for j in range(h):
            if bmap[j][i] == 'O' and i > 0:
                x = i
                while x > 0 and bmap[j][x - 1] == '.':
                    x -= 1
                if x != i:
                    bmap[j][i] = '.'
                    bmap[j][x] = 'O'

    # South
    for j in range(h - 1, -1, -1):
        for i in range(w):
            if bmap[j][i] == 'O' and j < h - 1:
                y = j
                while y < h - 1 and bmap[y + 1][i] == '.':
                    y += 1
                if y != j:
                    bmap[j][i] = '.'
                    bmap[y][i] = 'O'

    # East
    for i in range(w - 1, -1, -1):
        for j in range(h):
            if bmap[j][i] == 'O' and i < w - 1:
                x = i
                while x < w - 1 and bmap[j][x + 1] == '.':
                    x += 1
                if x != i:
                    bmap[j][i] = '.'
                    bmap[j][x] = 'O'


def load(bmap):
    h = len(bmap)
    result = 0

    for i in range(h):
        result += (h - i) * len([1 for x in bmap[i] if x == 'O'])

    return result


def main():
    part1 = 0
    part2 = 0
    states = {}
    i = 0
    target = 1000000000 

    initial = util.lines_from_file(sys.argv[1])
    p1map = [list(line.strip()) for line in initial]
    p2map = [list(line.strip()) for line in initial]
    cycle(p1map, True)
    part1 = load(p1map)
    print(f"Part 1: {part1}")

    while i < target:
        cycle(p2map)
        i += 1
        state = util.matrix_string(p2map)
        if state in states:
            interval = i - states[state]
            states[state] = i
            target -= ((target - i) // interval) * interval
        else:
            states[state] = i
    part2 = load(p2map)
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
