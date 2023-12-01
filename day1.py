#!/usr/bin/env python3

import sys
import util


def main():
    part1 = 0
    part2 = 0
    data = util.lines_from_file(sys.argv[1])
    for line in data:
        number = util.extract_digits(line)
        if len(number) > 0:
            part1 += int(number[0] + number[-1])
        number = util.read_digits(line)
        part2 += int(number[0] + number[-1])
    print(f"Part1: {part1}")
    print(f"Part2: {part2}")


if __name__ == '__main__':
    main()
