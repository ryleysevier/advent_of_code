with open('2021/6/input.txt') as file:
    starting_school_str = file.readline().split(',')
    starting_school = [int(numeric_string) for numeric_string in starting_school_str]

ages = [0,0,0,0,0,0,0,0,0]

for x in starting_school:
    ages[x] = ages[x] + 1

print(f'Day 0: {sum(ages)}')

for i in range(1,257):
    new_ages = [0,0,0,0,0,0,0,0,0]
    for x in range(0, len(ages)):
        # no fish in the bucket, move along
        if ages[x] == 0:
            continue

        if x == 0:
            #reset the fish
            new_ages[6] = new_ages[6] + ages[x]
            #create the fish
            new_ages[8] = new_ages[8] + ages[x]
        else:
            new_ages[x-1] = new_ages[x-1] + ages[x]
    ages = new_ages 
    print(f'Day {i}: {sum(ages)}')

