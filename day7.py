#!/usr/bin/env python3

import sys
import util

from functools import cmp_to_key

joker_rule = False


def card_value(card):
    if joker_rule:
        return "J123456789TQKA".index(card)
    else:
        return "0123456789TJQKA".index(card)


def compare_hands(left, right):
    lcards = left["cards"]
    rcards = right["cards"]
    htl = hand_type(lcards)
    htr = hand_type(rcards)
    if htl < htr:
        return -1
    if htl > htr:
        return 1
    for i in range(5):
        if card_value(lcards[i]) < card_value(rcards[i]):
            return -1
        if card_value(lcards[i]) > card_value(rcards[i]):
            return 1
    return 0


def hand_type(hand):
    unique = len(set(list(hand)))

    if unique == 1:
        return 7
    if unique == 2:
        if joker_rule and "J" in hand:
            return 7
        if len(hand.replace(hand[0], "")) in [1, 4]:
            return 6
        return 5
    if unique == 5:
        if joker_rule and "J" in hand:
            return 2
        return 1
    if unique == 4:
        if joker_rule and "J" in hand:
            return 4
        return 2
    if joker_rule and "J" in hand:
        tmp = hand.replace("J", "")
        if len(tmp) == 2:
            return 6
        if len(tmp) == 3:
            return 6
        tmp = tmp.replace(tmp[0], "")
        if len(tmp) == 2:
            return 5
        return 6

    tmp = hand.replace(hand[0], "")
    if len(tmp) == 2:
        return 4
    if len(tmp) == 3:
        return 3
    tmp = tmp.replace(tmp[0], "")
    if len(tmp) == 2:
        return 3
    return 4



def main():
    plays = []
    rank = 0
    part1 = 0
    part2 = 0
    global joker_rule

    for line in util.lines_from_file(sys.argv[1]):
        parts = line.strip().split(' ')
        plays.append({
            "cards": parts[0],
            "bid": int(parts[1])
        })

    for play in sorted(plays, key=cmp_to_key(compare_hands)):
        rank += 1
        part1 += rank * play["bid"]

    print(f"Part 1: {part1}")
    joker_rule = True
    rank = 0

    for play in sorted(plays, key=cmp_to_key(compare_hands)):
        rank += 1
        part2 += rank * play["bid"]

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
