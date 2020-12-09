f = open("input_data.txt", "r")
data = f.read().split("\n")
data = [int(num) for num in data]

part_1_slice_range = 26


def get_range_sum(preamble, left_index, slice_range):
    full_sequence = preamble[left_index : left_index + slice_range]
    next_value = full_sequence[-1]
    search_sequence = full_sequence[: len(full_sequence) - 1]
    valid_value = 0
    for i in search_sequence:
        for j in search_sequence:
            if i != j:
                if (i + j) == next_value:
                    valid_value += 1
    if valid_value == 0:
        return next_value, left_index, (left_index + slice_range - 1)


def run_over_every_range(preamble, slice_range):
    for idx in range(0, 1000):
        tmp = get_range_sum(preamble, left_index=idx, slice_range=slice_range)
        if tmp is not None:
            return tmp


part1 = run_over_every_range(data, part_1_slice_range)
part1_answer = part1[0]
part1_range = part1[2]

part2_sequence = data[:part1_range]


def get_part2_range_sum(preamble, left_index, slice_range, target_sum):
    search_sequence = preamble[left_index : left_index + slice_range]
    if sum(search_sequence) == target_sum:
        return min(search_sequence) + max(search_sequence)


def run_part2(preamble, target_sum):
    for s_range in list(range(2, 20)):
        last_index = len(preamble) - s_range
        for idx in list(range(last_index)):
            tmp = get_part2_range_sum(
                preamble=preamble,
                left_index=idx,
                slice_range=s_range,
                target_sum=target_sum,
            )
            if tmp is not None:
                return tmp


print(run_part2(part2_sequence, part1_answer))