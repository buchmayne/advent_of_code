f = open("input_data.txt", "r")
data = f.read().split("\n")

elf_idx = 0
calories_counter = 0
max_observed_cals = 0
elf_calories = []

for i in range(len(data)):
    if data[i] != "":
        calories_counter += int(data[i])
    else:
        if calories_counter > max_observed_cals:
            max_observed_cals = calories_counter
        elf_calories.append(calories_counter)
        elf_idx += 1
        calories_counter = 0

if __name__ == "__main__":
    print(max_observed_cals, sum(sorted(elf_calories, reverse=True)[0:3]))
