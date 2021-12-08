#!/bin/python3
import sys


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(int, f.readlines()[0].split(",")))
    f.close()
    school = puzzle_input

    period = 256
    day = 1
    timers = []
    for i in range(0, 9):
        timers.append(0)
    for i in range(0, 9):
        timers[i] = school.count(i)
    while day <= period:
        new = timers.pop(0)
        timers[6] = timers[6] + new
        timers.append(new)
        day += 1
    print(sum(timers))


if __name__ == "__main__":
    main()
