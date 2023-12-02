#!/usr/bin/env python3

import sys

import util


def main():
    part1 = 0
    part2 = 0
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in util.lines_from_file(sys.argv[1]):
        minbag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        games = line.strip().split(":")[1][1:]
        valid = True

        for game in games.split("; "):
            play = {}

            for item in game.split(", "):
                parts = item.split(' ')
                play[parts[1]] = int(parts[0])

            util.maxdict(play, minbag)

            if not util.issubset(play, bag):
                valid = False

        powers = 1
        for item in minbag:
            powers *= minbag[item]

        part2 += powers

        if valid:
            part1 += int(line.split(":")[0].split(' ')[1])

    print(f"Part1: {part1}")
    print(f"Part2: {part2}")


if __name__ == "__main__":
    main()
