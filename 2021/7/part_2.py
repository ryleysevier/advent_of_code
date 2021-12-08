with open('2021/7/input.txt') as file:
    starting_school_str = file.readline().split(',')
    crab_pos = [int(numeric_string) for numeric_string in starting_school_str]

current_position = 0
# position, fuel consumption
lowest_fuel_usage = (None, None)

mean = sum(crab_pos) / len(crab_pos)

crab_pos.sort()
low = crab_pos[0]
high = crab_pos[len(crab_pos)-1]
print(f'{mean}')

target = 0
gas = 0

lowest = 999999999

for y in range(low, high):
    gas = 0
    for x in range(0, len(crab_pos)):
        dist = abs(y-crab_pos[x])
        used = 0
        for j in range(1, dist + 1):
            used = used + j
        gas = gas + used
    if gas < lowest:
        lowest = gas
print(f'{lowest}')
