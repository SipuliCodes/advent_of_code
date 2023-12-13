def get_input(path_file):
    input_as_list = []
    with open(path_file) as input:
        for line in input:
            input_as_list.append(line)
    return input_as_list

def find_s(lines: list):
    s_position = tuple
    s_found = False
    for line_index, line in enumerate(lines):
        for column_index, character in enumerate(line):
            if character == "S":
                s_position = (line_index, column_index)
                s_found = True
                break
        if s_found:
            break
    return s_position

def find_starts(lines: list, s_position: tuple):
    first_start = tuple
    first_found = False
    second_start = tuple
    second_found = False
    row_index, column_index = s_position
    south = "|7F"
    north = "|LJ"
    west = "J7-"
    east = "FL-"

    while not first_found or not second_found:
        if lines[row_index - 1][column_index] in south:
            if not first_found:
                first_start = (row_index - 1, column_index)
                first_found = True
            else:
                second_start = (row_index - 1, column_index)
                second_found = True
        if lines[row_index + 1][column_index] in north:
            if not first_found:
                first_start = (row_index + 1, column_index)
                first_found = True
            else:
                second_start = (row_index + 1, column_index)
                second_found = True
        if lines[row_index][column_index - 1] in east:
            if not first_found:
                first_start = (row_index, column_index - 1)
                first_found = True
            else:
                second_start = (row_index, column_index - 1)
                second_found = True
        if lines[row_index][column_index + 1] in west:
            if not first_found:
                first_start = (row_index, column_index + 1)
                first_found = True
            else:
                second_start = (row_index, column_index + 1)
                second_found = True
    return (first_start, second_start)

def find_next(previous: tuple, current: tuple, character: str):
    if character == "7":
        return (current[0] + 1, current[1]) if (current[0], current[1] - 1) == previous else (current[0], current[1] - 1)
    if character == "J":
        return (current[0] - 1, current[1]) if (current[0], current[1] - 1) == previous else (current[0], current[1] - 1)
    if character == "-":
        return (current[0], current[1] + 1) if (current[0], current[1] - 1) == previous else (current[0], current[1] - 1)
    if character == "F":
        return (current[0] + 1, current[1]) if (current[0], current[1] + 1) == previous else (current[0], current[1] + 1)
    if character == "L":
        return (current[0] - 1, current[1]) if (current[0], current[1] + 1) == previous else (current[0], current[1] + 1)
    if character == "|":
        return (current[0] - 1, current[1]) if (current[0] + 1, current[1]) == previous else (current[0] + 1, current[1])
    
def find_farthest_away(input: list, start_points: tuple, s_position: tuple):
    current_first, current_second = start_points
    coordinates = {"first": {"current": current_first, "previous": s_position}, "second": {"current": current_second, "previous": s_position}}
    steps = 1
    
    while coordinates["first"]["current"] != coordinates["second"]["current"]:
       steps += 1
       for key in coordinates.keys():
           row, col = coordinates[key]["current"]
           row, col = find_next(coordinates[key]["previous"], coordinates[key]["current"], input[row][col])
           coordinates[key]["previous"] = coordinates[key]["current"]
           coordinates[key]["current"] = (row, col)
    
    return steps
           
        

input = get_input("day10/input.txt")

s_position = find_s(input)

start_points = find_starts(input, s_position)

steps = find_farthest_away(input, start_points, s_position)
print(steps)
