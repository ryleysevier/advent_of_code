class num:
    def __init__(self, val):
        self.value = val
        self.used = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f'{("~", "!")[self.used]}{self.value}'

class grid:
    def __init__(self, r1, r2, r3, r4, r5):
        self.matrix = []
        self.won = False
        self.matrix.append(self.make_row([i for i in r1.split(' ') if i != ' ' and i]))
        self.matrix.append(self.make_row([i for i in r2.split(' ') if i != ' ' and i]))
        self.matrix.append(self.make_row([i for i in r3.split(' ') if i != ' ' and i]))
        self.matrix.append(self.make_row([i for i in r4.split(' ') if i != ' ' and i]))
        self.matrix.append(self.make_row([i for i in r5.split(' ') if i != ' ' and i]))


    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return self.matrix

    def make_row(self, row):
        o = []
        for r in row:
            o.append(num(r))
        return o


    def use_num(self, val):
        for r in self.matrix:
            for c in r:
                if c.value == val:
                    c.used = True


    def check_winner(self):
        #check horizontal
        for r in self.matrix:
            h_win = True
            for h in r:
                if not h.used:
                    h_win = False
            if h_win:
                self.won = True
                return True
        
        # iterate vertically
        for x in range(0, len(self.matrix[0])):
            v_win = True
            for y in range(0, len(self.matrix)):
                if not self.matrix[y][x].used:
                    v_win = False
            if v_win:
                return True


    def get_unmarked(self):
        score = 0
        for r in self.matrix:
            for c in r:
                if not c.used:
                    score = score + int(c.value)
        return score


nums = []
boards = []


with open('2021/4/input.txt') as file:
    nums = file.readline().split(',')
    
    more = True
    while more:
        empty = file.readline()
        if not empty:
            more = False
        else:
            boards.append(
                grid(
                    file.readline().strip(), 
                    file.readline().strip(), 
                    file.readline().strip(), 
                    file.readline().strip(), 
                    file.readline().strip()))

iter_board = boards
for draw in nums:
    losers = []
    for b in iter_board:
        b.use_num(draw)
    
    for b in iter_board:
        if b.check_winner():
            print(int(draw) * b.get_unmarked())
        else:
            losers.append(b)
    iter_board = losers