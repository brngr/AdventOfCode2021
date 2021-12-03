#!/bin/python3
import sys
import cProfile
def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()

    oxygen = []
    scrubber = []
    for i in range(0, len(puzzle_input)):
        puzzle_input[i] = puzzle_input[i].strip()
        oxygen.append(puzzle_input[i])
        scrubber.append(puzzle_input[i])

    for i in range(0,len(puzzle_input[0])):
        count_0=0
        count_1=0
        oxygen.sort(key = lambda x: x[i])
        scrubber.sort(key = lambda y: y[i])
        if len(oxygen) > 1:
            for j in range(0,len(oxygen)):
                if oxygen[j][i] == '0':
                    count_0+=1
                if oxygen[j][i] == '1':
                    count_1+=1
            if count_0 and count_1 != 0:
                if count_0 > count_1:
                    oxygen = oxygen[0:count_0]
                if count_1 >= count_0:
                    oxygen = oxygen[count_0:len(oxygen)]
        count_0=0
        count_1=0
        if len(scrubber) > 1:
            for k in range(0,len(scrubber)):
                if scrubber[k][i] == '0':
                    count_0+=1
                if scrubber[k][i] == '1':
                    count_1+=1
            if count_0 and count_1 != 0: 
                if count_0 <= count_1:
                    scrubber = scrubber[0:count_0]
                if count_1 < count_0:
                    scrubber = scrubber[count_0:len(scrubber)]
    print(int(oxygen[0],2)*int(scrubber[0],2))

if __name__ == "__main__":
    #main()
    cProfile.run("main()")
