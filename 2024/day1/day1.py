f = open("input_data.txt", "r")
data = f.read().split("\n")

def solve_part_1(data):
    list_pairs = [x.split("   ") for x in data]

    list1 = []
    list2 = []

    for pair in list_pairs:
        list1.append(pair[0])
        list2.append(pair[1])
    
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    assert len(sorted_list1) == len(sorted_list2), "Different Lengths of Lists"

    answer = 0
    
    for i in range(len(sorted_list1)):
        answer += abs(int(sorted_list1[i]) - int(sorted_list2[i]))
        
    return answer


def solve_part_2(data):
    list_pairs = [x.split("   ") for x in data]

    list1 = []
    list2 = []

    for pair in list_pairs:
        list1.append(pair[0])
        list2.append(pair[1])
    
    answer = 0

    assert len(list1) == len(list2), "Different Lengths of Lists"
    
    for i in range(len(list1)):
        val = list1[i]
        answer += int(val) * len([x for x in list2 if x == val])
    
    return answer


if __name__ == "__main__":
    # Solve
    part_1_answer = solve_part_1(data)
    part_2_answer = solve_part_2(data)
    
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}"
    )