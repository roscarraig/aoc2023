#!/usr/bin/env python3

import util
import sys


def intersection2d(a, b):
    # x = a[0] + t1 * a[3]
    # y = a[1] + t1 * a[4]
    # x = b[0] + t2 * b[3]
    # y = b[1] + t2 * b[4]
    # x - a[0] = t1 * a[3]
    # (x - a[0]) / a[3] = t1
    # y = a[1] + (x - a[0]) * a[4] / a[3]
    # y = b[1] + (x - b[0]) * b[4] / b[3]
    # a[1] + (x - a[0]) * a[4] / a[3] = b[1] + (x - b[0]) * b[4] / b[3]
    # x*(a[4]/a[3] - b[4]/b[3]) = b[1] - b[0] * b[4] / b[3] - a[1] + a[0]*a[4]/a[3] 

    if a[3] * b[4] == a[4] * b[3]:
        return None

    x = (b[1] - b[0] * b[4] / b[3] - a[1] + a[0]*a[4]/a[3]) / (a[4]/a[3]-b[4]/b[3]) 
    y = a[1] + (x - a[0]) * a[4] / a[3]
    t1 = (x - a[0]) / a[3]
    t2 = (x - b[0]) / b[3]

    if min(t1, t2) < 0:
        return None


    return [x, y]


def inbounds(point, a, b):
    if point[0] < a:
        return False
    if point[1] < a:
        return False
    if point[0] > b:
        return False
    if point[1] > b:
        return False
    return True

    
def main():
    part1 = 0
    part2 = 0
    stones = [x.strip().replace('@', ',').replace(' ', '').split(',') for x in util.lines_from_file(sys.argv[1])]
    stones = [[int(y) for y in x] for x in stones]

    for a in range(len(stones) - 1):
        for b in range(a + 1, len(stones)):
            res =  intersection2d(stones[a], stones[b])
            if res and inbounds(res, 200000000000000, 400000000000000):
                part1 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
