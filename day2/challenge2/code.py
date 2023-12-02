cubesNeeded = {
    "red": 0,
    "green": 0,
    "blue": 0
}

with open("day2/input.txt") as input:
    powers = []
    for line in input:
        cubesNeeded["red"] = 0
        cubesNeeded["green"] = 0
        cubesNeeded["blue"] = 0
        values = line.split(":")[1]
        subsets = values.replace(";", ",").strip(" ").split(",")
        for subset in subsets:
            number, color = subset.split()
            if cubesNeeded[color] < int(number):
                cubesNeeded[color] = int(number)
        powers.append(cubesNeeded["red"] * cubesNeeded["green"] * cubesNeeded["blue"])
    print(sum(powers))
        

