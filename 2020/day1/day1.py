f = open('day1_input.txt', 'r')
input_data = [int(x) for x in f]

sum_condition = 2020


def get_product(data):
    for x in data:
        data_sans_x = [num for num in data if num != x]
        for y in data_sans_x:
            data_sans_x_y = [num for num in data_sans_x if num != y]
            for z in data_sans_x_y:
                if (x + y + z) == sum_condition:
                    answer = x * y * z
                    return answer


if __name__ == "__main__":
    print(get_product(input_data))
