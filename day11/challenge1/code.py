def get_input(file_path: str):
    rows = []
    with open(file_path) as input:
        for row in input:
            rows.append(row.strip())
    return rows

def expand_rows(rows: list):
    expanded_rows = []
    for row in rows:
        expanded_rows.append(row)
        if "#" not in row:
            expanded_rows.append(len(row)*".")
    return expanded_rows

def expand_columns(rows: list):
    expanded_columns = rows
    length = len(expanded_columns[0])
    i = 0
    while length > 0:
        empty = True
        for row in rows:
            try:
                if row[i] != ".":
                    empty = False
                    break
            except:
                pass
        if empty:
            for index, row in enumerate(expanded_columns):
                expanded_columns[index] = row[:i] + "." + row[i:]
            i += 1
        i += 1
        length -= 1
    return expanded_columns
            
def get_coordinates(expanded_space: list):
    coordinates = []
    for i, row in enumerate(expanded_space):
        for j, col in enumerate(row):
            if col == "#":
                coordinates.append((i, j))
    return coordinates

def get_paths(coordinates: list):
    sum_of_lengths = 0
    while coordinates:
        start = coordinates.pop()
        for end in coordinates:
            sum_of_lengths += (abs(end[0] - start[0]) + abs(end[1] - start[1]))
    return sum_of_lengths


space = get_input("day11/input.txt")

expanded_space_row = expand_rows(space)
expanded_space = expand_columns(expanded_space_row)
coordinates = get_coordinates(expanded_space)
path_length = get_paths(coordinates)

for index, row in enumerate(space):
    print(row, index)
print()
print()
for index, row in enumerate(expanded_space):
    print(row, index)

print(coordinates)
print(path_length)

