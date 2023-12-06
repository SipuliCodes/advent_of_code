import math

def get_input_as_tuples(file_path: str):
    tuple_list = []
    time_list = []
    distance_list = []
    with open(file_path) as input:
        for line in input:
            numbers = line.split()
            if "Time:" in numbers:
                for number in numbers[1:]:
                    time_list.append(number)
            if "Distance:" in numbers:
                for number in numbers[1:]:
                    distance_list.append(number)
    for index, time in enumerate(time_list):
        tuple_list.append((int(time), int(distance_list[index])))
    return tuple_list

def number_of_ways(time_distances: list):
    amount_of_ways = []
    for time_distance in time_distances:
        ways = 0
        time, distance = time_distance
        speed = 0
        while time >= 0:
            if time * speed > distance:
                ways += 1
            time -= 1
            speed += 1
        amount_of_ways.append(ways)
    return math.prod(amount_of_ways)

input = get_input_as_tuples("day6/input.txt")
print(input)
ways = number_of_ways(input)
print(ways)


