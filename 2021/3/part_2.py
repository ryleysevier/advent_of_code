def find_rating(matrix, get_most_common, curr_col=0):
    # base case
    if len(matrix) == 1:
        return matrix[0]

    ones = [], zeds = []
    # iterate vertically
    for y in range(0, len(matrix)):
        curr_val = matrix[y][curr_col]
        if curr_val == '0':
            zeds.append(matrix[y])
        else:
            ones.append(matrix[y])

    if get_most_common:
        return find_rating((zeds,ones)[len(ones) >= len(zeds)], get_most_common, curr_col + 1)
    return find_rating((zeds,ones)[len(ones) < len(zeds)], get_most_common, curr_col + 1)


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

oxy = find_rating(matrix, True)
co2 = find_rating(matrix, False)

o2_rating = 0
for bit in oxy:
    o2_rating = (o2_rating << 1) | int(bit)

co2_rating = 0
for bit in co2:
    co2_rating = (co2_rating << 1) | int(bit)

print(f'{o2_rating} {co2_rating} {o2_rating * co2_rating}')