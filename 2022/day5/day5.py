f1 = open("input_data1.txt", "r")
directions = f1.read().split("\n")

col1 = ["s", "l", "w"]
col2 = ["j", "t", "n", "q"]
col3 = ["s", "c", "h", "f", "j"]
col4 = ["t", "r", "m", "w", "n", "g", "b"]
col5 = ["t", "r", "l", "s", "d", "h", "q", "b"]
col6 = ["m", "j", "b", "v", "f", "h", "r", "l"]
col7 = ["d", "w", "r", "n", "j", "m"]
col8 = ["b", "z", "t", "f", "h", "n", "d", "j"]
col9 = ["h", "l", "q", "n", "b", "f", "t"]


container = {
    1: col1,
    2: col2,
    3: col3,
    4: col4,
    5: col5,
    6: col6,
    7: col7,
    8: col8,
    9: col9,
}


def parse_directions(direction):
    move_, from_, to_ = (
        direction.replace("move", "")
        .replace("from", "")
        .replace("to", "")
        .lstrip()
        .replace("  ", " ")
        .split(" ")
    )
    return int(move_), int(from_), int(to_)


for direction in directions:
    move_, from_, to_ = parse_directions(direction)
    while move_ > 0:
        crate = container[from_].pop()
        container[to_].append(crate)
        move_ -= 1


answer_part_1 = []

for k in list(container.keys()):
    last_letter = container[k].pop().upper()
    answer_part_1.append(last_letter)


print(answer_part_1)
