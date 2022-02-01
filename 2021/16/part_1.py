lines = []

with open('2021/16/sample_input.txt') as file:
    ls = file.readlines()
    for line in ls:
        lines.append(line.strip())

hex_str = bin(int(lines[0], 16))

v = hex_str[:3]
t = hex_str[3:3]