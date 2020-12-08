f = open("input_data.txt", "r")
data = f.read().split("\n")
data = [x.split(" ") for x in data]
idx = list(range(len(data)))
data = {x: data[x] for x in idx}


def get_accumulator_count(data):
    time_to_stop = False
    index_counter = 0
    accumulator = 0
    executed_instruction = []
    while not time_to_stop:
        instruction = data[index_counter]
        if index_counter in executed_instruction:
            return accumulator
        executed_instruction.append(index_counter)
        if instruction[0] == "nop":
            index_counter += 1
        if instruction[0] == "acc":
            accumulator += int(instruction[1])
            index_counter += 1
        if instruction[0] == "jmp":
            index_counter += int(instruction[1])


print(get_accumulator_count(data))

# Part 2
list_of_nop_index = []
list_of_jmp_index = []

for i in list(range(len(data))):
    if data[i][0] == "nop":
        list_of_nop_index.append(i)
    elif data[i][0] == "jmp":
        list_of_jmp_index.append(i)


def part2(data, switch_index):
    max_index = 630
    time_to_stop = False
    index_counter = 0
    accumulator = 0
    executed_instruction = []
    while not time_to_stop:
        instruction = data[index_counter]
        executed_instruction.append(index_counter)
        move_to_make = instruction[0]
        if index_counter == switch_index:
            if move_to_make == "nop":
                move_to_make = "jmp"
            elif move_to_make == "jmp":
                move_to_make = "nop"
        if move_to_make == "nop":
            index_counter += 1
            if index_counter >= max_index:
                return index_counter, accumulator
        if move_to_make == "acc":
            accumulator += int(instruction[1])
            index_counter += 1
            if index_counter >= max_index:
                return index_counter, accumulator
        if move_to_make == "jmp":
            index_counter += int(instruction[1])
            if index_counter >= max_index:
                return index_counter, accumulator
        if index_counter in executed_instruction:
            time_to_stop = True


for jmp_index in list_of_jmp_index:
    tmp = part2(data, jmp_index)
    if tmp is not None:
        print(tmp)
