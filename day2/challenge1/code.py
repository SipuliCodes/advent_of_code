amountOfCubesPerColor = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("day2/input.txt") as input:
    possibleGameIds = []
    for line in input:
        game, values = line.split(":")
        subsets = values.replace(";", ",").strip(" ").split(",")
        gameId = int(game.split()[1])
        possibleGame = True
        for subset in subsets:
            number, color = subset.split()
            if int(number) > amountOfCubesPerColor[color]:
                possibleGame = False
                break
        if possibleGame:
            possibleGameIds.append(gameId)
    print(possibleGameIds)
    print(sum(possibleGameIds))