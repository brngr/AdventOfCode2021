#!/bin/python3
import sys
from typing import KeysView


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()

    for i in range(0, len(puzzle_input)):
        puzzle_input[i] = puzzle_input[i].strip()

    count_1 = []
    count_0 = []
    for j in range(0, len(puzzle_input[0])):
        count_1.append(0)
        count_0.append(0)

    for p in puzzle_input:
        for k in range(0, len(p)):
            if p[k] == "1":
                count_1[k] = count_1[k] + 1
            elif p[k] == "0":
                count_0[k] = count_0[k] + 1

    gamma = ""
    epsilon = ""
    for l in range(0, len(count_1)):
        if count_1[l] > count_0[l]:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)


if __name__ == "__main__":
    main()
