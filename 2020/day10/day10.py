f = open("input_data.txt", "r")
data = f.read()
data = data.split("\n")
data = [int(x) for x in data]
data = sorted(data)

jolts = 0
one_jolt_diff = 0
three_jolt_diff = 1

for i in list(range(len(data))):
    diff_ = data[i] - jolts
    if diff_ == 1:
        one_jolt_diff += 1
    if diff_ == 3:
        three_jolt_diff += 1
    jolts = data[i]

part1_answer = one_jolt_diff * three_jolt_diff

print(part1_answer)

# Part 2
