#!/usr/bin/env python3

import util
import sys


def findsym(pattern):
    w = len(pattern[0])
    w2 = w // 2
    h = len(pattern)
    mirs = []

    for i in range(1, w - 1):
        mir = True
        for j in range(h):
            if i <= w2:
                if pattern[j][:i] != pattern[j][2 * i - 1:i - 1:-1]:
                    mir = False
                    break
            else:
                if pattern[j][i - w2:i] != pattern[j][w - 1: i - 1: -1]:
                    mir = False
                    break

        if mir:
            print(i)
            return i
    for line in pattern:
        print(line)
    print("None")
    return 0


def translate(pattern):
    w = len(pattern[0])
    h = len(pattern)
    return [''.join([pattern[j][i] for j in range(h)]) for i in range(w)]



def main():
    patterns = []
    pattern = []
    hcount = 0
    vcount = 0

    for line in util.lines_from_file(sys.argv[1]):
        if line.strip() == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())

    patterns.append(pattern)

    for pattern in patterns:
        print("H")
        hcount += findsym(pattern)
        print("V")
        vcount += findsym(translate(pattern))

    print(f"Part 1: {hcount + 100 * vcount}")
    # 7175 low


if __name__ == '__main__':
    main()
