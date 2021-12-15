

from queue import PriorityQueue 

class VNode:
    def __init__(self):
        self.val = 9


class Node(VNode):
    def __init__(self, val, name):
        self.name = name
        self.val = val
        self.visited = False
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.nodes = []

    def __ge__(self, other):
            if self.val>=other.val:
                return True
            else:
                return False
    def __lt__(self, other):
            if self.val < other.val:
                return True
            else:
                return False


class SNode:
    def __init__(self):
        self.start_node = None
        self.bottom_left = None
        self.bottom_right = None
        self.size = 0
        self.name_counter = 1
        self.nodes = []
        self.visited = []
        self.v = None
        self.edges = []
        self.visited = []


    def add_right(self, v):
        # if
        self.size += 1

        if self.start_node is None:
            self.start_node = Node(v, self.name_counter)
            self.name_counter += 1
            self.nodes.append(self.start_node)
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        new_node = Node(v, self.name_counter)
        self.name_counter += 1
        self.nodes.append(new_node)

        self.bottom_right.right = new_node
        self.bottom_right.nodes.append(new_node)
        new_node.left = self.bottom_right
        new_node.nodes.append(self.bottom_right)


        # if it's not a top rop, update up/down
        if isinstance(self.bottom_right.up, Node):
            n = self.bottom_right.up.right
            new_node.up = n
            new_node.nodes.append(n)
            n.down = new_node
            n.nodes.append(new_node)

        self.bottom_right = new_node\


    def add_down(self, v):
        # if
        self.size += 1

        if self.start_node is None:
            self.start_node = Node(v, self.name_counter)
            self.name_counter += 1
            self.nodes.append(self.start_node)
            self.bottom_right = self.start_node
            self.bottom_left = self.start_node
            return
        
        n = self.bottom_left

        new_node = Node(v, self.name_counter)
        self.name_counter += 1
        self.nodes.append(new_node)
        
        n.down = new_node
        n.nodes.append(new_node)
        new_node.up = n
        new_node.nodes.append(n)
        self.bottom_left = new_node
        self.bottom_right = new_node


    def init_graph(self):

        self.v = self.size
        self.edges = {}
        self.visited = []
        for n in self.nodes:
            for e in n.nodes:
                self.add_edge(n, e, e.val)

    def add_edge(self, u, v, weight):
        if self.edges.get(u.name) is None:
            self.edges[u.name] = {}
        if self.edges.get(v.name) is None:
            self.edges[v.name] = {}
        
        self.edges[u.name][v.name] = weight


def dijkstra(graph, start_vertex):
    D = {v.name:float('inf') for v in graph.nodes}
    D[start_vertex.name] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in graph.nodes:
            cv = graph.edges.get(current_vertex.name)
            nv = cv.get(neighbor.name, -1)
            if nv != -1:
                distance = graph.edges[current_vertex.name][neighbor.name]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor.name]
                    new_cost = D[current_vertex.name] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor.name] = new_cost
    return D


grid = SNode()

with open('2021/15/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        grid.add_down(int(line[0]))
        for c in [int(c) for c in line.strip()[1:]]:
            grid.add_right(c)

grid.init_graph()
res = dijkstra(grid, grid.start_node)

print(res[grid.name_counter-1])
exit()
#N OT 383 - too low
# NOT 390 - too low
# NOT 284
