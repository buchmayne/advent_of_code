f = open("input_data.txt", "r")
data = [x.split('\n') for x in f]

lines_ = [line[0] for line in data]
long_lines_ = [line * 323 for line in lines_]

# now each line is 10,013 characters
long_lines_with_break = [line + '\n' for line in long_lines_]

# now each line is 10,014 characters as a line break is added to each line
massive_string = ''

for line in long_lines_with_break:
    massive_string = massive_string + line


down_1 = 10014
down_2 = down_1 * 2
jumps_for_one_line = 322
jumps_for_two_line = jumps_for_one_line / 2


def count_tress(slope, right, down, n_jumps_down):
    trees = 0
    position = 0

    while n_jumps_down > 0:
        new_position = position + right + down
        if slope[new_position] == '#':
            trees += 1
        position = new_position
        n_jumps_down -= 1

    return trees


r1_d1 = count_tress(slope=massive_string, right=1, down=down_1, n_jumps_down=jumps_for_one_line)
r3_d1 = count_tress(slope=massive_string, right=3, down=down_1, n_jumps_down=jumps_for_one_line)
r5_d1 = count_tress(slope=massive_string, right=5, down=down_1, n_jumps_down=jumps_for_one_line)
r7_d1 = count_tress(slope=massive_string, right=7, down=down_1, n_jumps_down=jumps_for_one_line)
r1_d2 = count_tress(slope=massive_string, right=1, down=down_2, n_jumps_down=jumps_for_two_line)

trees_product = r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2

print(trees_product)
