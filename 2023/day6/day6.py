import math

f = open("input_data.txt", "r")
data = f.read().split("\n")

time_p1 = [x for x in data[0].replace("Time:", "").split(" ") if x != ""]
distance_p1 = [x for x in data[1].replace("Distance:", "").split(" ") if x != ""]

race_dict_p1, race_dict_p2 = {}, {}
for i in range(len(time_p1)):
    race_dict_p1[i] = {'time': int(time_p1[i]), 'distance': int(distance_p1[i])}

race_dict_p2[0] = {
    "time": int(data[0].replace("Time:", "").replace(" ", "")),
    "distance": int(data[1].replace("Distance:", "").replace(" ", ""))
}

def model_race(race):
    a = 1
    b = -1 * race['time']
    c = race['distance'] + 0.0001
    sqrt_part = math.sqrt((b**2) - 4 * a * c)
    answer_ceiling = math.ceil(((-1* b) - sqrt_part) / (2 * a))
    answer_floor = math.floor(((-1* b) + sqrt_part) / (2 * a))
    return len(range(answer_floor - answer_ceiling)) + 1
    

answer_part_1 = math.prod([model_race(race_dict_p1[i]) for i in range(len(race_dict_p1))])
answer_part_2 = math.prod([model_race(race_dict_p2[i]) for i in range(len(race_dict_p2))])

if __name__ == "__main__":
    print(
        f"Part 1: {answer_part_1}\n"
        f"Part 2: {answer_part_2}"
    )

    