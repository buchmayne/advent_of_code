f = open("input_data.txt", "r")
data = [report.split(" ") for report in f.read().split("\n")]


def check_conditions(report):
    deltas = []
    for i in range(1, len(report)):
        deltas.append(int(report[i]) - int(report[i-1]))
    
    condition_1 = all([abs(x) > 0 and abs(x) <= 3 for x in deltas])
    condition_2 = (all([x > 0 for x in deltas]) | all([x < 0 for x in deltas]))
    return condition_1 and condition_2

def handle_edge_cases(report):
        answer = False
        idx = [x for x in range(1, len(report) - 1)]
        for index_ in idx:
            updated_list = [element for i, element in enumerate(report) if i != index_]
            if check_conditions(updated_list):
                answer = True
                return answer

def solve_part_1(data):    
    answer = 0
    result = {}
    for report in data:
        result[str(report)] = False
        condition_check = check_conditions(report)
        if condition_check:
            result[str(report)] = True
            answer += 1  
    return answer, result

def solve_part_2(data):
    answer = 0
    result = {}

    for report in data:
        result[str(report)] = False
        
        condition_A = check_conditions(report[1:])
        condition_B = check_conditions(report[:-1])

        deltas = []
        for i in range(1, len(report)):
            deltas.append(int(report[i]) - int(report[i-1]))
    
        if condition_A or condition_B:
            result[str(report)] = True
            answer += 1
        elif handle_edge_cases(report):
            answer += 1

    return answer, result


if __name__ == "__main__":
    # Solve
    part_1_answer, part_1_result = solve_part_1(data)
    part_2_answer, part_2_result = solve_part_2(data)

    debug = []
    for key in part_1_result.keys():
        if part_1_result[key] == False and part_2_result[key] == False:
            debug.append(key)
    
    example_1 = ['64', '67', '69', '70', '68', '71', '72']

    

    
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}\n"
        f"Debug: {debug}\n"
    )

