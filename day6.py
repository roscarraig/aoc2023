#!/usr/bin/env python3

import math
import sys
import util


def bounds(t, d):
    d += 0.1
    low = (t - math.sqrt(t * t - 4 * d)) / 2
    high = (t + math.sqrt(t * t - 4 * d)) / 2
    if low != int(low):
        low += 1

    return [ int(low), int(high) ]


def main():
    part1 = 1
    data = util.lines_from_file(sys.argv[1])
    times = [int(x) for x in data[0].strip().split(":")[1].split(' ') if x != '']
    dists = [int(x) for x in data[1].strip().split(":")[1].split(' ') if x != '']
    for i in range(len(times)):
        lowhigh = bounds(times[i], dists[i])
        part1 *= 1 + lowhigh[1] - lowhigh[0]
    print(f"Part 1: {part1}")
    t = int (data[0].strip().split(":")[1].replace(" ", ""))
    d = int (data[1].strip().split(":")[1].replace(" ", ""))
    lowhigh = bounds(t, d)
    print(f"Part 2: {1 + lowhigh[1] - lowhigh[0]}")


if __name__ == '__main__':
    main()
