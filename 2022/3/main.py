def score(o):
    o = ord(o) 
    if o > 97: return o - 96
    return o - 64 + 26

def p1(data):
    p = 0
    for d in data:
        l = d[:int(len(d)/2)]
        r = d[-int(len(d)/2):]
        b = set(l).intersection(set(r))
        p += score(ord(list(b)[0]))
        
    return p

def p2(data):
    p = 0
    for r in range(0, int(len(data)/3)):
        i = r*3
        a = data[i]
        b = data[i+1]
        c = data[i+2]

        x = set(a).intersection(set(b))
        y = x.intersection(set(c))
        p += score(ord(list(b)[0]))
        
    return p


sample = []
with open('./2022/3/sample_input.txt') as file:
    sample = file.readlines()
    sample = [line.rstrip() for line in sample]

data = []
with open('./2022/3/input_1.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

print(p1(sample))
print(p1(data))
print(p2(sample))
print(p2(data))