def separator(line: str):
    line = line.replace(":", "|").replace("\n", "").split("|")
    return make_list(line[1]), make_list(line[2])

def make_list(line: str):
    return line.split()

def get_input(input_path: str):
    input_in_lines = []
    with open(input_path) as input:
        for line in input:
            input_in_lines.append(line)
    return input_in_lines

def amount_of_matching_number(your_numbers: list, winning_numbers: list):
    amount = 0
    for number in your_numbers:
        if number in winning_numbers:
            amount += 1
    return amount

def amount_of_scratchcards(line: str,  index: int):
    scratchcards = 0
    your_numbers, winning_numbers = separator(line)
    amount = amount_of_matching_number(your_numbers, winning_numbers)
    if amount == 0:
        return 1
    for i in range(1, amount + 1):
        scratchcards += amount_of_scratchcards(input_lines[index + i], index + i)
    return scratchcards + 1

def line_by_line(input: list):
    scratchcard_amounts = 0
    index = 0
    for line in input:
        scratchcard_amounts += amount_of_scratchcards(line, index)
        index += 1
    return scratchcard_amounts

input_lines = get_input("day4/input.txt")
scratchcard_amounts = line_by_line(input_lines)
print(scratchcard_amounts)


    

