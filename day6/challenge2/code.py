import math

def get_input_as_tuple(file_path: str):
    time = ""
    distance = ""
    with open(file_path) as input:
        for line in input:
            numbers = line.split()
            if "Time:" in numbers:
                for number in numbers[1:]:
                    time += number
            if "Distance:" in numbers:
                for number in numbers[1:]:
                    distance += number
    return (int(time), int(distance))

def number_of_ways(time_distance: tuple):
    amount_of_ways = 0
    time, distance = time_distance
    speed = 0
    while time >= 0:
        if time * speed > distance:
            amount_of_ways += 1
        time -= 1
        speed += 1
    return amount_of_ways

input = get_input_as_tuple("day6/input.txt")
print(input)
ways = number_of_ways(input)
print(ways)
