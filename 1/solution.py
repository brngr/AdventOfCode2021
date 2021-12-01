#!/bin/python3
import sys


def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(int,f.readlines()))
    f.close()
    increased = 0
    for i in range(1,len(puzzle_input)):
        #print(puzzle_input[i])
        if puzzle_input[i] > puzzle_input[i-1]:
            increased = increased + 1
    print(increased)
if __name__ == "__main__":
    main()