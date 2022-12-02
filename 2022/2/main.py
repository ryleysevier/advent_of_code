class node:
    def __init__(self, points):
        self.beats = None
        self.points = points

def score(a,b):
    r = node(1)
    p = node(2)
    s = node(3)
    r.beats = s
    p.beats = r
    s.beats = p

    g = {
        'A': r, # rock
        'X': r, 
        'B': p, # paper
        'Y': p, 
        'C': s, # scissors
        'Z': s, 
    }

    # tie
    if g[a] == g[b]: return 3 + g[b].points
    if g[a].beats == g[b]: return g[b].points
    if g[b].beats == g[a]: return g[b].points + 6


def p1(data):
    scores = []
    for d in data:
        i = d.split(' ')
        s = scores.append(score(i[0], i[1]))
    return sum(scores)


sample = []
with open('./2022/2/sample_input.txt') as file:
    sample = file.readlines()
    sample = [line.rstrip() for line in sample]

data = []
with open('./2022/2/input_1.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

print(p1(sample))
print(p1(data))