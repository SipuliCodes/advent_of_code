def get_input(file_path: str):
    rows = []
    with open(file_path) as input:
        for row in input:
            rows.append(row.strip())
    return rows

def split_patterns(input: list):
    patterns = []
    temp = []
    for row in input:
        if row:
            temp.append(row)
        if row == "":
            patterns.append(temp)
            temp = []
    patterns.append(temp)
    return patterns

def row_checker(pattern: list):
    for i in range(0, len(pattern) - 1):
        if pattern[i] == pattern[i+1]:
            smaller = 0
            if i <= len(pattern) - i - 2: 
                smaller = i
            else: 
                smaller = len(pattern) - i - 2
            mirror = True
            for j in range(1, smaller + 1):
                if pattern[i-j] != pattern[i+1+j]:
                    mirror = False
            if mirror:
                return i + 1
    return 0

def column_checker(pattern: list):
    for i in range(len(pattern[0])- 1):
        mirror = True
        for row in pattern:
            if row[i] != row[i + 1]:
                mirror = False  
        if mirror:
            smaller = 0
            if i <= len(pattern[0])  - 2 - i:
                smaller = i
            else:
                smaller = len(pattern[0]) - 2 - i
            for j in range(1, smaller + 1):
                for row in pattern:
                    if row[i-j] != row[i+1+j]:
                        mirror = False
        if mirror:
            return i + 1
    return 0

def summarize(patterns: list):
    sum = 0
    for pattern in patterns:
        sum += row_checker(pattern) * 100
        sum += column_checker(pattern)
    return sum
input = get_input("day13/input.txt")
patterns = split_patterns(input)
sum = summarize(patterns)

print(sum)
