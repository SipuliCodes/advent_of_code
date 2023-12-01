with open("day1/input.txt") as input:
    calibrationValues = []
    for line in input:
        first = None
        last = None
        for character in line:
            try:
                int(character)
                if first == None:
                    first = character
                last = character
            except:
                continue
        calibrationValues.append(int(first + last))
    print(sum(calibrationValues))
        