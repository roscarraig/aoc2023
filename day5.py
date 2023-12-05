#!/usr/bin/env python3

import sys
import util


def findmap2(items, map):
    result = []
    for i in range(0, len(items), 2):
        a = items[i]
        b = items[i + 1]
        for entry in map:

def findmap(item, map):
    for entry in map:
        if item in range(entry[1], entry[1] + entry[2]):
            return entry[0] + item - entry[1]
    return item


def tracemaps(a, r, maps, level, seeds):
    if level == -1:
        return traceseed(a, r, seeds)

    for map in maps[level]:
        if a < map[0]:
            if a + r < map[0]:
                return tracemaps(a, r, maps, level - 1, seeds)
            res = tracemaps(a, map[0] - a, maps, level - 1, seeds)
            if res:
                return res
            if a + r > map[0] + map[2]:
                res = tracemaps(map[1], map[2], maps, level - 1, seeds)
                if res:
                    return res

            return tracemaps(map[0], r + map[0] - a, maps, level - 1, seeds)
        if a < map


def main():
    maps = {}
    mapi = []
    data = util.lines_from_file(sys.argv[1])
    seeds = util.line_to_ints(data[0].strip().split(': ')[1])
    seeds2 = []

    for i in range(0, len(seeds), 2):
        seeds2 += list(range(seeds[i], seeds[i] + seeds[i + 1]))

    for i in range(2, len(data)):
        if data[i].strip().endswith(" map:"):
            active = data[i].split(' ')[0]
            maps[active] = []
            mapi.append(active)
        elif data[i].strip() != '':
            maps[active].append(util.line_to_ints(data[i]))

    from1 = seeds
    from2 = seeds2

    for item in sorted(maps[-1], key=lambda x:x[0]):
        for i in range(len(maps) - 2, -1, -1):


    for i in range(len(mapi)):
        print(mapi[i])
        to1 = []
        to2 = []
        for item in from1:
            to1.append(findmap(item, maps[mapi[i]]))
        for item in from2:
            to2.append(findmap(item, maps[mapi[i]]))
        from1 = to1
        from2 = to2

    print(f"Part 1: {min(to1)}")
    print(f"Part 2: {min(to2)}")



if __name__ == '__main__':
    main()
