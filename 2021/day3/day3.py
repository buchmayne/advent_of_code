import os

f = open(os.path.expanduser("~/Desktop/input_data.txt"), "r")
data = [x.split("\n")[0] for x in f]

p1_solution = {i: 0 for i in range(len(data[0]))}

container = {}

for i in range(len(data[0])):
    its_a_zero = 0
    for sequence in data:
        if sequence[i] == '0':
            its_a_zero += 1

    container[i] = its_a_zero

first_container = container.copy()
second_container = container.copy()

for key, values in first_container.items():
    if first_container[key] > 500:
        first_container[key] = '0'
        second_container[key] = '1'
    else:
        first_container[key] = '1'
        second_container[key] = '0'


first_binary_string = ''
second_binary_string = ''

for x in first_container.values():
    first_binary_string = first_binary_string + x

for x in second_container.values():
    second_binary_string = second_binary_string + x

print(f"Part 1 Solution: {int(first_binary_string, 2) * int(second_binary_string, 2)}")


count_observations = len(data)
bit_locations = len(data[0])

keepers_1 = []
for idx in range(bit_locations):
    if idx == 0:
        count_of_ones = 0
        count_of_zeroes = 0
        for char in data:
            if char[idx] == '1':
                count_of_ones += 1
            else:
                count_of_zeroes += 1

        if count_of_ones >= count_of_zeroes:
            target_val = '1'
        else:
            target_val = '0'

        new_universe = data.copy()
        keeping = []

        for i in range(len(new_universe)):
            if new_universe[i][idx] == target_val:
                keeping.append(new_universe[i])
    else:
        count_of_ones = 0
        count_of_zeroes = 0
        for char in keeping:
            if char[idx] == '1':
                count_of_ones += 1
            else:
                count_of_zeroes += 1

        if count_of_ones >= count_of_zeroes:
            target_val = '1'
        else:
            target_val = '0'

        new_universe = keeping.copy()
        keeping = []

        for i in range(len(new_universe)):
            if new_universe[i][idx] == target_val:
                keeping.append(new_universe[i])

        if len(keeping) == 1:
            keepers_1.append(keeping[0])


p2_1_answer = int(list(set(keepers_1))[0], 2)


keepers_2 = []
for idx in range(bit_locations):
    if idx == 0:
        count_of_ones = 0
        count_of_zeroes = 0
        for char in data:
            if char[idx] == '1':
                count_of_ones += 1
            else:
                count_of_zeroes += 1

        if count_of_zeroes <= count_of_ones:
            target_val = '0'
        else:
            target_val = '1'

        new_universe = data.copy()
        keeping = []

        for i in range(len(new_universe)):
            if new_universe[i][idx] == target_val:
                keeping.append(new_universe[i])
    else:
        count_of_ones = 0
        count_of_zeroes = 0
        for char in keeping:
            if char[idx] == '1':
                count_of_ones += 1
            else:
                count_of_zeroes += 1

        if count_of_zeroes <= count_of_ones:
            target_val = '0'
        else:
            target_val = '1'

        new_universe = keeping.copy()
        keeping = []

        for i in range(len(new_universe)):
            if new_universe[i][idx] == target_val:
                keeping.append(new_universe[i])

        if len(keeping) == 1:
            keepers_2.append(keeping[0])


p2_2_answer = int(list(set(keepers_2))[0], 2)

print(f"Part 2 Solution: {p2_1_answer * p2_2_answer}")