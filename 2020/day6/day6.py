f = open("input_data.txt", "r")
data_ = f.read()

data_ = data_.split("\n\n")
data_ = [idx.replace("\n", " ") for idx in data_]
data_ = [x.split(" ") for x in data_]


def unify_answers(list_obj):
    single_str = ""
    for x in list_obj:
        single_str = single_str + x
    return single_str


def count_unique_obs(list_obj):
    list_unique_count = []
    for x in list_obj:
        unique_count = len(list(set(unify_answers(x))))
        list_unique_count.append(unique_count)
    return list_unique_count


# print(sum(count_unique_obs(data_)))


# Part 2
def part2(group):
    single_string = unify_answers(group)
    all_unique_answers = list(set(single_string))
    n_people_in_group = len(group)
    unique_dict = {x: 0 for x in all_unique_answers}
    count_everybody_answers = 0
    for person in group:
        for answer in all_unique_answers:
            if person.count(answer) > 0:
                unique_dict[answer] = unique_dict[answer] + 1
    for answer in all_unique_answers:
        if unique_dict[answer] == n_people_in_group:
            count_everybody_answers += 1
    return count_everybody_answers


print(sum([part2(x) for x in data_]))
