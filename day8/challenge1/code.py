
def get_input(file_path: str):
    instructions_and_network = tuple
    routes = {}
    with open(file_path) as input:
        content = input.read()
        instructions, network = content.split('\n\n')
        for route in network.split("\n"):
            route = route.translate(str.maketrans("", "", "(),=")).split()
            routes[route[0]] = {"L": route[1], "R": route[2] }
    instructions_and_network = (instructions, routes)
    return instructions_and_network

def steps_counter(inst_and_network: tuple):
    instruction, network = inst_and_network
    current = "AAA"
    end = "ZZZ"
    instruction_index = 0
    steps = 0
    while True:
        if current == end:
            break
        current = network[current][instruction[instruction_index]]
        steps += 1
        instruction_index += 1
        if instruction_index >= len(instruction):
            instruction_index = 0
    return steps
        


input = get_input("day8/input.txt")

steps = steps_counter(input)

print(steps)

