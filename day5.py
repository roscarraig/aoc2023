#!/usr/bin/env python3

import sys
import util


def findmap(item, map):
    for entry in map:
        if item in range(entry[1], entry[1] + entry[2]):
            return entry[0] + item - entry[1]
    return item


def traceseed(a, r, seeds):
    seedlist = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    for seed in sorted(seedlist, key=lambda x:x[0]):
        if a + r < seed[0]:
            return
        if a < seed[0]:
            return seed[0]
        if a < seed[0] + seed[1]:
            return a


def tracemaps(a, r, maps, level, seeds):
    if level == -1:
        return traceseed(a, r, seeds)

    for map in sorted(maps[level], key=lambda x:x[0]):
        if a < map[0]:
            if a + r < map[0]:
                return tracemaps(a, r, maps, level - 1, seeds)
            res = tracemaps(a, map[0] - a, maps, level - 1, seeds)
            if res:
                return res
            r -= map[0] - a
            a = map[0]
        if a < map[0] + map[2]:
            if a + r < map[0] + map[2]:
                return tracemaps(map[1] + a - map[0], r, maps, level - 1, seeds)
            res = tracemaps(map[1] + a - map[0], map[2] + map[0] - a, maps, level - 1, seeds)
            if res:
                return res

            r -= map[0] + map[2] - a
            a = map[0] + map[2]
    return tracemaps(a, r, maps, level - 1, seeds)


def main():
    part2 = 0
    maps = []
    data = util.lines_from_file(sys.argv[1])
    seeds = util.line_to_ints(data[0].strip().split(': ')[1])
    active = []

    for i in range(2, len(data)):
        if data[i].strip().endswith(" map:"):
            if active:
                maps.append(active)
            active = []
        elif data[i].strip() != '':
            active.append(util.line_to_ints(data[i]))

    maps.append(active)

    from1 = seeds

    end = maps[-1]
    highstart = max([x[0] for x in end])
    highrange = [x[2] for x in end if x[0] == highstart][0]

    part2 = tracemaps(0, highstart + highrange, maps, len(maps) - 1, seeds)

    for i in range(len(maps)):
        to1 = []
        for item in from1:
            to1.append(findmap(item, maps[i]))
        from1 = to1
        part2 = findmap(part2, maps[i])

    print(f"Part 1: {min(to1)}")
    print(f"Part 2: {part2}")



if __name__ == '__main__':
    main()
