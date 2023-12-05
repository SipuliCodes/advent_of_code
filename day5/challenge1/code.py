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
            line = line.split()
            map_dict[line[0]] = []
            for number in line:
                try:
                    map_dict[line[0]].append(int(number))
                except:
                    pass
            continue
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
        index += 1
    return map_dict

def path_finder(map: dict):
    values_list = []
    changed = []
    for name_key in map.keys():
        change_bool(changed)
        if type(map[name_key]) == list:
            values_list = map[name_key]
            temp_list = [False] * len(values_list)
            changed = temp_list
            continue
        for index_key in map[name_key].keys():
            for index, value in enumerate(values_list):
                if (value <= map[name_key][index_key]["max"]) and value >= map[name_key][index_key]["min"]:
                    if not changed[index]:
                        values_list[index] = value - map[name_key][index_key]["sep"]
                        changed[index] = True
                    continue
    return values_list

def change_bool(bools: list):
    for index, bool in enumerate(bools):
        bools[index] = False
    return bools

def get_min_location(locations: list):
    return min(locations)


input = open_file("day5/input.txt")
dictionary = input_to_dict(input)
location_list = path_finder(dictionary)
min_location = get_min_location(location_list)
print(min_location)