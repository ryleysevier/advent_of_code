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


data = []
with open('sample_input.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

print(p1(data))

data = []
with open('input_1.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

print(p1(data))