#!/usr/bin/env python3

import util
import sys


def show(pmap):
    for j in range(len(pmap)):
        print(''.join(pmap[j]))


def start(pmap):
    for j in range(len(pmap)):
        for i in range(len(pmap[0])):
            if pmap[j][i] == 'S':
                return i, j


def tidy(pmap):
    w = len(pmap[0])
    h = len(pmap)
    untidy = True

    while untidy:
        untidy = False

        for j in range(h):
            for i in range(w):
                if pmap[j][i] == '.':
                    continue
                if pmap[j][i] in ['-', 'J', '7']:
                    if i == 0 or pmap[j][i - 1] not in ['-', 'F', 'S', 'L']:
                        untidy = True
                        pmap[j][i] = '.'
                        continue
                if pmap[j][i] in ['|', 'L', 'J']:
                    if j == 0 or pmap[j - 1][i] not in ['|', 'F', 'S', '7']:
                        untidy = True
                        pmap[j][i] = '.'
                        continue
                if pmap[j][i] in ['-', 'F', 'L']:
                    if i == w - 1 or pmap[j][i + 1] not in ['-', '7', 'J', 'S']:
                        untidy = True
                        pmap[j][i] = '.'
                        continue
                if pmap[j][i] in ['|', 'F', '7']:
                    if j == h - 1 or pmap[j + 1][i] not in ['|', 'L', 'J', 'S']:
                        untidy = True
                        pmap[j][i] = '.'
                        continue


def step(pmap, grid, num, shadow):
    hit = False
    w = len(pmap[0])
    h = len(pmap)

    if num == 0:
        sx, sy = start(pmap)
        shadow[sy][sx] = '#'
        if sx > 0 and pmap[sy][sx - 1] in ['-', 'F', 'L']:
            grid[sy][sx - 1] = 1
        if sx < w - 1 and pmap[sy][sx + 1] in ['-', '7', 'J']:
            grid[sy][sx + 1] = 1
        if sy > 0 and pmap[sy - 1][sx] in ['|', 'F', '7']:
            grid[sy - 1][sx] = 1
        if sy < h - 1 and pmap[sy + 1][sx] in ['|', 'L', 'J']:
            grid[sy + 1][sx] = 1
        return True

    for j in range(h):
        for i in range(w):
            if grid[j][i] == num:
                shadow[j][i] = '#'
                if i > 0 and pmap[j][i] in ['-', '7', 'J', 'S']:
                    if grid[j][i - 1] == -1:
                        grid[j][i - 1] = num + 1
                        hit = True
                if j > 0 and pmap[j][i] in ['|', 'L', 'J', 'S']:
                    if grid[j - 1][i] == -1:
                        grid[j - 1][i] = num + 1
                        hit = True
                if i < w - 1 and pmap[j][i] in ['-', 'F', 'L', 'S']:
                    if grid[j][i + 1] == -1:
                        grid[j][i + 1] = num + 1
                        hit = True
                if j < h - 1 and pmap[j][i] in ['|', 'F', '7', 'S']:
                    if grid[j + 1][i] == -1:
                        grid[j + 1][i] = num + 1
                        hit = True
    return hit


def step2(shadow, x, y, w, h):
    if shadow[y][x] not in ['L', 'J', '7', 'F', '-', '|', ' ']:
        shadow[y][x] = ' '
        if x > 0:
            step2(shadow, x - 1, y, w, h)
        if x <  w - 1:
            step2(shadow, x + 1, y, w, h)
        if y > 0:
            step2(shadow, x, y - 1, w, h)
        if y < h - 1:
            step2(shadow, x, y + 1, w, h)


def step3(shadow, w, h):
    hit = True
    while hit:
        hit = False
        for j in range(h):
            for i in range(w):
                if i < w - 1 and shadow[j][i] == ' ' and shadow[j][i + 1] == 'F' and shadow[j + 1][i + 1] == 'L':
                    hit = True
                    shadow[j][i + 1] = '.'
                    shadow[j + 1][i + 1] = '.'
                    if shadow[j][i + 2] == '7':
                        shadow[j][i + 2] = ' '
                        shadow[j + 1][i + 2] = ' '
                        step2(shadow, i + 1, j, w, h)
                        continue
                    if shadow[j][i + 2] == '-':
                        shadow[j][i + 2] = 'F'
                    elif shadow[j][i + 2] == 'J':
                        shadow[j][i + 2] = '|'
                    if shadow[j + 1][i + 2] == '-':
                        shadow[j + 1][i + 2] = 'L'
                    elif shadow[j + 1][i + 2] == '7':
                        shadow[j + 1][i + 2] = '|'
                    step2(shadow, i + 1, j, w, h)
                elif i < w - 2 and shadow[j][i] == ' ' and shadow[j][i + 1] == 'F' and shadow[j][i + 2] == '7':
                    hit = True
                    shadow[j][i + 1] = '.'
                    shadow[j][i + 2] = '.'
                    if shadow[j + 1][i + 1] == '|':
                        shadow[j + 1][i + 1] = 'F'
                    elif shadow[j + 1][i + 1] == 'J':
                        shadow[j + 1][i + 1] = '-'
                    if shadow[j + 1][i + 2] == '|':
                        shadow[j + 1][i + 2] = '7'
                    elif shadow[j + 1][i + 2] == 'L':
                        shadow[j + 1][i + 2] = '-'
                    step2(shadow, i + 1, j, w, h)
                elif i < w - 2 and shadow[j][i] == ' ' and shadow[j][i + 1] == 'L' and shadow[j][i + 2] == 'J':
                    hit = True
                    shadow[j][i + 1] = '.'
                    shadow[j][i + 2] = '.'
                    if shadow[j - 1][i + 1] == '|':
                        shadow[j - 1][i + 1] = 'L'
                    elif shadow[j - 1][i + 1] == '7':
                        shadow[j - 1][i + 1] = '-'
                    if shadow[j - 1][i + 2] == '|':
                        shadow[j - 1][i + 2] = 'J'
                    elif shadow[j - 1][i + 2] == 'F':
                        shadow[j - 1][i + 2] = '-'
                    step2(shadow, i + 1, j, w, h)
                elif i < w - 2 and shadow[j][i] == ' ' and shadow[j][i + 1] == 'L' and shadow[j - 1][i + 1] == 'F':
                    hit = True
                    shadow[j][i + 1] = '.'
                    shadow[j - 1][i + 1] = '.'
                    if shadow[j][i + 2] == '-':
                        shadow[j][i + 2] = 'L'
                    elif shadow[j][i + 2] == '7':
                        shadow[j][i + 2] = '|'
                    if shadow[j - 1][i + 2] == '-':
                        shadow[j - 1][i + 2] = 'F'
                    elif shadow[j - 1][i + 2] == 'J':
                        shadow[j - 1][i + 2] = '|'
                    step2(shadow, i + 1, j, w, h)


def main():
    sys.setrecursionlimit(10000000)
    pmap = []

    for line in util.lines_from_file(sys.argv[1]):
        pmap.append(list(line.strip()))

    w = len(pmap[0])
    h = len(pmap)
    part1 = 0
    part2 = 0

    tidy(pmap)
    show(pmap)
    shadow = [[pmap[j][i] for i in range(w)] for j in range(h)]
    show(shadow)

    grid = [[-1 for _ in range(w)] for _ in range(h)]
    sx, sy = start(pmap)
    grid[sy][sx] = 0
    while step(pmap, grid, part1, shadow):
        part1 += 1
    print("=====")
    show(shadow)

    print(f"Part 1: {part1}")
    step2(pmap, 0, 0, w, h)
    step3(pmap, w, h)
    show(pmap)
    for line in pmap:
        for point in line:
            if point == '.':
                part2 += 1
    print(f"Part 2: {part2}")
    # 535 high


if __name__ == '__main__':
    main()
