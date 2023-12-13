def get_input(file_path: str):
    rows = []
    with open(file_path) as input:
        for row in input:
            rows.append(row.strip())
    return rows

def expand_rows(rows: list):
    expanded_rows = set()
    for index, row in enumerate(rows):
        if "#" not in row:
            expanded_rows.add(index)
    return expanded_rows

def expand_columns(rows: list):
    expanded_columns = set()
    i = 0
    for _ in range(len(rows[0])):
        empty = True
        for row in rows:
            if row[i] != ".":
                empty = False
                break
        if empty:
            expanded_columns.add(i)
        i += 1
    return expanded_columns
            
def get_coordinates(space: list):
    coordinates = []
    for i, row in enumerate(space):
        for j, col in enumerate(row):
            if col == "#":
                coordinates.append((i, j))
    return coordinates

def get_paths(coordinates: list, expanded_rows: set, expanded_cols: set, expansion: int):
    sum_of_lengths = 0
    while coordinates:
        start_row, start_col = coordinates.pop()
        for end_row, end_col in coordinates:
            multiplier = 0
            for i in range(end_row, start_row):
                if i in expanded_rows:
                    multiplier += 1
            if end_col > start_col:
                for i in range(start_col, end_col):
                    if i in expanded_cols:
                        multiplier += 1
            if start_col > end_col:
                for i in range(end_col, start_col):
                    if i in expanded_cols:
                        multiplier += 1
            sum_of_lengths += (abs(end_row - start_row) + abs(end_col - start_col) + expansion * multiplier - multiplier)
    return sum_of_lengths


space = get_input("day11/input.txt")

expanded_rows = expand_rows(space)
expanded_cols = expand_columns(space)
coordinates = get_coordinates(space)
path_length = get_paths(coordinates, expanded_rows, expanded_cols, 1000000)

print(path_length)

