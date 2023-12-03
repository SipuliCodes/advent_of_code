import string

with open("day3/input.txt") as input:
    part_numbers = []
    previous_line = ""
    current_line = ""
    next_line = ""
    previous_line_numbers_by_indices = {}
    current_line_numbers_by_indices = {}
    next_line_numbers_by_indices = {}
    indices_for_star = []
    number_indices_list = []
    number = ""
    for line in input:
        next_line_numbers_by_indices = {}
        next_line = line

        for index, character in enumerate(next_line):
            if character in string.digits:
                number_indices_list.append(index)
                number += character
            if character not in string.digits and number != "":
                for index in number_indices_list:
                    next_line_numbers_by_indices[index] = number
                number = ""
                number_indices_list = []
        if current_line == "":
            current_line_numbers_by_indices = next_line_numbers_by_indices
            current_line = next_line
            continue
        for index, character in enumerate(current_line):
            if character == "*":
                indices_for_star.append(index)
        
        for index in indices_for_star:
            numbers = set()
            for tries in [-1, 0, 1]:
                try:
                    numbers.add(previous_line_numbers_by_indices[index + tries])
                except:
                    pass
                try:
                    numbers.add(current_line_numbers_by_indices[index + tries])
                except:
                    pass
                try:
                    numbers.add(next_line_numbers_by_indices[index + tries])
                except:
                    pass
            if len(numbers) == 2:
                number1, number2 = numbers
                part_numbers.append(int(number1) * int(number2))

        indices_for_star = []
        previous_line = current_line
        current_line = next_line
        previous_line_numbers_by_indices = current_line_numbers_by_indices
        current_line_numbers_by_indices = next_line_numbers_by_indices
    print(sum(part_numbers))
