
data = []
with open('day1_input.txt') as file:
    data = file.readlines()
    data = [int(line.rstrip()) for line in data]
    print(len(data))

inc = 0

for x in range(3, len(data)):
    prev_win = data[x-1] + data[x-2] + data[x-3]
    curr_win = data[x-1] + data[x-2] + data[x]
    if curr_win > prev_win:
        inc = inc + 1

print(f'inc: {inc}')

# boofed the type on the inputs. same as day 1
