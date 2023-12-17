#!/usr/bin/env python3

import util
import resource
import sys


def add_to_wave(wave, params):
    for i in range(len(wave) - 1, -1, -1):
        if wave[i][0:3] == params[0:3]:
            if wave[i][3] >= params[3]:
                if wave[i][4] <= params[4]:
                    return
            if wave[i][3] < params[3] and wave[i][4] >= params[4]:
                wave.pop(i)
    wave.append(params)


def check(x, y, ldir, heat, steps, city, seen):

    if steps < 1:
        return False

    if x < 0 or y < 0 or x >= len(city[0]) or y >= len(city):
        return False

    heat += city[y][x]

    if (x, y) in seen:
        for item in seen[(x, y)]:
            if item['heat'] < heat:
                if item['dir'] == ldir and item['steps'] >= steps:
                    return False
            if item['heat']  == heat and item['dir'] == ldir and item['steps'] >= steps:
                return False
            if item['heat'] + 36 < heat:
                return False
        for i in range(len(seen[(x, y)]) - 1, -1, -1):
            if seen[(x, y)][i]['dir'] == ldir and seen[(x, y)][i]['heat'] >= heat and seen[(x, y)][i]['steps'] <= steps:
                seen[(x, y)].pop(i)
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


def trace(city, seen):
    wave = []
    wave.append([1, 0, 1, 2, 0])
    wave.append([0, 1, 2, 2, 0])
    i = 0

    while wave:
        i += 1
        nextwave = []
        print(i, len(wave))
        for item in wave:
            x = item[0]
            y = item[1]
            ldir = item[2]
            steps = item[3]
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
        # print(wave)


def main(filename):
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    sys.setrecursionlimit(10**6)

    part1 = 0
    part2 = []
    city =  [[int(y) for y in x.strip()] for x in util.lines_from_file(filename)]
    seen = {}
    h = len(city)
    w = len(city[0])
    trace(city, seen)
    part1 = min([x["heat"] for x in seen[(w - 1, h - 1)]])
    print(f"Part 1: {part1}")
    # print(f"Part 2: {max(part2)}")


if __name__ == '__main__':
    main(sys.argv[1])
