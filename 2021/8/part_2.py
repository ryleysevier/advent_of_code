def char_to_bits(str):
    d = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g':6
    }
    bits = ['0'] * 7
    cs = list(str)
    for c in cs:
        bits[d[c]] = '1'

    out = ''
    for bit in bits:
        out += bit
    return out

lines = []
with open('2021/8/sample_input.txt') as file:
    entries = file.readlines()
    for entry in entries:
        in_out = entry.rstrip().split(' | ')
        lines.append((in_out[0].split(' '), in_out[1].split(' ')))

count = 0
for x in lines:
    '''
     0000
    5    1
    5    1
     6666  
    4    2
    4    2
     3333

    0123456
    0000000
    abcdefg
    '''

    key = {}
    input = x[0]
    input.sort(key=len)
    bins = []
    for y in input:
        bins.append(char_to_bits(y))

    # add all possibilities for all values to each of their slots

    one = bins[0]
    seven = bins[1]
    four = bins[2]
    eight = bins[9]
    two_three_five = [bins[3], bins[4], bins[5]]
    zero_six_nine = [bins[6], bins[7], bins[8]]

    #b_0 = 1 xor 7
    b_0 = int(one, 2) ^ int(seven, 2)
    
    print(b_0)

print(count)