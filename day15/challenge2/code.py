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

def hashmap(hashes: str):
    boxes = {}
    for hash in hashes:
        if "=" in hash:
            label, focal_length = hash.split("=")
            number = hash_algorithm(label)
            if number in boxes:
                boxes[number][label] = int(focal_length)
            else:
                boxes[number] = {}
                boxes[number][label] = int(focal_length)

        if "-" in hash:
            label = hash.replace("-", "")
            number = hash_algorithm(label)
            try:
                del boxes[number][label]
            except:
                pass
    return boxes

def calculate_focusing_power(boxes: dict):
    focusing_power = 0
    for box in boxes:
        i = 1
        for lens in boxes[box]:
            focusing_power += (box + 1) * i * boxes[box][lens]
            i += 1
    return focusing_power


input = get_input("day15/input.txt")
boxes = hashmap(input)
focusing_power = calculate_focusing_power(boxes)

print(focusing_power)
