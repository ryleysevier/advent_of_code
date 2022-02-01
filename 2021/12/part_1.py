class Node():
    def __init__(self, val):
        self.val = val
        self.edges = []

    def __repr__(self) -> str:
        return str(self.val)

nodes = {}

with open('2021/12/sample_input.txt') as file:
    lines = file.readlines()
    for line in lines:
        ns = line.strip().split('-')
        # check if either exists first
        n1 = nodes.get(ns[0], Node(ns[0]))
        n2 = nodes.get(ns[1], Node(ns[1]))
        # add connected nodes
        n1.edges.append(n2)
        n2.edges.append(n1)
        # add the to dict (overwriting if needed)
        nodes[ns[0]] = n1
        nodes[ns[1]] = n2

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, start_node):
    #modify bfs to not add capital letters to cave listing
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        s = queue.pop(0) 
        print (s.val, end = " ") 

        for neighbour in s.edges:
            if neighbour not in visited:
                if neighbour.val.islower():
                    visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,nodes['start'])