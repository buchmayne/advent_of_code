import string

f = open("input_data.txt", "r")
data = f.read().split("\n")

example = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

alphabet_characters = list(string.ascii_letters)
alphabet_values = list(range(1, len(alphabet_characters) + 1))

alphabet_crosswalk = {k: v for k, v in zip(alphabet_characters, alphabet_values)}


def split_rucksack(rucksack):
    length_of_compartment = int(len(rucksack) / 2)
    compartment_1 = rucksack[:length_of_compartment]
    compartment_2 = rucksack[length_of_compartment:]

    return compartment_1, compartment_2


def get_shared_character(rucksack):
    compartment_1, compartment_2 = split_rucksack(rucksack)
    unique_values_1, unique_values_2 = list(set(compartment_1)), list(
        set(compartment_2)
    )
    return [character for character in unique_values_1 if character in unique_values_2][
        0
    ]


def get_numeric_value_from_rucksack(rucksack):
    character = get_shared_character(rucksack)
    return alphabet_crosswalk[character]


assert split_rucksack(example[0])[0] == "vJrwpWtwJgWr"
assert split_rucksack(example[0])[1] == "hcsFMMfFFhFp"
assert get_shared_character(example[0]) == "p"
assert get_numeric_value_from_rucksack(example[0]) == 16
assert sum([get_numeric_value_from_rucksack(rucksack) for rucksack in example]) == 157


def get_shared_character_across_elf_group(elf_group):
    unique_vals = [list(set(x)) for x in elf_group]
    return [
        character
        for character in unique_vals[0]
        if character in unique_vals[1] and character in unique_vals[2]
    ][0]


def define_elf_groups(list_of_rucksacks):
    number_of_rucksacks = len(list_of_rucksacks)
    number_of_groups = int(number_of_rucksacks / 3)

    group_idx = [x * 3 for x in list(range(1, number_of_groups + 1))]

    elf_groups = []

    for i in range(len(group_idx)):
        if i == 0:
            elf_groups.append(list_of_rucksacks[: group_idx[i]])
        else:
            elf_groups.append(list_of_rucksacks[group_idx[i - 1] : group_idx[i]])

    return elf_groups


def solve_part_two(list_of_rucksacks):
    elf_groups = define_elf_groups(list_of_rucksacks)
    shared_characters = [
        get_shared_character_across_elf_group(elf_group) for elf_group in elf_groups
    ]
    return sum([alphabet_crosswalk[character] for character in shared_characters])


assert get_shared_character_across_elf_group(define_elf_groups(example)[0]) == "r"
assert solve_part_two(example) == 70

print(
    f"Answer to Part 1: {sum([get_numeric_value_from_rucksack(rucksack) for rucksack in data])}\n"
    f"Answer to Part 2: {solve_part_two(data)}"
)
