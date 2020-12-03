f = open("input_data.txt", "r")
data = [line.split() for line in f]

valid_passwords = 0

for password in data:
    min_max_str = password[0].split('-')
    min_ = int(min_max_str[0]) - 1
    max_ = int(min_max_str[1]) - 1

    letter_ = password[1].replace(':', '')
    pword = password[2]
    letter_one = pword[min_]
    letter_two = pword[max_]
    new_pword = letter_one + letter_two
    occurences = new_pword.count(letter_)

    if occurences == 1:
        valid_passwords += 1

print(valid_passwords)
