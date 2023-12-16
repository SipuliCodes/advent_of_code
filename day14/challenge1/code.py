def get_input(file_path: str):
    rows = []
    with open(file_path) as input:
        for row in input:
            rows.append(row.strip())
    return rows

def coordinates(input: list):
    tilt = set()
    stay = set()
    for row_index, row in enumerate(input):
        for col_index, col in enumerate(row):
            if col == "O":
                tilt.add((row_index, col_index))
            if col == "#":
                stay.add((row_index, col_index))
    return tilt, stay

def tilt_north(tilt: set, stay: set):
    tilt = sorted(tilt)
    for index, coordinate in enumerate(tilt):
        row, col = coordinate
        i = 1
        while (row - i, col) not in tilt and (row - i, col) not in stay and row - i >= 0:
            i += 1
        tilt[index] = (row - i + 1, col)
    return tilt

def count_load(size: int, tilt: list):
    load = 0
    for rock in tilt:
        load += size - rock[0]
    return load

    

input = get_input("day14/input.txt")
tilt, stay = coordinates(input)
north_tilt = tilt_north(tilt, stay)
load = count_load(len(input), north_tilt)

print(load)
            
