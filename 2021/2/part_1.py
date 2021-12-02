data = []
with open('2021/2/input.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]
    print(len(data))

y = 0
z = 0


for x in data:
    curr = str(x).split(' ')
    if curr[0] == 'forward':
        z = z + int(curr[1])
    if curr[0] == 'up':
        y = y - int(curr[1])
    if curr[0] == 'down':
        y = y + int(curr[1])

print(f'forward: {z}, depth: {y}, res: {z * y}')