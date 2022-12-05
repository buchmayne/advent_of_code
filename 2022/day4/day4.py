f = open("input_data.txt", "r")
data = f.read().split("\n")


example = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def solve_part_1(elf_pair):
    range_1, range_2 = elf_pair.split(",")
    min_1, max_1 = range_1.split("-")
    min_2, max_2 = range_2.split("-")
    range_1 = list(range(int(min_1), int(max_1) + 1))
    range_2 = list(range(int(min_2), int(max_2) + 1))
    if all(num in range_2 for num in range_1):
        return 1
    elif all(num in range_1 for num in range_2):
        return 1
    else:
        return 0


def solve_part_2(elf_pair):
    range_1, range_2 = elf_pair.split(",")
    min_1, max_1 = range_1.split("-")
    min_2, max_2 = range_2.split("-")
    range_1 = list(range(int(min_1), int(max_1) + 1))
    range_2 = list(range(int(min_2), int(max_2) + 1))
    if any(num in range_2 for num in range_1):
        return 1
    elif any(num in range_1 for num in range_2):
        return 1
    else:
        return 0


assert sum([solve_part_1(x) for x in example]) == 2
assert sum([solve_part_2(x) for x in example]) == 4

if __name__ == "__main__":
    print(f"Solution Part 1: {sum([solve_part_1(x) for x in data])}")
    print(f"Solution Part 2: {sum([solve_part_2(x) for x in data])}")
