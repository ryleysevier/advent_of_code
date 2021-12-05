import math

class vent:
    def __init__(self, val):
        self.value = val
        self.used = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        if self.value == 0:
            return '.'
        return str(self.value)

class grid:

    height = 1000
    width = 1000

    def __init__(self):
        self.matrix = []
        self.overlap = {}

        for y in range(0, grid.height):
            row = []
            for x in range(0, grid.width):
                row.append(vent(0))
            self.matrix.append(row)


    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        out = ''
        for x in self.matrix:
            for y in x:
                out = f'{out}{str(y)}'
            out = f'{out}\n'

        return out

    def add_vent(self, input:str):
        vals = input.split(',')
        x1 = int(vals[0])
        y2 = int(vals[2])
        vals = vals[1].split(' -> ')
        y1 = int(vals[0])
        x2 = int(vals[1])

        points = self.generate_points(x1,y1,x2,y2)
        for point in points:
            curr_val = self.matrix[point[1]][point[0]].value + 1
            self.check_high(curr_val, point[0], point[1])
            self.matrix[point[1]][point[0]].value = curr_val


    def generate_points(self, x1, y1, x2, y2):
        points = []
        up = (False, True)[y2 < y1]
        down = (False, True)[y1 < y2]
        right = (False, True)[x1 < x2]
        left = (False, True)[x2 < x1]

        dist_x = abs(x1-x2) + 1
        dist_y = abs(y1-y2) + 1

        curr_x = x1
        curr_y= y1

        # horizontal line
        if not up and not down:
            for i in range(0, dist_x):
                points.append((curr_x, curr_y))
                curr_x = (curr_x-1, curr_x+1)[right]
            return points

        # vertical line
        if not left and not right:
            for i in range(0, dist_y):
                points.append((curr_x, curr_y))
                curr_y = (curr_y-1, curr_y+1)[down]
            return points

        # diagonal
        if dist_x != dist_y:
            raise Exception()

        for i in range(0, dist_x):
            points.append((curr_x, curr_y))
            curr_x = (curr_x-1, curr_x+1)[right]
            curr_y = (curr_y-1, curr_y+1)[down]
        return points


    def check_high(self, new_val, x, y):
        if new_val > 1:
            self.overlap[f'{x},{y}'] = new_val
            


nums = []
boards = []

vents = grid()

with open('2021/5/input.txt') as file:
    while True:
        cur_line = file.readline()
        if not cur_line:
            break
        vents.add_vent(cur_line)
    
print(len(vents.overlap))
