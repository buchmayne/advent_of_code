f = open("input_data.txt", "r")
data = f.read().split("\n")

# Validate
validate_part_1_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

validate_part_1_answer = 13

def solve_part_1(input: str) -> int:
    card_number, game_numbers = input.split(": ")
    winning_numbers, my_numbers = game_numbers.split(" | ")
    winning_numbers_set = set(sorted([int(n) for n in winning_numbers.split(" ") if n != '']))
    my_numbers_set = set(sorted([int(n) for n in my_numbers.split(" ") if n != '']))
    n_matches = len(winning_numbers_set.intersection(my_numbers_set))

    if n_matches == 0 or n_matches == 1:
        return n_matches
    else:
        return 2 ** (n_matches - 1)


assert sum([solve_part_1(x) for x in validate_part_1_input]) == validate_part_1_answer


if __name__ == "__main__":
    part_1_answer = sum([solve_part_1(x) for x in data])
    
    print(
        f"Part 1 Answer: {part_1_answer}"
    )