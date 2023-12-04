#!/usr/bin/env python3

import sys

import util


def line_to_play(line):
    result = [set(), set()]
    parts = line.strip().split(': ')[1].split(' | ')
    for i in range(2):
        for item in parts[i].split(' '):
            if item != '':
                result[i].add(int(item))
    return result


def main():
    part1 = 0
    cards = [0] * 200
    num = 0
    lines = util.lines_from_file(sys.argv[1])
    for line in lines:
        num += 1
        cards[num] += 1
        play = line_to_play(line)

        if play[0] & play[1]:
            part1 += (1 << (len(play[0] & play[1]) - 1))
            for i in range(len(play[0] & play[1])):
                cards[num + 1 + i] += cards[num]

    print(f"Part 1: {part1}")
    print(f"Part 2: {sum(cards)}")


if __name__ == "__main__":
    main()
