#data = [
#    199, 200, 208, 210, 200, 207, 240, 269, 260, 263
#]

data = []
with open('day1_input.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]
    print(len(data))

inc = 0
dec = 0

for x in range(1, len(data)):
    if int(data[x]) > int(data[x-1]):
        inc = inc + 1

print(f'inc: {inc}')