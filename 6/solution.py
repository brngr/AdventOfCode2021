#!/bin/python3
import sys


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(int, f.readlines()[0].split(",")))
    f.close()
    school = puzzle_input

    period = 80
    day = 1
    print(school)
    while day <= period:

        for i in range(0, len(school)):
            if school[i] == 0:
                school[i] = 6
                school.append(8)
            elif 1 <= school[i]:
                school[i] -= 1

        # print(school)
        day += 1
    print(len(school))


if __name__ == "__main__":
    main()
