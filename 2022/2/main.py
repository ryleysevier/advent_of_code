class node:
    def __init__(self, points):
        self.beats = None
        self.ties = None
        self.loses = None
        self.points = points
    
    def setup(self, beats, loses):
        self.beats = beats
        self.ties = self
        self.loses = loses

r = node(1)
p = node(2)
s = node(3)
r.setup(s, p)
p.setup(r, s)
s.setup(p, r)


def score(a,b):
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


def predict(a,b):
    g = {
        'A': r, # rock
        'B': p, # paper
        'C': s, # scissors 
    }

    if b == 'Y': return 3 + g[a].ties.points
    if b == 'X': return g[a].beats.points
    if b == 'Z': return 6 + g[a].loses.points


def p1(data):
    scores = []
    for d in data:
        i = d.split(' ')
        s = scores.append(score(i[0], i[1]))
    return sum(scores)


def p2(data):
    scores = []
    for d in data:
        i = d.split(' ')
        s = scores.append(predict(i[0], i[1]))
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
print(p2(sample))
print(p2(data))