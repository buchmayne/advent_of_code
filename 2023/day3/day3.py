f = open("input_data.txt", "r")
data = f.read().split("\n")

# Validate
validate_part_1_input = []
validate_part_1_answer = None

validate_part_2_input = []
validate_part_2_answer = None

# Solver
# nrows = len(data)
# ncols = len(data[0])

# def extract_numeric(input_string):
#     numeric_characters = re.sub(r'\D', '', input_string)
#     return numeric_characters

# numbers_dict = {}
# for i in range(len(data)):
#     vals0 = [x for x in [re.sub(r'\D', ',', x) for x in data[i].split(".") if x != ''] if x != ',']
#     vals1 = [x.replace(",", "") if x[0] == "," or x[-1] == "," else x for x in vals0]
#     vals2 = [x.split(',') if ',' in x else x for x in vals1]
#     vals3 = [item if isinstance(item, str) else item for sublist in vals2 for item in (sublist if isinstance(sublist, list) else [sublist])]
#     numbers_dict[i] = vals3


test = data[:3]
nrows = len(test)
ncols = len(test[0])

def is_numeric_char(input: str) -> bool:
    return input in '0123456789'


for i in range(nrows):
    for j in range(ncols):
        if data[i][j] != '.':
            if is_numeric_char(data[i][j]):
                adjacent = False
                if j > 0:
                    j

print(test)