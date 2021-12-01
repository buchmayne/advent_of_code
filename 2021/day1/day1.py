f = open("input_data.txt", "r")
data = f.read().split("\n")

data = [int(num) for num in data]

part1_count = 0

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        part1_count += 1

part2_count = 0

for i in range(2, len(data) - 1):
    sum1 = data[i] + data[i - 1] + data[i - 2]
    sum2 = data[i + 1] + data[i] + data[i - 1]
    if sum2 > sum1:
        part2_count += 1


print(f"Part 1 Solution: {part1_count}\nPart 2 Solution: {part2_count}")
