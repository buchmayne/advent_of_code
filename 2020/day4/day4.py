f = open('input_data.txt', 'r')
data_ = f.read()

data_ = data_.split('\n\n')
data_ = [idx.replace('\n', ' ') for idx in data_]
data_ = [x.split(' ') for x in data_]

# there is a line break which causes a missing value in the final input
new_data_ = []

for x in data_:
    new_data_.append([y for y in x if y])


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def convert_to_dict(list_obj):
    dict_ = {}
    for x in list_obj:
        key_, value_ = x.split(':')
        tmp_dict = {key_: value_}
        dict_ = Merge(dict_, tmp_dict)

    return dict_


list_of_passports = [convert_to_dict(x) for x in new_data_]

all_passport_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
passport_keys_sans_cid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

#     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     hgt (Height) - a number followed by either cm or in:
#         If cm, the number must be at least 150 and at most 193.
#         If in, the number must be at least 59 and at most 76.
#     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     cid (Country ID) - ignored, missing or not.


def validate_values(passport_dict):
    birth_year = int(passport_dict['byr'])
    if (birth_year < 1920) or (birth_year > 2002):
        return False
    issue_year = int(passport_dict['iyr'])
    if (issue_year < 2010) or (issue_year > 2020):
        return False
    expiration_year = int(passport_dict['eyr'])
    if (expiration_year < 2020) or (expiration_year > 2030):
        return False
    # could be issue if there are non-numeric characters, try this first though
    if len(passport_dict['pid']) != 9:
        return False
    eye_color = passport_dict['ecl']
    if eye_color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    hair_color = passport_dict['hcl']
    if hair_color[0] != '#':
        return False
    if hair_color[0] == '#':
        if len(hair_color) != 7:
            return False
    height = passport_dict['hgt']
    if (height[-2:] != 'in') and (height[-2:] != 'cm'):
        return False
    if height[-2:] == 'in':
        height_in = int(height.replace('in', ''))
        if (height_in < 59) or (height_in > 76):
            return False
    if height[-2:] == 'cm':
        height_cm = int(height.replace('cm', ''))
        if (height_cm < 150) or (height_cm > 193):
            return False

    return True


valid_passports = 0

for passport in list_of_passports:
    keys_ = list(passport.keys())
    if 'cid' in keys_:
        if set(keys_) == set(all_passport_keys):
            try:
                if validate_values(passport):
                    valid_passports += 1
            except:
                pass
    else:
        if set(keys_) == set(passport_keys_sans_cid):
            try:
                if validate_values(passport):
                    valid_passports += 1
            except:
                pass


print(valid_passports)
