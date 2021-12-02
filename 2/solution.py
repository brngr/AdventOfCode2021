#!/bin/python3
import sys


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()
    commands = []
    tmp = []

    for p in puzzle_input:
        tmp = p.strip().split(" ")
        commands.append(tmp)

    horizontal = 0
    depth = 0
    aim = 0

    for c in commands:
        print(c)
        if c[0] == "forward":
            horizontal = horizontal + int(c[1])
            depth = depth + aim * int(c[1])
        if c[0] == "down":
            aim = aim + int(c[1])
        if c[0] == "up":
            aim = aim - int(c[1])
    result = horizontal * depth

    print(horizontal)
    print(depth)
    print(result)


if __name__ == "__main__":
    main()
