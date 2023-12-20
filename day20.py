#!/usr/bin/env python3

import math
import util
import sys


def main():
    part1 = 0
    part2 = 0
    lines = util.lines_from_file(sys.argv[1])
    code = {}
    hilow = [0, 0]

    for line in lines:
        left, right = line.strip().split(' -> ')
        targets = right.split(', ')
        if left == 'broadcaster':
            code[left] = {"targets": targets, "type": "b"}
        else:
            code[left[1:]] = {"targets": targets, "type": left[0]}
    for item in code:
        if code[item]['type'] == '%':
            code[item]['state'] = 0
        elif code[item]['type'] == '&':
            code[item]['state'] = {x: 0 for x in code if item in code[x]["targets"]}
            code[item]['loop'] = {}

    i = 0
    while not part2:
        i += 1
        queue = [("button", "broadcaster", 0)]
        if i % 1000000 == 0:
            print(i // 1000000)
        while queue:
            # inpt, module, pulse = queue.pop()
            press = queue.pop(0)
            inpt, module, pulse = press
            if i <= 1000:
                hilow[pulse] += 1
            if module == "rx" and pulse == 0:
                part2 = i
                break
            elif module not in code:
                pass
            elif code[module]["type"] == 'b':
                for item in code[module]["targets"]:
                    queue.append((module, item, pulse))
            elif code[module]["type"] == '%':
                if not pulse:
                    code[module]["state"] = 1 - code[module]["state"]
                    for item in code[module]["targets"]:
                        queue.append((module, item, code[module]["state"]))
            elif code[module]["type"] == '&':
                code[module]["state"][inpt] = pulse
                if module == 'hj' and pulse:
                    code[module]["loop"][inpt] = i
                    if len(code[module]["loop"]) == len(code[module]["state"]):
                        part2 = math.lcm(*[code[module]["loop"][x] for x in code[module]["loop"]])
                        break
                if min([code[module]["state"][x] for x in code[module]["state"]]) == 1:
                    for item in code[module]["targets"]:
                        queue.append((module, item, 0))
                else:
                    for item in code[module]["targets"]:
                        queue.append((module, item, 1))
        if i == 1000:
            part1 = hilow[0] * hilow[1]
            print(f"Part 1: {part1}")

    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()
