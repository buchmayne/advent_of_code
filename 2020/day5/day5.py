f = open("input_data.txt", "r")
data = f.read()
list_of_boarding_passes = data.split("\n")


def get_row_number(row_input):
    total_rows = 128
    first_row = 0
    for x in row_input:
        row_slicer = int((total_rows - first_row) / 2) + first_row
        f_half = list(range(first_row, row_slicer))
        b_half = list(range(row_slicer, total_rows))
        if x == "F":
            if len(f_half) == 1:
                return f_half[0]
            total_rows = row_slicer
            first_row = first_row
        elif x == "B":
            if len(b_half) == 1:
                return b_half[0]
            total_rows = total_rows
            first_row = row_slicer


def get_column_number(column_input):
    total_columns = 8
    first_column = 0
    for y in column_input:
        column_slicer = int((total_columns - first_column) / 2) + first_column
        f_half = list(range(first_column, column_slicer))
        b_half = list(range(column_slicer, total_columns))
        if y == "L":
            if len(f_half) == 1:
                return f_half[0]
            total_columns = column_slicer
            first_column = first_column
        elif y == "R":
            if len(b_half) == 1:
                return b_half[0]
            total_columns = total_columns
            first_column = column_slicer


def calculate_seat_id(boarding_pass):
    rows_ = boarding_pass[:7]
    columns_ = boarding_pass[7:]
    row_id = get_row_number(rows_)
    column_id = get_column_number(columns_)
    seat_id = (row_id * 8) + column_id
    return seat_id


seat_ids = [
    calculate_seat_id(boarding_pass) for boarding_pass in list_of_boarding_passes
]

print(max(seat_ids))


# GET MISSING SEAT
sorted_seat_ids = sorted(seat_ids)
first_seat_id = sorted_seat_ids[0]
count_seats = len(sorted_seat_ids)
continous_seats = list(range(first_seat_id, first_seat_id + count_seats))

dont_match = []
for x in range(0, count_seats):
    if sorted_seat_ids[x] != continous_seats[x]:
        dont_match.append(sorted_seat_ids[x] - 1)

print(min(dont_match))
