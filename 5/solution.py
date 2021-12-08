#!/bin/python3
import sys



class line:
    def __init__(self, xy1,xy2):
        self.x1 = xy1[0]
        self.y1 = xy1[1]
        self.x2 = xy2[0]
        self.y2 = xy2[1]
        self.horizontal = False
        self.vertical = False
        self.points = []
        if self.x1 == self.x2:
            self.horizontal = True
        if self.y1 == self.y2:
            self.vertical = True
        self.points = self.get_points()

        
    def get_points(self):
        x = 0
        y = 0
        point = []
        points = []
        if self.horizontal:
            x = self.x1
            if self.y1 < self.y2:
                coord_range = range(self.y1,self.y2 + 1)
            elif self.y1 > self.y2:
                coord_range = range(self.y2,self.y1 + 1)
            for i in coord_range:
                point=[x,i]
                points.append(point)
        if self.vertical:
            y = self.y1
            if self.x1 < self.x2:
                coord_range = range(self.x1,self.x2 + 1)
            elif self.x1 > self.x2:
                coord_range = range(self.x2,self.x1 + 1)
            for i in coord_range:
                point=[i,y]
                points.append(point)
        return points

def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(str,f.readlines()))
    f.close()
    buffer=[]
    lines=[]
    for p in puzzle_input:
        buffer.append(p.strip().split(" -> "))
    for b in buffer:  
        xy1 = list(map(int,b[0].split(',')))  
        xy2 = list(map(int,b[1].split(',')))
        lines.append(line(xy1,xy2))

    points = []
    for l in lines:
        #print(l.points)
        for p in l.points:
            points.append(p)

    counted = []

    for i in range(0,len(points)):
        if len(points[i]) < 3 and points[i] not in counted:
            points[i].append(1)
            #print(str(i) + '/' + str(len(points)))
            if i == 4579:
                print(str(i) + '/' + str(len(points)))
        for j in range(i+1,len(points)):
            #if i == 4579:
            #    print(points[i][0],points[j][0],points[i][1],points[j][1])
            if points[i] not in counted and points[i][0] == points[j][0] and  points[i][1] == points[j][1]:
                print(points[i])
                points[i][2] = points[i][2] + 1
                if points[j] not in counted:
                    counted.append(points[j])

    total = 0
    for p in points:
        if len(p) == 3:
            if p[2] > 1:
                total = total + 1
    print(total)
if __name__ == "__main__":
    main()


#4579/108178
#[105, 241]
#Traceback (most recent call last):
#  File "./solution.py", line 90, in <module>
#    main()
#  File "./solution.py", line 79, in main
#    points[i][2] = points[i][2] + 1
#IndexError: list index out of range