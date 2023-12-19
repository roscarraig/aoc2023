#!/usr/bin/env python3

import util
import sys


def process(part, flow, flows):
    if flow in 'AR':
        return flow
    for item in flows[flow]:
        if item['test'] == 'go':
            return process(part, item['target'], flows)
        elif item['test'] == '<':
            if part[item['param']] < item['value']:
                return process(part, item['target'], flows)
        elif item['test'] == '>':
            if part[item['param']] > item['value']:
                return process(part, item['target'], flows)


def process2(part, flow, flows):
    if flow == 'R':
        return []
    if flow == 'A':
        result = 1
        for item in part:
            a, b = part[item]
            result *= b + 1 - a
        return [result]
    for item in flows[flow]:
        if item['test'] == 'go':
            return process2(part, item['target'], flows)
        elif item['test'] == '<':
            if part[item['param']][1] < item['value']:
                return process2(part, item['target'], flows)
            if part[item['param']][0] >= item['value']:
                continue
            p1 = {x: list(part[x]) for x in part}
            p2 = {x: list(part[x]) for x in part}
            p1[item['param']][1] = item['value'] - 1
            p2[item['param']][0] = item['value']
            return process2(p1, flow, flows) + process2(p2, flow, flows)
        elif item['test'] == '>':
            if part[item['param']][0] > item['value']:
                return process2(part, item['target'], flows)
            if part[item['param']][1] <= item['value']:
                continue
            p1 = {x: list(part[x]) for x in part}
            p2 = {x: list(part[x]) for x in part}
            p1[item['param']][1] = item['value']
            p2[item['param']][0] = item['value'] + 1
            return process2(p1, flow, flows) + process2(p2, flow, flows)


def main():
    part1 = 0
    part2 = 1
    lines = util.lines_from_file(sys.argv[1])
    flows = {}
    parts = []
    logic = 1

    for line in lines:
        if logic == 1:
            if line.strip() == '':
                logic = 2
                continue
            bits = line.strip().split('{')
            tests = bits[1][:-1].split(',')
            flows[bits[0]] = []

            for item in tests:
                if ':' not in item:
                    flows[bits[0]].append({'test': 'go', 'target': item})
                    continue
                test, target = item.split(':')
                flows[bits[0]].append({
                    'test': test[1],
                    'param': test[0],
                    'value': int(test[2:]),
                    'target': target
                })
        else:
            parts.append({a.split('=')[0]: int(a.split('=')[1]) for a in line.strip()[1:-1].split(',')})

    for part in parts:
        if process(part, "in", flows) == 'A':
            part1 += sum([part[x] for x in part])

    print(f"Part 1: {part1}")

    candidate = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    part2 = sum(process2(candidate, 'in', flows))

    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()
