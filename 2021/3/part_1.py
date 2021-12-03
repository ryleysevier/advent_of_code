data = []
with open('2021/3/input.txt') as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

# convert each row to an array then smoosh to 2d array
matrix = []
for d in data:
    matrix.append(list(d))

epp_out = []
gam_out = []
# it's an invert bit count for the second opp. just flip the bits after you get one
# iterate horizontally
for x in range(0, len(matrix[0])):
    ones = 0
    zeds = 0
    # iterate vertically
    for y in range(0, len(matrix)):
        curr_val = matrix[y][x]
        if curr_val == '0':
            zeds = zeds + 1
        else:
            ones = ones + 1
    epp_out.append((1,0)[ones < zeds])
    gam_out.append((0,1)[ones < zeds])

epsilon = 0
gamma = 0
for bit in epp_out:
    epsilon = (epsilon << 1) | bit

gamma = 0
for bit in gam_out:
    gamma = (gamma << 1) | bit

print(f'{epsilon} {gamma} {epsilon * gamma}')