import re

f = open("input_data.txt", "r")
data = f.read()


def solve_part_1(data):    
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, data)
    return sum([int(x[0]) * int(x[1]) for x in [pair.replace("mul", "").replace("(", "").replace(")", "").split(",") for pair in matches]])

def solve_part_2(data) -> int:
    memory_segments = re.split(r"(don't\(\)|do\(\))", data)
    answer = solve_part_1(memory_segments[0]) + sum(
        solve_part_1(segment)
        for condition, segment in zip(
            memory_segments[1::2], memory_segments[2::2], strict=False
        )
        if condition == "do()"
    )
    return answer

if __name__ == "__main__":
    # Solve
    part_1_answer = solve_part_1(data)
    part_2_answer = solve_part_2(data)
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}\n"
    )

