#!/usr/bin/env python3

import util
import sys


def trace(nodes, point, finish, path, travelled):
    longest = 0

    if point == finish:
        return travelled

    tpath = set(path) | set([point])

    for node in nodes[point]:
        if node in tpath:
            continue
        longest = max(longest, trace(nodes, node, finish, tpath, nodes[point][node] + travelled))
    return longest


def trace0(nodes, point, finish, path):
    longest = 0
    tpath = list(path)
    tpath.append(point)
    seen = set(tpath)
    npoints = set(nodes[point]) - set(tpath)

    if point == finish:
        return len(tpath) - 1

    while len(npoints) < 2:
        if point == finish:
            return len(tpath) - 1
        if len(npoints) == 0:
            return 0
        point = list(npoints)[0]
        tpath.append(point)
        npoints = set(nodes[point]) - set(tpath)

    for x in set(nodes[point]) - set(tpath):
        longest = max(longest, trace(nodes, x, finish, tpath))
    return longest


def neighbours(bmap, x, y, w, h, part2=False):
    result = []
    if x > 0:
        if part2:
            if bmap[y][x - 1] != '#':
                result.append((x - 1, y))
        else:
            if bmap[y][x - 1] in ['.', '<']:
                result.append((x - 1, y))
    if x < w - 1:
        if part2:
            if bmap[y][x + 1] != '#':
                result.append((x + 1, y))
        else:
            if bmap[y][x + 1] in ['.', '>']:
                result.append((x + 1, y))
    if y > 0:
        if part2:
            if bmap[y - 1][x] != '#':
                result.append((x, y - 1))
        else:
            if bmap[y - 1][x] in ['.', '^']:
                result.append((x, y - 1))
    if y < h - 1:
        if part2:
            if bmap[y + 1][x] != '#':
                result.append((x, y + 1))
        else:
            if bmap[y + 1][x] in ['.', 'v']:
                result.append((x, y + 1))
    return result


def main():
    part1 = 0
    part2 = 0
    nodes = {}
    nodes2 = {}
    dnodes = {}
    dnodes2 = {}

    bmap = [x.strip() for x in util.lines_from_file(sys.argv[1])]
    h = len(bmap)
    w = len(bmap[0])

    for y in range(h):
        for x in range(w):
            if bmap[y][x] == '#':
                continue
            nodes[(x, y)] = neighbours(bmap, x, y, w, h)
            nodes2[(x, y)] = neighbours(bmap, x, y, w, h, True)
            if y == 0:
                start = (x, y)
            elif y == h - 1:
                finish = (x, y)

    for node in nodes:
        if len(nodes[node]) != 2 or node in [start, finish]:
            dnodes[node] = {}

            for point in nodes[node]:
                last = node
                count = 1
                while len(nodes[point]) == 2:
                    count += 1
                    nnode = list(set(nodes[point]) - set([last]))[0]
                    last = point
                    point = nnode
                dnodes[node][point] = count

        if len(nodes2[node]) != 2 or node in [start, finish]:
            dnodes2[node] = {}

            for point in nodes2[node]:
                last = node
                count = 1
                while len(nodes2[point]) == 2:
                    count += 1
                    nnode = list(set(nodes2[point]) - set([last]))[0]
                    last = point
                    point = nnode
                dnodes2[node][point] = count

    part1 = trace(dnodes, start, finish, [], 0)
    print(f"Part 1: {part1}")
    part2 = trace(dnodes2, start, finish, [], 0)

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
