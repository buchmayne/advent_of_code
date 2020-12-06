f = open("input_data.txt", "r")
data = f.read()
list_of_boarding_passes = data.split("\n")


def get_row_or_column_number(
    data_input, f_input_type, b_input_type, min_input_type, max_input_type
):
    total_input_ = max_input_type
    first_value = min_input_type
    for x in data_input:
        slicer_ = int((total_input_ - first_value) / 2) + first_value
        f_half = list(range(first_value, slicer_))
        b_half = list(range(slicer_, total_input_))
        if x == f_input_type:
            if len(f_half) == 1:
                return f_half[0]
            total_input_ = slicer_
            first_value = first_value
        elif x == b_input_type:
            if len(b_half) == 1:
                return b_half[0]
            total_input_ = total_input_
            first_value = slicer_


def calculate_seat_id(boarding_pass):
    rows_ = boarding_pass[:7]
    columns_ = boarding_pass[7:]
    row_id = get_row_or_column_number(
        rows_, f_input_type="F", b_input_type="B", min_input_type=0, max_input_type=128
    )
    column_id = get_row_or_column_number(
        columns_, f_input_type="L", b_input_type="R", min_input_type=0, max_input_type=8
    )
    seat_id = (row_id * 8) + column_id
    return seat_id


seat_ids = [
    calculate_seat_id(boarding_pass) for boarding_pass in list_of_boarding_passes
]


# GET MISSING SEAT
sorted_seat_ids = sorted(seat_ids)
first_seat_id = sorted_seat_ids[0]
count_seats = len(sorted_seat_ids)
continous_seats = list(range(first_seat_id, first_seat_id + count_seats))

dont_match = []
for x in range(0, count_seats):
    if sorted_seat_ids[x] != continous_seats[x]:
        dont_match.append(sorted_seat_ids[x] - 1)

print("Highest Seat ID: {}\nMissing Seat ID: {}".format(max(seat_ids), min(dont_match)))
