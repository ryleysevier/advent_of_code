score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
points = 0
with open('2021/10/input.txt') as file:
    all_lines = file.readlines()
    stack = []

    for line in all_lines:
        try:
            stack = []
            li = list(line.rstrip())
            
            # incomplete
            for l in li:
                if l in ['(', '[', '{', '<']:
                    stack += l
                else:
                    val = stack.pop()
                    if key[val] != l:
                        raise Exception(l)
        except Exception as val:
            points += score[str(val)]
print(points)
