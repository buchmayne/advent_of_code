f = open("input_data.txt", "r")
data = f.read().split("\n")

# Validate
validate_part_1_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

validate_part_1_answer = 8

validatee_part_2_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

validate_part_2_answer = 2286

# Parameters
red_constraint = 12
green_constraint = 13
blue_constraint = 14

# Solver
def solve_part_1(input: str) -> int:
    game_id, games_record = input.split(": ")
    games = [game.split(",") for game in games_record.split("; ")]
    for round in games:
        for draw in round:
            if 'blue' in draw:
                if int(draw.replace(" blue", "")) > blue_constraint:
                    return 0
            elif 'red' in draw:
                if int(draw.replace(" red", "")) > red_constraint:
                    return 0
            elif 'green' in draw:
                if int(draw.replace(" green", "")) > green_constraint:
                    return 0
    return int(game_id.replace("Game ", ""))


assert sum([solve_part_1(x) for x in validate_part_1_input]) == validate_part_1_answer

if __name__ == "__main__":
    print(
        f"Part 1 Answer: {sum([solve_part_1(x) for x in data])}\n"
        f"Part 2 Answer: {None}"
    )