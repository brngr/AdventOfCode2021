#!/bin/python3
import sys

#Formatting values
PURPLE_START = '\033[95m'
RED_START = '\033[91m'
BOLD_START = '\033[1m'
END = '\033[0m'



class number:
    def __init__(self,value):
        self.value=value
        self.drawn=False

class bingo_grid:
    def __init__(self,id,grid):
        self.id=id
        self.grid=[]
        self.undrawn=[]
        self.score=0
        self.won = False
        for c in grid:
            col=[]
            for n in c:
                col.append(number(n))
            self.grid.append(col)
    def show_grid(self):
        for c in self.grid:
            l = ''
            for n in c:
                if n.drawn == True:
                    l = l + ' ' + PURPLE_START + str(n.value) + END
                else:
                    l = l + ' ' +str(n.value)
            print(l)
        print()       

    def is_in_grid(self,number):
        for row in self.grid:
            for n in row:
                if n.value == number:
                    n.drawn = True
                    return True
        return False
    def check_row(self):
        for row in self.grid:
            bingo = True
            for n in row:
                if n.drawn == False:
                    bingo = False
                    break
            if bingo == True:
                return True
        return False

    def check_col(self):
        for i in range(0,len(self.grid[0])):
            bingo = True
            for n in self.grid:
                if n[i].drawn == False:
                    bingo = False
                    break
            if bingo == True:
                return True
        return False

    def check_bingo(self):
        if self.check_row() or self.check_col():
            #print(BOLD_START + RED_START + 'BINGO!' + END)
            #self.show_grid()
            self.get_sum()
            self.won = True
            return True

        return False
    def get_sum(self):
        for row in self.grid:
            for n in row:
                if n.drawn == False:
                    self.score+=n.value
        return

def play_bingo(draw,grids):
    winners = 0
    last_winner = 0
    for d in draw:
        for bg in grids:
            bg.is_in_grid(d)
            if bg.won == False:
                if bg.check_bingo():
                    winners+=1
                    last_winner = bg
                    if winners == len(grids):
                        return d*last_winner.score
    

def setup_bingo(puzzle_input):
    grid=[]
    grids=[]
    count=1
    draw=list(map(int,puzzle_input[0].split(',')))

    for i in range(2,len(puzzle_input)):
        if puzzle_input[i] == '\n':
            grids.append(bingo_grid(count,grid))
            grid=[]
            count+=1
        elif i == len(puzzle_input)-1:
            grid.append(list(map(int,puzzle_input[i].strip().replace('  ',' ').split(' '))))
            grids.append(bingo_grid(count,grid))
            count+=1
            grid=[]
        else:
            grid.append(list(map(int,puzzle_input[i].strip().replace('  ',' ').split(' '))))
    
    return draw,grids

def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(str,f.readlines()))
    f.close()
    bingo_draw,bingo_grids = setup_bingo(puzzle_input)
    score = play_bingo(bingo_draw,bingo_grids)
    print(score)
            


if __name__ == "__main__":
    main()
