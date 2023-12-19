#!/usr/bin/env python3

import util
import resource
import sys

from operator import itemgetter


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


def check2(x, y, ldir, heat, steps, city, seen):

    if steps < 1:
        return False

    if x < 0 or y < 0 or x >= len(city[0]) or y >= len(city):
        return False

    heat += city[y][x]
    if heat > 901:
        return False

    if (x, y) in seen:
        for item in seen[(x, y)]:
            if item['heat'] < heat:
                if item['dir'] == ldir and item['steps'] >= steps:
                    return False
            if item['heat']  == heat and item['dir'] == ldir and item['steps'] >= steps:
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


def check2a(x, y, ldir, heat, steps, city, seen, w, h):

    if steps < 1:
        return False

    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    heat += city[y][x]

    if (x, y, ldir, steps) in seen:
        if seen[(x, y, ldir, steps)] <= heat:
            return False
    seen[(x, y, ldir, steps)] = heat
    return True


def trace(city, seen):
    wave = []
    wave.append([1, 0, 1, 2, 0])
    wave.append([0, 1, 2, 2, 0])
    i = 0

    while wave:
        i += 1
        nextwave = []
        # print(i, len(wave))
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
        wave = sorted(nextwave, key=itemgetter(4))


def trace2a(city, seen):
    wave = []
    wave.append([4, 0, 1, 6, sum([city[0][1 + i] for i in range(3)])])
    wave.append([0, 4, 2, 6, sum([city[i + 1][0] for i in range(3)])])
    i = 0
    ch = len(city)
    cw = len(city[0])

    while wave:
        i += 1
        nextwave = []
        print(i, len(wave))
        for x, y, ldir, steps, heat in wave:
            heat += city[y][x]
            if ldir == 1:
                if check2a(x + 1, y, 1, heat, steps - 1, city, seen, cw, ch):
                    nextwave.append([x + 1, y, 1, steps - 1, heat])
                if y + 4 < ch:
                    v = sum([city[y + 1 + j][x] for j in range(3)])
                    if check2a(x, y + 1, 2, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x, y + 4, 2, 6, heat + v])
                if y > 3:
                    v = sum([city[y - 1 - j][x] for j in range(3)])
                    if check2a(x, y - 1, 4, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x, y - 4, 4, 6, heat + v])
            elif ldir == 3:
                if check2a(x - 1, y, 3, heat, steps - 1, city, seen, cw, ch):
                    nextwave.append([x - 1, y, 3, steps - 1, heat])
                if y + 4 < ch:
                    v = sum([city[y + 1 + j][x] for j in range(3)])
                    if check2a(x, y + 4, 2, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x, y + 4, 2, 6, heat + v])
                if y > 3:
                    v = sum([city[y - 1 - j][x] for j in range(3)])
                    if check2a(x, y - 1, 4, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x, y - 4, 4, 6, heat + v])
            elif ldir == 2:
                if check2a(x, y + 1, 2, heat, steps - 1, city, seen, cw, ch):
                    nextwave.append([x, y + 1, 2, steps - 1, heat])
                if x + 4 < cw:
                    v = sum([city[y][x + 1 + j] for j in range(3)])
                    if check2a(x + 4, y, 1, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x + 4, y, 1, 6, heat + v])
                if x > 3:
                    v = sum([city[y][x - 1 - j] for j in range(3)])
                    if check2a(x - 4, y, 3, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x - 4, y, 3, 6, heat + v])
            elif ldir == 4:
                if check2a(x, y - 1, 4, heat, steps - 1, city, seen, cw, ch):
                    nextwave.append([x, y - 1, 4, steps - 1, heat])
                if x + 4 < cw:
                    v = sum([city[y][x + 1 + j] for j in range(3)])
                    if check2a(x + 4, y, 1, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x + 4, y, 1, 6, heat + v])
                if x > 3:
                    v = sum([city[y][x - 1 - j] for j in range(3)])
                    if check2a(x - 4, y, 3, heat + v, 6, city, seen, cw, ch):
                        nextwave.append([x - 4, y, 3, 6, heat + v])
        wave = sorted(nextwave, key=itemgetter(4))


def trace2(city, seen):
    wave = []
    wave.append([4, 0, 1, 6, sum([city[0][1 + i] for i in range(3)])])
    wave.append([0, 4, 2, 6, sum([city[i + 1][0] for i in range(3)])])
    i = 0
    ch = len(city)
    cw = len(city[0])

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
                if check2(x + 1, y, 1, heat, steps - 1, city, seen):
                    nextwave.append([x + 1, y, 1, steps - 1, heat])
                if y + 4 < ch:
                    v = sum([city[y + 1 + j][x] for j in range(3)])
                    if check2(x, y + 1, 2, heat + v, 6, city, seen):
                        nextwave.append([x, y + 4, 2, 6, heat + v])
                if y > 3:
                    v = sum([city[y - 1 - j][x] for j in range(3)])
                    if check2(x, y - 1, 4, heat + v, 6, city, seen):
                        nextwave.append([x, y - 4, 4, 6, heat + v])
            elif ldir == 3:
                if check2(x - 1, y, 3, heat, steps - 1, city, seen):
                    nextwave.append([x - 1, y, 3, steps - 1, heat])
                if y + 4 < ch:
                    v = sum([city[y + 1 + j][x] for j in range(3)])
                    if check2(x, y + 4, 2, heat + v, 6, city, seen):
                        nextwave.append([x, y + 4, 2, 6, heat + v])
                if y > 3:
                    v = sum([city[y - 1 - j][x] for j in range(3)])
                    if check2(x, y - 1, 4, heat + v, 6, city, seen):
                        nextwave.append([x, y - 4, 4, 6, heat + v])
            elif ldir == 2:
                if check2(x, y + 1, 2, heat, steps - 1, city, seen):
                    nextwave.append([x, y + 1, 2, steps - 1, heat])
                if x + 4 < cw:
                    v = sum([city[y][x + 1 + j] for j in range(3)])
                    if check2(x + 4, y, 1, heat + v, 6, city, seen):
                        nextwave.append([x + 4, y, 1, 6, heat + v])
                if x > 3:
                    v = sum([city[y][x - 1 - j] for j in range(3)])
                    if check2(x - 4, y, 3, heat + v, 6, city, seen):
                        nextwave.append([x - 4, y, 3, 6, heat + v])
            elif ldir == 4:
                if check2(x, y - 1, 4, heat, steps - 1, city, seen):
                    nextwave.append([x, y - 1, 4, steps - 1, heat])
                if x + 4 < cw:
                    v = sum([city[y][x + 1 + j] for j in range(3)])
                    if check2(x + 4, y, 1, heat + v, 6, city, seen):
                        nextwave.append([x + 4, y, 1, 6, heat + v])
                if x > 3:
                    v = sum([city[y][x - 1 - j] for j in range(3)])
                    if check2(x - 4, y, 3, heat + v, 6, city, seen):
                        nextwave.append([x - 4, y, 3, 6, heat + v])
        wave = nextwave


def main(filename):
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    sys.setrecursionlimit(10**6)

    part1 = 0
    part2 = []
    city =  [[int(y) for y in x.strip()] for x in util.lines_from_file(filename)]
    seen = {}
    h = len(city)
    w = len(city[0])
    # trace(city, seen)
    # part1 = min([x["heat"] for x in seen[(w - 1, h - 1)]])
    # print(f"Part 1: {part1}")
    # seen = {}
    # trace2(city, seen)
    # part2 = min([x["heat"] for x in seen[(w - 1, h - 1)]])
    seen = {}
    trace2a(city, seen)
    part2 = min([seen[a] for a in seen if a[0] == w - 1 and a[1] == h - 1]) 
    print(f"Part 2: {part2}")
    # 901 high
    # 876 low


if __name__ == '__main__':
    main(sys.argv[1])
