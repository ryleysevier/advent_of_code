class VNode:
    def __init__(self):
        self.val = 9

    def __repr__(self) -> str:
        return "*9"

class Node(VNode):
    def __init__(self, val):
        self.val = val
        self.up = VNode()
        self.right = VNode()
        self.down = VNode()
        self.left = VNode()
        self.flashed = False

    def __repr__(self) -> str:
        return str(self.val)

class SNode:
    def __init__(self):
        self.start_node = None
        self.bottom_left = None
        self.bottom_right = None
        self.size = 0
        self.flashes = 0
        self.step_flash = 0

    def __str__(self):
        retval = ''
        row = self.start_node
        curr_node = row
        more_rows = True
        while more_rows:
            #iterate the cols
            more_cols = True
            while more_cols:
                retval = retval + str(curr_node.val)
                if isinstance(curr_node.right, Node):
                    curr_node = curr_node.right
                else:
                    more_cols = False

            if isinstance(row.down, Node):
                retval = retval + '\n'
                row = row.down
                curr_node = row
            else:
                more_rows = False
        return retval

    def day(self):
        # increment everyones value + 1
        will_flash = []
        self.step_flash = 0
        row = self.start_node
        curr_node = row
        more_rows = True
        while more_rows:
            #iterate the cols
            more_cols = True
            while more_cols:
                curr_node.flashed = False
                curr_node.val += 1
                if curr_node.val > 9:
                    will_flash.append(curr_node)
                if isinstance(curr_node.right, Node):
                    curr_node = curr_node.right
                else:
                    more_cols = False

            if isinstance(row.down, Node):
                row = row.down
                curr_node = row
            else:
                more_rows = False
        #iterate to next row
        for n in will_flash:
            self.flash(n)

    def energize(self, n):
        if not n.flashed:
            n.val += 1
            if n.val > 9:
                self.flash(n)

    def flash(self, n):
        if not n.flashed:
            n.flashed = True
            self.step_flash += 1
            self.flashes += 1
            n.val = 0

            if isinstance(n.up, Node):
                self.energize(n.up)
                if isinstance(n.up.right, Node):
                    self.energize(n.up.right)

            if isinstance(n.right, Node):
                self.energize(n.right)
                if isinstance(n.right.down, Node):
                    self.energize(n.right.down)

            if isinstance(n.down, Node):
                self.energize(n.down)
                if isinstance(n.down.left, Node):
                    self.energize(n.down.left)

            if isinstance(n.left, Node):
                self.energize(n.left)
                if isinstance(n.left.up, Node):
                    self.energize(n.left.up)

    def add_right(self, v):
        # if
        self.size += 1

        if self.start_node is None:
            self.start_node = Node(v) 
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        new_node = Node(v)
        self.bottom_right.right = new_node
        new_node.left = self.bottom_right


        # if it's not a top rop, update up/down
        if isinstance(self.bottom_right.up, Node):
            n = self.bottom_right.up.right
            new_node.up = n
            n.down = new_node

        self.bottom_right = new_node


    def add_down(self, v):
        # if
        self.size += 1

        if self.start_node is None:
            self.start_node = Node(v) 
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        n = self.bottom_left
        new_node = Node(v)
        n.down = new_node
        new_node.up = n
        self.bottom_left = new_node
        self.bottom_right = new_node


grid = SNode()

with open('2021/11/sample_input.txt') as file:
    lines = file.readlines()
    for line in lines:
        grid.add_down(int(line[0]))
        for c in [int(c) for c in line.strip()[1:]]:
            grid.add_right(c)
        
for d in range(0,500):
    # flash
    grid.day()
    if grid.step_flash == grid.size:
        print(grid)
        print(d)
        exit()