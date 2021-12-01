#!/bin/python3
import sys


def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(int,f.readlines()))
    f.close()

if __name__ == "__main__":
    main()
