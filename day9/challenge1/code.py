def extrapolate(numbers: list):
    biggest_from_rows = []
    while numbers:
        for index, value in enumerate(numbers):
            try:
                numbers[index] = numbers[index + 1] - value
            except:
                pass
        biggest_from_rows.append(numbers.pop())
    return sum(biggest_from_rows)

def make_int(numbers: list):
    return [int(number) for number in numbers]

with open("day9/input.txt") as input:
    sums = []
    for line in input:
        sums.append(extrapolate(make_int(line.split())))
    print(sum(sums))



