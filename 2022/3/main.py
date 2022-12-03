def p1(data):
    p = 0
    for d in data:
        l = d[:int(len(d)/2)]
        r = d[-int(len(d)/2):]
        b = set(l).intersection(set(r))
        o = ord(list(b)[0]) 
        if o > 97: p += o - 96
        else: p += o - 64 + 26
        
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