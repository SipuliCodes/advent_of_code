import string

def open_file(file_path: str):
    line_list = []
    with open(file_path) as input:
        for line in input:
            line = line.strip()
            if line != "":
                line_list.append(line)
    return line_list

def input_to_dict(input: list):
    map_dict = {}
    key = ""
    index = 0
    for line in input:
        if "seeds" in line:
            seed_ranges = get_seed_ranges(line)
            map_dict["seeds"] = []
            for rng in seed_ranges:
                map_dict["seeds"].append(rng)
            continue
        #print(map_dict)
        if line[0] in string.ascii_letters:
            key = line.replace(" ", "_").replace(":", "")
            map_dict[key] = {}
            index = 0
            continue
        map_dict[key][index] = {}
        destination, source, rng = line.split()
        separation = int(source) - int(destination)
        map_dict[key][index]["min"] = int(source)
        map_dict[key][index]["max"] = int(source) + int(rng) - 1
        map_dict[key][index]["sep"] = separation
        #map_dict[key][index]["rng"] = rng
        index += 1
    return map_dict

def get_seed_ranges(line: str):
    number_list = line.split()[1:]
    seed_ranges = []
    index = 0
    while index < len(number_list):
        seed_ranges.append((int(number_list[index]), int(number_list[index + 1])))
        index += 2
    #print(seed_ranges)
    return seed_ranges

def path_finder(map: dict):
    values_list = []
    changed = []
    for name_key in map.keys():
        change_bool(changed)
        print(name_key)
        if type(map[name_key]) == list:
            values_list = map[name_key]
            changed = [False] * len(values_list)
            print(values_list)
            continue
        for index_key in map[name_key].keys():
            for index, value in enumerate(values_list):
                max = map[name_key][index_key]["max"]
                min = map[name_key][index_key]["min"]
                sep = map[name_key][index_key]["sep"]
                start = value[0]
                rng = value[1]
                #print("3", values_list)
                #print("max:", max, "min:", min)
                if (min <= start <= max) and not changed[index]:
                    
                    if start + rng <= max:
                        values_list[index] = (start - sep, rng)
                    elif start + rng > max:
                        #print((start - sep, max - start))
                        #print((max + 1, rng - max + start))
                        values_list[index] = (start - sep, max - start)
                        values_list.append((max + 1, rng - max + start))
                        changed.append(True)
                    changed[index] = True
                if (min < start + rng < max) and not changed[index]:
                    #print((start, min - start))
                    #print((min, start + rng - min))
                    values_list[index] = (start, min - start)
                    values_list.append((min - sep, rng + start - min))
                    changed.append(True)
                    changed[index] = True
                
            print(values_list)
    return values_list

def change_bool(bools: list):
    for index, bool in enumerate(bools):
        bools[index] = False
    return bools

def get_min_location(locations: list):
    return min(locations)[0]


input = open_file("day5/input.txt")
dictionary = input_to_dict(input)
#print(dictionary)
location_list = path_finder(dictionary)
min_location = get_min_location(location_list)
print(location_list)
print(min_location)