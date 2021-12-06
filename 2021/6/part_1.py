class fish:
    def __init__(self, val):
        self.value = val
        self.mature = True

    def age(self):
        if self.value == 0:
            self.value = 6
            return True

        self.value = self.value - 1
        return False
        

class school:

    def __init__(self, fishies):
        self.fishes = []
        for f in fishies:
            self.fishes.append(fish(f))

    def day(self):
        new_fish = []
        for f in self.fishes:
            new = f.age()
            if new:
                new_fish.append(fish(8))
        self.fishes.extend(new_fish)
        


with open('2021/6/input.txt') as file:
    starting_school_str = file.readline().split(',')
    starting_school = [int(numeric_string) for numeric_string in starting_school_str]

school_of_fish = school(starting_school)

for i in range(1,81):
    school_of_fish.day()
    print(f'Day {i}: {len(school_of_fish.fishes)}')