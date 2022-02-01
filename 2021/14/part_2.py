'''
Refactor into a Rope 
https://en.wikipedia.org/wiki/Rope_(data_structure)
'''

comps = {}
init = ''
with open('2021/14/input.txt') as file:
    lines = file.readlines()
    init = lines[0].strip()

    for line in lines[2:]:
        form = line.strip().split(' -> ')
        comps[form[0]] = form[1]

print(init)

steps = 40
for x in range(0, steps):
    print(x)
    length = len(init)
    looping = True
    i = 0
    while looping:
        window = init[i:i+2]
        insertion = comps.get(window, None)
        if insertion is not None:
            pre = init[:i+1]
            post = init[i+1:]
            init = pre + insertion + post
            i += 1

        if i == len(init):
            looping = False
        i += 1

char_list = ''.join(set(init))
counts = []
for c in list(char_list):
    counts.append(init.count(c))
counts.sort()
print(f'{counts[-1] - counts[0]}')