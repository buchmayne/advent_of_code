f = open("input_data.txt", "r")
data = f.read().split("\n")

map_choice_to_score = {"X": 1, "Y": 2, "Z": 3}
map_choice_to_standard_choice = {"X": "A", "Y": "B", "Z": "C"}


def determine_outcome_part_1(opponent_choice, my_choice):
    if opponent_choice == my_choice:
        return 3
    if opponent_choice == "A":
        if my_choice == "B":
            return 6
        else:
            return 0
    if opponent_choice == "B":
        if my_choice == "C":
            return 6
        else:
            return 0
    if opponent_choice == "C":
        if my_choice == "A":
            return 6
        else:
            return 0


def score_matchup_part_1(matchup):
    opponent_choice, my_choice = matchup.split(" ")
    return (
        determine_outcome_part_1(
            opponent_choice, map_choice_to_standard_choice[my_choice]
        )
        + map_choice_to_score[my_choice]
    )


def determine_correct_response(opponent_choice, my_choice):
    if my_choice == "X":
        if opponent_choice == "A":
            return "Z"
        elif opponent_choice == "B":
            return "X"
        else:
            return "Y"
    elif my_choice == "Y":
        if opponent_choice == "A":
            return "X"
        elif opponent_choice == "B":
            return "Y"
        else:
            return "Z"
    elif my_choice == "Z":
        if opponent_choice == "A":
            return "Y"
        elif opponent_choice == "B":
            return "Z"
        else:
            return "X"


def score_matchup_part_2(matchup):
    opponent_choice, my_direction = matchup.split(" ")
    my_choice = determine_correct_response(opponent_choice, my_direction)
    return (
        determine_outcome_part_1(
            opponent_choice, map_choice_to_standard_choice[my_choice]
        )
        + map_choice_to_score[my_choice]
    )


example = ["A Y", "B X", "C Z"]
assert sum([score_matchup_part_1(m) for m in example]) == 15
assert sum([score_matchup_part_2(m) for m in example]) == 12

if __name__ == "__main__":
    print(
        sum([score_matchup_part_1(m) for m in data]),
        sum([score_matchup_part_2(m) for m in data]),
    )
