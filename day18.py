#!/usr/bin/env python3

import util
import sys


def flood(bmap, w, h):
    wave = set()
    for i in range(w):
        if bmap[0][i] == '.':
            bmap[0][i] = ' '
            wave.add((i, 0))
        if bmap[h - 1][i] == '.':
            bmap[h - 1][i] = ' '
            wave.add((i,  h - 1))
    for i in range(1, h - 1):
        if bmap[i][0] == '.':
            bmap[i][0] = ' '
            wave.add((0, i))
        if bmap[i][w - 1] == '.':
            bmap[i][w - 1] = ' '
            wave.add((w - 1, i))
    while wave:
        nextwave = set()
        for x, y in wave:
            if x > 0:
                if bmap[y][x - 1] == '.':
                    bmap[y][x - 1] = ' '
                    nextwave.add((x - 1, y))
            if x < w - 1:
                if bmap[y][x + 1] == '.':
                    bmap[y][x + 1] = ' '
                    nextwave.add((x + 1, y))
            if y > 0:
                if bmap[y - 1][x] == '.':
                    bmap[y - 1][x] = ' '
                    nextwave.add((x, y - 1))
            if y < h - 1:
                if bmap[y + 1][x] == '.':
                    bmap[y + 1][x] = ' '
                    nextwave.add((x, y + 1))
        wave = nextwave


def main():
    part1 = 0
    part2 = 0
    dig = util.lines_from_file(sys.argv[1])
    lake = {}
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    xl = [0]
    yl = [0]
    xl2 = [0]
    yl2 = [0]
    hlines = []
    vlines = []
    
    for line in dig:
        parts = line.split(' ')

        if parts[0] == 'R':
            x += int(parts[1])
            xl.append(x)
        elif parts[0] == 'L':
            x -= int(parts[1])
            xl.append(x)
        elif parts[0] == 'D':
            y += int(parts[1])
            yl.append(y)
        elif parts[0] == 'U':
            y -= int(parts[1])
            yl.append(y)

        p2i = parts[2]
        p2dir = p2i[7]
        p2dis = int(p2i[2:7], 16)

        if p2dir == '0':
            x2 += p2dis
            xl2.append(x2)
        elif p2dir == '2':
            x2 -= p2dis
            xl2.append(x2)
        elif p2dir == '1':
            y2 += p2dis
            yl2.append(y2)
        elif p2dir == '3':
            y2 -= p2dis
            yl2.append(y2)

    print(min(xl2), max(xl2), min(yl2), max(yl2))

    w = 1 + max(xl) - min(xl)
    h = 1 + max(yl) - min(yl)
    x = -min(xl)
    y = -min(yl)
    w2 = 1 + max(xl2) - min(xl2)
    h2 = 1 + max(yl2) - min(yl2)
    x2 = -min(xl2)
    y2 = -min(yl2)
    bmap1 = [['.' for _ in range(w)] for _ in range(h)]
    bmap1[y][x] = '#'
    map2 = {}
    map2[(x2, y2)] = '>v<^'[int(dig[-1].split(' ')[2][7])]

    for line in dig:
        parts = line.split(' ')
        dist = int(parts[1])
        p2i = parts[2]
        p2dir = p2i[7]
        p2dis = int(p2i[2:7], 16)

        if parts[0] == 'R':
            hlines.append([x, y, x + dist])
            for i in range(dist):
                x += 1
                bmap1[y][x] = '#'
        elif parts[0] == 'L':
            hlines.append([x - dist, y, x])
            for i in range(dist):
                x -= 1
                bmap1[y][x] = '#'
        elif parts[0] == 'D':
            vlines.append([x, y, y + dist])
            for i in range(dist):
                y += 1
                bmap1[y][x] = '#'
        elif parts[0] == 'U':
            vlines.append([x, y - dist, y])
            for i in range(dist):
                y -= 1
                bmap1[y][x] = '#'

        if p2dir == '0':
            if map2[(x2, y2)] == '^':
                map2[(x2, y2)] = 'F'
            elif map2[(x2, y2)] == 'v':
                map2[(x2, y2)] = 'L'
            for i in range(p2dis):
                x2 += 1
                map2[(x2, y2)] = '>'
        elif p2dir == '2':
            if map2[(x2, y2)] == '^':
                map2[(x2, y2)] = '7'
            elif map2[(x2, y2)] == 'v':
                map2[(x2, y2)] = 'J'
            for i in range(p2dis):
                x2 -= 1
                map2[(x2, y2)] = '<'
        elif p2dir == '1':
            if map2[(x2, y2)] == '>':
                map2[(x2, y2)] = '7'
            elif map2[(x2, y2)] == '<':
                map2[(x2, y2)] = 'F'
            for i in range(p2dis):
                y2 += 1
                map2[(x2, y2)] = 'v'
        elif p2dir == '3':
            if map2[(x2, y2)] == '>':
                map2[(x2, y2)] = 'J'
            elif map2[(x2, y2)] == '<':
                map2[(x2, y2)] = 'L'
            for i in range(p2dis):
                y2 += 1
                map2[(x2, y2)] = '^'

    flood(bmap1, w, h)

    # for j in range(h):
    #     print(''.join(bmap1[j]))

    part1 = len(''.join([''.join(bmap1[i]) for i in range(h)]).replace(' ', ''))

    print(f"Part 1: {part1}")
    part2 = 0

    for j in range(h2):
        inout = 0
        updown = 0
        for i in range(w2):
            if (i, j) not in map2:
                part2 += inout
                continue
            part2 += 1
            c = map2[(i, j)]
            if c in '^v':
                inount = 1 - inout
                continue
            if c in '<>':
                continue
            if c == 'L':
                updown = -1
            elif c == 'F':
                updown = 1
            elif c == 'J':
                if updown == 1:
                    inout = 1 - inout
            elif c == '7':
                if updown == -1:
                    inout = 1 - inout
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()
