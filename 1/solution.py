#!/bin/python3
import sys


def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(int,f.readlines()))
    f.close()
    increased = 0
    previous_window = -1
    sum_window = 0
    for i in range(0,len(puzzle_input)-2):
        sum_window = puzzle_input[i] + puzzle_input[i+1] + puzzle_input[i+2]
        if previous_window != -1 and sum_window > previous_window:
            increased = increased + 1
        previous_window = sum_window

    print(increased)
if __name__ == "__main__":
    main()