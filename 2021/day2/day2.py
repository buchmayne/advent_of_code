f = open("input_data.txt", "r")
data = [x.split("\n") for x in f]

commands = [line[0] for line in data]

horizontal_position = 0
depth = 0

for command in commands:
    direction = command[0]
    value = int(command[-1])
    if direction == "f":
        horizontal_position += value
    elif direction == "d":
        depth += value
    elif direction == "u":
        depth -= value


p1_solution = horizontal_position * depth

# Part 2
horizontal_position = 0
depth = 0
aim = 0

for command in commands:
    direction = command[0]
    value = int(command[-1])
    if direction == "f":
        horizontal_position += value
        depth += value * aim
    elif direction == "d":
        aim += value
    elif direction == "u":
        aim -= value

p2_solution = horizontal_position * depth

print(f"Solution Part 1: {p1_solution}\nSolution Part 2: {p2_solution}")
