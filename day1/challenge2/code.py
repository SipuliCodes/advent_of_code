transform = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open("day1/input.txt") as input:
    calibrationValues = []
    for line in input:
        print("line", line)
        first = None
        last = None
        firstIndex = len(line)
        lastIndex = 0
        for index, character in enumerate(line):
            try:
                int(character)
                if first == None:
                    first = character
                    firstIndex = index
                last = character
                lastIndex = index
            except:
                continue
        for key in transform.keys():
            findLastIndex = line.rfind(key)
            if findLastIndex != -1 and findLastIndex > lastIndex:
                lastIndex = findLastIndex
                last = key
            findFirstIndex = line.find(key)
            if findFirstIndex != -1 and findFirstIndex < firstIndex:
                firstIndex = findFirstIndex
                first = key
        try:
            last = str(transform[last])
        except:
            last = last
        try: 
            first = str(transform[first])
        except:
            first = first
        print("first: ", first, "last: ", last)
        calibrationValues.append(int(first + last))
    print(sum(calibrationValues))