#!/usr/bin/python

import itertools
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # ********* Naive Solution *********
    # items.sort(key=lambda x: x.value, reverse=True)

    # sack = []
    # cur_weight = 0
    # for i in range(len(items)):
    #     if cur_weight + items[i].weight <= capacity:
    #         sack.append(items[i])

    # return sack

    # ********* Brute Force Solution *********
    # max_value = -1
    # best_comnbo = None

    # for i in range(1, len(items) + 1):
    #     list_of_combos = list(combinations(items, i))

    #     for combo in all_combos:
    #         # weight of entire combo
    #         weight = 0
    #     for item in combo:
    #         value += item.value
    #         weight += item.weight
    #         # Can fit
    #         if weight <= capacity:
    #             if value > max_value:
    #                 max_value = value
    #                 best_comnbo = combo

    #     for combo in list_of_combos:
    #         all_combos.append(combo)

    # return best_comnbo

    # ********* Greedy Solution *********
    for i in items:
        i.efficiency = i.value / i.weight

    items.sort(key=lambda x: x.efficiency, reverse=True)

    sack = []
    weight = 0

    for i in items:
        weight += i.weight
        if weight > capacity:
            return sack
        else:
            sack.append(i)
    return sack


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
