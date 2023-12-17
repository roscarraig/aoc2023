#!/usr/bin/env python3

import util
import resource
import sys


def check(x, y, ldir, heat, steps, city, seen):
    h = len(city)
    w = len(city[0])

    if steps < 1:
        return False
    if x < 0 or y < 0 or x >= len(city[0]) or y >= len(city):
        return False
    if (w - 1, h - 1) in seen:
        print(seen[(w - 1, h - 1)])

    heat += city[y][x]

    if (x, y) in seen:
        for item in seen[(x, y)]:
            if item['dir'] == ldir and item['steps'] >= steps and item['heat'] < heat:
                return False
        seen[(x, y)].append({
            "steps": steps,
            "dir": ldir,
            "heat": heat
        })
    else:
        seen[(x, y)] = [{
            "steps": steps,
            "dir": ldir,
            "heat": heat
        }]
    return True


def trace2(city, seen):
    wave = []
    wave.append([1, 0, 1, 2, 0])
    wave.append([0, 1, 2, 2, 0])

    while wave:
        nextwave = []
        print(len(wave))
        for item in wave:
            x = item[0]
            y = item[1]
            ldir = item[2]
            steps = item[3]
            # print(x, y, item, city[y][x])
            heat = item[4] + city[y][x]
            if ldir == 1:
                if check(x + 1, y, 1, heat, steps - 1, city, seen):
                    nextwave.append([x + 1, y, 1, steps - 1, heat])
                if check(x, y + 1, 2, heat, 3, city, seen):
                    nextwave.append([x, y + 1, 2, 3, heat])
                if check(x, y - 1, 4, heat, 3, city, seen):
                    nextwave.append([x, y - 1, 4, 3, heat])
            elif ldir == 3:
                if check(x - 1, y, 3, heat, steps - 1, city, seen):
                    nextwave.append([x - 1, y, 3, steps - 1, heat])
                if check(x, y + 1, 2, heat, 3, city, seen):
                    nextwave.append([x, y + 1, 2, 3, heat])
                if check(x, y - 1, 4, heat, 3, city, seen):
                    nextwave.append([x, y - 1, 4, 3, heat])
            elif ldir == 2:
                if check(x, y + 1, 2, heat, steps - 1, city, seen):
                    nextwave.append([x, y + 1, 2, steps - 1, heat])
                if check(x + 1, y, 1, heat, 3, city, seen):
                    nextwave.append([x + 1, y, 1, 3, heat])
                if check(x - 1, y, 3, heat, 3, city, seen):
                    nextwave.append([x - 1, y, 3, 3, heat])
            elif ldir == 4:
                if check(x, y - 1, 4, heat, steps - 1, city, seen):
                    nextwave.append([x, y - 1, 4, steps - 1, heat])
                if check(x + 1, y, 1, heat, 3, city, seen):
                    nextwave.append([x + 1, y, 1, 3, heat])
                if check(x - 1, y, 3, heat, 3, city, seen):
                    nextwave.append([x - 1, y, 3, 3, heat])
        wave = nextwave


def trace(x, y, ldir, heat, steps, city, seen):
    while steps > 0:
        if x < 0 or y < 0 or x >= len(city[0]) or y >= len(city):
            return
        if (x, y, ldir, steps) in seen and seen[(x, y, ldir, steps)] < heat + city[y][x]:
            return
        if (x, y, ldir, steps + 1) in seen and seen[(x, y, ldir, steps + 1)] < heat + city[y][x]:
            return
        if (x, y, ldir, steps + 2) in seen and seen[(x, y, ldir, steps + 2)] < heat + city[y][x]:
            return
        if (x, y) in seen and seen[(x, y)] < heat + city[y][x]:
            return

        seen[(x, y, ldir, steps)] = heat + city[y][x]
        seen[(x, y)] = heat + city[y][x]
        heat += city[y][x]
        steps -= 1

        if ldir == 1:
            trace(x, y + 1, 2, heat, 3, city, seen)
            trace(x, y - 1, 2, heat, 3, city, seen)
            x += 1
        elif ldir == 2:
            trace(x + 1, y, 1, heat, 3, city, seen)
            trace(x - 1, y, 3, heat, 3, city, seen)
            y += 1
        elif ldir == 3:
            trace(x, y + 1, 2, heat, 3, city, seen)
            trace(x, y - 1, 4, heat, 3, city, seen)
            x -= 1
        elif ldir == 4:
            trace(x + 1, y, 1, heat, 3, city, seen)
            trace(x - 1, y, 3, heat, 3, city, seen)
            y -= 1


def main():
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    sys.setrecursionlimit(10**6)

    part1 = 0
    part2 = []
    city =  [[int(y) for y in x.strip()] for x in util.lines_from_file(sys.argv[1])]
    seen = {}
    h = len(city)
    w = len(city[0])
    # trace(1, 0, 1, 0, 2, city, seen)
    # trace(0, 1, 2, 0, 2, city, seen)
    trace2(city, seen)
    # print(seen[(w - 1, h - 1)])
    part1 = min([x["heat"] for x in seen[(w - 1, h - 1)]])
    print(f"Part 1: {part1}")
    # print(f"Part 2: {max(part2)}")


if __name__ == '__main__':
    main()
