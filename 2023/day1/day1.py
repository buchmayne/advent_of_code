f = open("input_data.txt", "r")
data = f.read().split("\n")

# Parameters
integer_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
integer_words = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

all_integer_values = integer_characters + integer_words

words_to_char_mapping = {k:v for k,v in zip(integer_words, integer_characters)}

# Test Cases
validate_part_1 = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]

validate_part_2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
]

# Suggested Additional Test Cases
validate_adhoc = [
    "eighthree", #83
    "sevenine", #79
    'twone', # 21
    'eightwo', # 82
    'nineight', # 98
    'nineeight', # 98
    'eeeight', # 88
    'oooneeone' # 11
]

answers_adhoc = sum([83, 79, 21, 82, 98, 98, 88, 11])


def solve_part_1(input: str) -> int:    
    nums = [x for x in input if x in integer_characters]
    return int(nums[0] + nums[-1])

assert sum([solve_part_1(x) for x in validate_part_1]) == 142


def solve_part_2(input: str) -> int:
    locations = []
    values = []
    for int_val in all_integer_values:
        loc = input.find(int_val)
        if loc is not None and loc != -1:
            locations.append(loc)
            values.append(int_val)
    
    location_mapping = {k:v for k,v in zip(locations, values)}

    first_number = location_mapping[min(locations)]
    last_number = location_mapping[max(locations)]

    if first_number in integer_words:
        first_number = words_to_char_mapping[first_number]

    if last_number in integer_words:
        last_number = words_to_char_mapping[last_number]
    
    return int(first_number + last_number)

assert sum([solve_part_2(x) for x in validate_part_2]) == 281
assert sum([solve_part_2(x) for x in validate_adhoc]) == answers_adhoc

test = "one1165bjcpkpsjfxlnmz6"

def solve_part_2_(input: str) -> int:
    locations = []
    values = []
    for int_val in all_integer_values:
        
        loc_f = input.find(int_val)
        loc_l = input.rfind(int_val)
        
        if loc_f is not None and loc_f != -1:
            locations.append(loc_f)
            values.append(int_val)
        if loc_l is not None and loc_l != -1:
            locations.append(loc_l)
            values.append(int_val)

    location_mapping = {k:v for k,v in zip(locations, values)}

    first_number = location_mapping[min(locations)]
    last_number = location_mapping[max(locations)]

    if first_number in integer_words:
        first_number = words_to_char_mapping[first_number]

    if last_number in integer_words:
        last_number = words_to_char_mapping[last_number]
    
    return int(first_number + last_number)


if __name__ == "__main__":
    # Solve
    part_1_answer = sum([solve_part_1(x) for x in data])
    part_2_answer = sum([solve_part_2_(x) for x in data])
    
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}"
    )