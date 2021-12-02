data = []
with open('2021/2/input.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]
    print(len(data))

forward = 0
depth = 0
aim = 0

for x in data:
    curr = str(x).split(' ')
    if curr[0] == 'forward':
        forward = forward + int(curr[1])
        depth_adj = aim * int(curr[1])
        depth = depth + depth_adj
    if curr[0] == 'up':
        aim = aim - int(curr[1])
    if curr[0] == 'down':
        aim = aim + int(curr[1])
    print(f'{x} - forward: {forward}, depth: {depth}, aim: {aim}')

print(f'forward: {forward}, depth: {depth}, res: {depth * forward}')