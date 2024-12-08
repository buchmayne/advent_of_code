f = open("input_data.txt", "r")
data = [[char for char in row] for row in f.read().split("\n")]

def solve_part_1(data):
    def check_forward(data, row, col):
        if col + 3 >= len(data[0]):
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row][col + 1]
            char_3 = data[row][col + 2]
            char_4 = data[row][col + 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_backwards(data, row, col):
        if col - 3 < 0:
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row][col - 1]
            char_3 = data[row][col - 2]
            char_4 = data[row][col - 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_above(data, row, col):
        if row - 3 < 0:
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row - 1][col]
            char_3 = data[row - 2][col]
            char_4 = data[row - 3][col]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_below(data, row, col):
        if row + 3 >= len(data):
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row + 1][col]
            char_3 = data[row + 2][col]
            char_4 = data[row + 3][col]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_diagonal_SE(data, row, col):
        if row + 3 >= len(data) or col + 3 >= len(data[0]):
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row + 1][col + 1]
            char_3 = data[row + 2][col + 2]
            char_4 = data[row + 3][col + 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_diagonal_NE(data, row, col):
        if row - 3 < 0 or col + 3 >= len(data[0]):
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row - 1][col + 1]
            char_3 = data[row - 2][col + 2]
            char_4 = data[row - 3][col + 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_diagonal_SW(data, row, col):
        if row + 3 >= len(data) or col - 3 < 0:
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row + 1][col - 1]
            char_3 = data[row + 2][col - 2]
            char_4 = data[row + 3][col - 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False

    def check_diagonal_NW(data, row, col):
        if row - 3 < 0 or col - 3 < 0:
            return False
        try:
            char_1 = data[row][col]
            char_2 = data[row - 1][col - 1]
            char_3 = data[row - 2][col - 2]
            char_4 = data[row - 3][col - 3]
            xmas = char_1 + char_2 + char_3 + char_4
            if xmas == "XMAS":
                return True
        except:
            return False
    
    answer = 0
    
    total_rows = len(data)
    total_cols = len(data[0])
    
    for r in range(total_rows):
        for c in range(total_cols):
            if check_forward(data, r, c):
                answer += 1
            if check_backwards(data, r, c):
                answer += 1
            if check_above(data, r, c):
                answer += 1
            if check_below(data, r, c):
                answer += 1
            if check_diagonal_SE(data, r, c):
                answer += 1
            if check_diagonal_NE(data, r, c):
                answer += 1
            if check_diagonal_SW(data, r, c):
                answer += 1
            if check_diagonal_NW(data, r, c):
                answer += 1
    return answer

def solve_part_2(data):
    def check_se(data, row, col):
        letter = data[row][col]
        opposite_map = {'S': 'M', 'M': 'S'}
        if (row + 2 >= len(data)) or (col + 2 >= len(data[0])):
            return False
        if (letter in ['S', 'M']):
            if data[row + 1][col + 1] == 'A':
                if data[row + 2][col + 2] == opposite_map[letter]:
                    new_letter = data[row + 2][col]
                    if new_letter in ['S', 'M']:
                        if data[row][col + 2] == opposite_map[new_letter]:
                            return True
        return False
                 
    
    answer = 0
    
    total_rows = len(data)
    total_cols = len(data[0])
    
    for r in range(total_rows):
        for c in range(total_cols):
            if check_se(data, r, c):
                print(f"SE: {r}, {c}")
                answer += 1
    return answer

if __name__ == "__main__":
    # Solve
    part_1_answer = solve_part_1(data)
    part_2_answer = solve_part_2(data)
    print(
        f"Part 1 Answer: {part_1_answer}\n"
        f"Part 2 Answer: {part_2_answer}\n"
    )

