def gold_bag_finder(bags, contents, found=False):
    for k in contents.keys():
        if "shiny gold" in k:
            found = True
        found = gold_bag_finder(bags, bags[k], found)
    return found


def content_finder(bags, contents):
    global totalnumber
    for k, v in contents.items():
        for x in range(v):
            totalnumber += 1
            content_finder(bags, bags[k])
    return totalnumber


with open("input_data.txt", "r") as file:
    data = [y.split(" contain ") for y in [x.strip() for x in file.read().splitlines()]]
    bags = {}
    totalnumber = 0
    for bag in data:
        bag = [
            bag[0],
            bag[1].replace("bag.", "bags.").replace("bag,", "bags,").strip("."),
        ]
        bags[bag[0]] = {
            x[2:]: (int(x[0])) for x in bag[1].split(", ") if not x[0].isalpha()
        }
    print(
        "Part 1: {}".format(
            len([k for k, v in bags.items() if gold_bag_finder(bags, v)])
        )
    )
    print("Part 2: {}".format(content_finder(bags, bags["shiny gold bags"])))
