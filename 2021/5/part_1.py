class vent:
    def __init__(self, val):
        self.value = val
        self.used = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        if self.value == 0:
            return '.'
        return self.value

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
                out = f'{out}{y.value}'
            out = f'{out}\n'

        return out

    def add_vent(self, input:str):
        vals = input.split(',')
        x1 = int(vals[0])
        y2 = int(vals[2])
        vals = vals[1].split(' -> ')
        y1 = int(vals[0])
        x2 = int(vals[1])

        if x1 == x2:
            low = (y1,y2)[y1 >= y2]
            high = (y1,y2)[y1 <= y2]
            for i in range(low, high+1):
                curr_val = self.matrix[i][x1].value + 1
                self.check_high(curr_val, i, x1)
                self.matrix[i][x1].value = curr_val
            return

        if y1 == y2:
            low = (x1,x2)[x1 >= x2]
            high = (x1,x2)[x1 <= x2]
            for i in range(low, high+1):
                curr_val = self.matrix[y1][i].value + 1
                self.check_high(curr_val, y1, i)
                self.matrix[y1][i].value = curr_val
            return
        
        return

    def check_high(self, new_val, x,y):
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
    
print(vents)
print(len(vents.overlap))
