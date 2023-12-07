f = open("example_data.txt", "r")
data = [x.split('\n') for x in f.read().split("\n\n")]

keys_to_maps = [
    "seed_to_soil",
    "soil_to_fertilizer",
    "fertilizer_to_water",
    "water_to_light",
    "light_to_temperature",
    "temperature_to_humidity",
    "humidity_to_location"
]

data_dict = {k:v[1:] for k,v in zip(keys_to_maps, data[1:])}

seeds_dict = {'seeds': [x.replace("seeds: ", "") for x in data[0]]}

for k in data_dict.keys():
    for i in range(len(data_dict[k])):    
        destination_range_start, source_range_start, range_length = data_dict[k][i].split(" ")
        data_dict[k][i] = {
            "destination_range_start": int(destination_range_start), 
            "source_range_start": int(source_range_start), 
            "range_length": int(range_length)
        }

test = data_dict['seed_to_soil']


def seed_to_soil(input: dict):
    dd = data_dict['seed_to_soil']

    seed_list = list(range(100))
    container_list = []
    for i in len(dd):
        if i == 1:
            source_range = list(
                range(
                    dd[i]["source_range_start"], 
                    dd[i]["source_range_start"] + dd[i]["range_length"]
                    )
                )
            
            destination_range = list(
                range(dd[i]["destination_range_start"], 
                      dd[i]["destination_range_start"] + dd[i]["range_length"]
                    )
                )

            mapping = {k:v for k,v in zip(source_range, destination_range)}
            l1 = [x for x in list(range(100)) if x not in destination_range]
            l2 = l1 + [mapping[x] for x in source_range]
        else:
            
            
            container_list.append(l2)
    
    return container_list


# print(seed_to_soil(test))

print(len(test))