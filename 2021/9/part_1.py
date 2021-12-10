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
        self.add_low = False

    def __repr__(self) -> str:
        return str(self.val)

class SNode:
    def __init__(self):
        self.start_node = None
        self.bottom_left = None
        self.bottom_right = None
        self.lows = 0
    
    def get_right(self):
        n = self.start_node
        while not isinstance(n.right, VNode):
            n = n.right
        return n

    def update_node_low(self, n:Node):
        if n.val < n.up.val and \
            n.val < n.down.val and \
            n.val < n.left.val and \
            n.val < n.right.val:

            if not n.add_low:
                self.lows += 1 + n.val
                n.add_low = True
                return
            return
        
        if n.add_low:
            self.lows -= 1 + n.val
            n.add_low = False
            return

        return

    def add_right(self, v):
        # if
        if self.start_node is None:
            self.start_node = Node(v) 
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        new_node = Node(v)
        self.bottom_right.right = new_node
        new_node.left = self.bottom_right
        self.update_node_low(new_node.left)

        # if it's not a top rop, update up/down
        if isinstance(self.bottom_right.up, Node):
            n = self.bottom_right.up.right
            new_node.up = n
            n.down = new_node
            self.update_node_low(new_node.up)

        self.bottom_right = new_node
        self.update_node_low(new_node)

    def add_down(self, v):
        # if
        if self.start_node is None:
            self.start_node = Node(v) 
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        n = self.bottom_left
        new_node = Node(v)
        n.down = new_node
        new_node.up = n
        self.update_node_low(n)
        self.update_node_low(new_node)
        self.bottom_left = new_node
        self.bottom_right = new_node


grid = SNode()

with open('2021/9/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        grid.add_down(int(line[0]))
        for c in [int(c) for c in line.strip()[1:]]:
            grid.add_right(c)
        print(grid.lows)
        
print(grid.lows)