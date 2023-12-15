#!/usr/bin/env python3

import util
import sys


def hash(instr):
    result = 0
    for x in instr:
        result += ord(x)
        result *= 17
        result %= 256
    return result


def main():
    part1 = 0
    part2 = 0
    boxes = [[] for _ in range(256)]
    boxva = [[] for _ in range(256)]

    for instr in util.lines_from_file(sys.argv[1])[0].strip().split(","):
        part1 += hash(instr)
        if '=' in instr:
            parts = instr.split('=')
            boxno = hash(parts[0])
            value = int(parts[1])
            label = parts[0]
            if label in boxes[boxno]:
                boxva[boxno][boxes[boxno].index(label)] = value
            else:
                boxes[boxno].append(label)
                boxva[boxno].append(value)
        elif '-' in instr:
            label = instr.split('-')[0]
            boxno = hash(label)
            if label in boxes[boxno]:
                ind = boxes[boxno].index(label)
                boxes[boxno].pop(ind)
                boxva[boxno].pop(ind)

    print(f"Part 1: {part1}")

    for i in range(256):
        if len(boxes[i]) > 0:
            for j in range(len(boxes[i])):
                part2 += (i + 1) * (j + 1) * boxva[i][j]
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
