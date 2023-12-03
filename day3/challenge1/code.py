import string
punctuation = string.punctuation.replace(".", "")
print(punctuation)

with open("day3/input.txt") as input:
    part_numbers = []
    previous_line = ""
    
    for line in input:
        previous_line_indices = {}
        if previous_line == "":
            previous_line = line
            continue
        number = ""
        symbol = ""
        indices_list = []
        symbol_index = None
        for index, character in enumerate(previous_line):
            if character == "." or character == "\n":
                if len(number) != 0 and len(symbol) != 0:
                    #print(number, "appended to parts")
                    part_numbers.append(int(number))
                    previous_line_indices[symbol_index] = symbol
                elif len(number) != 0:
                    #print(number, "number added in previous")
                    for index in indices_list:
                        previous_line_indices[index] = int(number)
                elif len(symbol) != 0:
                    #print("symbol added")
                    previous_line_indices[symbol_index] = symbol
                symbol = ""
                number = ""
                indices_list = []
                symbol_index = None
                continue
            if character in string.digits:
                number += character
                indices_list.append(index)
            elif character in punctuation:
                if len(number) != 0:
                    part_numbers.append(int(number))
                    number = ""
                symbol += character
                symbol_index = index

        number = ""
        indices_list = []
        for index, character in enumerate(line):
            if character in string.digits:
                number += character
                indices_list.append(index)
            
            if character in punctuation:
                numbers = set()
                tries = [-1, 0, 1]
                for i in tries:
                    try:
                        numbers.add(previous_line_indices[index + i])
                    except:
                        pass
                
                if len(numbers) != 0:
                    for number in numbers:
                        part_numbers.append(number)
                    #print("number appended in != 0", number)
                number = ""
            
            if (character not in string.digits) and len(indices_list) != 0:
                indices_list.append(max(indices_list) + 1)
                indices_list.append(min(indices_list) - 1)
                #print("indices", indices_list)
                for index in indices_list:
                    try:
                        if previous_line_indices[index] in punctuation:
                            part_numbers.append(int(number))
                            #print(number, "appended")
                            number = ""
                            indices_list = []
                            break
                    except:
                        pass
                indices_list = [] 
                number = ""
        previous_line = line
    #print(previous_line_indices)
    print(part_numbers)
    print(sum(part_numbers))