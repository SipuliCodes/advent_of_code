from math import lcm


def get_input(file_path: str):
    instructions_and_network = tuple
    routes = {}
    starts = []
    with open(file_path) as input:
        content = input.read()
        instructions, network = content.split('\n\n')
        for route in network.split("\n"):
            route = route.translate(str.maketrans("", "", "(),=")).split()
            if route[0][2] == "A":
                starts.append(route[0])
            routes[route[0]] = {"L": route[1], "R": route[2] }
    instructions_and_network = (instructions, routes, starts)
    return instructions_and_network

def steps_counter(inst_and_network: tuple, start: str):
    instruction, network = inst_and_network
    instruction_index = 0
    current = start
    steps = 1
    while True:
        current = network[current][instruction[instruction_index]]
        if current[2] == "Z":
            break
        steps += 1
        instruction_index += 1
        if instruction_index >= len(instruction):
            instruction_index = 0
    return steps 


input = get_input("day8/input.txt")

inst_and_network, starts = input[:-1], input[-1]

lcms = [steps_counter(inst_and_network, start) for start in starts]

print(lcm(*lcms))