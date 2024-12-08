import statistics

f = open("example_data.txt", "r")
data = f.read().split("\n\n")

def solve_part_1(data):
    answer = 0
    correct_updates = []
    rules, updates = data[0].split("\n"), data[1].split("\n")
    rules = [rule.split("|") for rule in rules]
    for update in updates:
        is_correct = True
        update_ = update.split(",")
        update_dict = {}
        for idx in range(len(update_)):
            update_dict[update_[idx]] = idx
        for rule in rules:
            if (rule[0] in update_) and (rule[1] in update_):
                if update_dict[rule[0]] > update_dict[rule[1]]:
                    is_correct = False
                    break
        if is_correct:
            correct_updates.append(update)
    split_updates = [[x for x in update.split(",")] for update in correct_updates]
    for su in split_updates:
        list_range = list(range(len(su)))
        idx = statistics.median(list_range)
        answer += int(su[idx])
    
    return answer, correct_updates

def solve_part_2(data):
    rules, updates = data[0].split("\n"), data[1].split("\n")
    rules = [rule.split("|") for rule in rules]

    _, correct_updates = solve_part_1(data)
    incorrect_updates = [update for update in updates if update not in correct_updates]
    return incorrect_updates

if __name__ == "__main__":
    # Solve
    part_1_answer, _ = solve_part_1(data)
    part_2_answer = solve_part_2(data)
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}\n"
    )

