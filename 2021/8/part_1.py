lines = []
with open('2021/8/input.txt') as file:
    entries = file.readlines()
    for entry in entries:
        in_out = entry.rstrip().split(' | ')
        lines.append((in_out[0].split(' '), in_out[1].split(' ')))

count = 0
for x in lines:
    for y in x[0]:
        if len(y) in [2,3,4, 7]:
            count += 1

print(count)
