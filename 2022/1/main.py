def p1(data):
    o = [0]
    i = 0
    largest = i
    for d in data:
        if d == '': 
            if o[i] > o[largest]: largest = i
            o.append(0)
            i+=1 
            continue
        o[i]+= int(d)
    return(largest, o[largest])


def p2(data):
    o = [0]
    i = 0
    for d in data:
        if d == '': 
            o.append(0)
            i+=1 
            continue
        o[i]+= int(d)
    o.sort()
    return(sum(o[-3:]))


sample = []
with open('sample_input.txt') as file:
    sample = file.readlines()
    sample = [line.rstrip() for line in sample]

data = []
with open('input_1.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

print(p1(sample))
print(p1(data))
print(p2(sample))
print(p2(data))