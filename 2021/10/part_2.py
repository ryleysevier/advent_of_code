score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

key = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

lines = []
corruption_points = 0
a_c_points = []
with open('2021/10/input.txt') as file:
    all_lines = file.readlines()
    stack = []

    for line in all_lines:
        try:
            stack = []
            li = list(line.rstrip())
            
            # corrupted
            for l in li:
                if l in ['(', '[', '{', '<']:
                    stack += l
                else:
                    val = stack.pop()
                    if key[val] != l:
                        raise Exception(l)
            
            # incomplete
            if len(stack) != 0:
                s = 0
                a_c = []
                for i in range(1, len(stack)+1):
                    c = stack[i*-1]
                    k = key[c]
                    a_c += k
                    s = s * 5
                    s += score[k]
                a_c_points.append(s)

        except Exception as val:
            pass

a_c_points.sort()
print(a_c_points[int(len(a_c_points) / 2)])
