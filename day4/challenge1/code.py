def separator(line: str):
    line = line.replace(":", "|").split("|")
    return make_list(line[1]), make_list(line[2])

def make_list(line: str):
    return line.split()

def point_giver(your_numbers: list, winning_number: list):
    points = 0
    one_found = False
    for number in your_numbers:
        if number in winning_number and not one_found:
            points = 1
            one_found = True
            continue
        if number in winning_number:
            points *= 2
    return points


def get_input(input_path: str):
    input_in_lines = []
    with open(input_path) as input:
        for line in input:
            input_in_lines.append(line)
    return input_in_lines

def line_by_line(input: list):
    all_points = 0
    for line in input:
        your_numbers, winning_numbers = separator(line)
        all_points += point_giver(your_numbers, winning_numbers)
    return all_points

input = get_input("day4/input.txt")
points = line_by_line(input)
print(points)


    



 
