#!/bin/python3
import sys


class line:
    def __init__(self, xy1, xy2):
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
                coord_range = range(self.y1, self.y2 + 1)
            elif self.y1 > self.y2:
                coord_range = range(self.y2, self.y1 + 1)
            for i in coord_range:
                point = [x, i]
                points.append(point)
        if self.vertical:
            y = self.y1
            if self.x1 < self.x2:
                coord_range = range(self.x1, self.x2 + 1)
            elif self.x1 > self.x2:
                coord_range = range(self.x2, self.x1 + 1)
            for i in coord_range:
                point = [i, y]
                points.append(point)
        return points


def main():
    grid_x_size = 0
    grid_y_size = 0

    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()
    buffer = []
    lines = []
    for p in puzzle_input:
        buffer.append(p.strip().split(" -> "))
    for b in buffer:
        xy1 = list(map(int, b[0].split(",")))
        xy2 = list(map(int, b[1].split(",")))
        lines.append(line(xy1, xy2))
        if xy1[0] > grid_x_size:
            grid_x_size = xy1[0]
        if xy2[0] > grid_x_size:
            grid_x_size = xy2[0]
        if xy1[1] > grid_x_size:
            grid_y_size = xy1[1]
        if xy2[1] > grid_x_size:
            grid_y_size = xy2[1]

    points = []
    for l in lines:
        # print(l.points)
        for p in l.points:
            points.append(p)

    # for i in range(0, len(points)):

    # print(grid_x_size, grid_y_size)
    grid = []
    row = []
    for i in range(0, grid_x_size):
        row.append(0)
    for i in range(0, grid_y_size):
        grid.append(row)
    for r in grid:
        print(r)


if __name__ == "__main__":
    main()
