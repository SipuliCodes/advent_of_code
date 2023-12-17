def get_input(file_path):
    f = open(file_path)
    input = f.read().split(",")
    return input

def hash_algorithm(hash: str):
    current_value = 0
    for letter in hash:
        current_value += ord(letter)
        current_value *= 17
        current_value %= 256
    return current_value


input = get_input("day15/input.txt")

sum = 0
for hash in input:
    sum += hash_algorithm(hash)

print(sum)

