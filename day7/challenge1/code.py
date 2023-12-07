from collections import Counter

def get_input(file_path: str):
    hands = []
    with open(file_path) as input:
        for line in input:
            hand, bid = line.split()
            hands.append((hand, int(bid)))
    return hands

def make_hands(hands: list):
    game_hands = []
    for hand in hands:
        play_hand = 0
        different_cards = Counter(hand[0])
        if len(different_cards) == 5:
            play_hand = 1
        if len(different_cards) == 4:
            play_hand = 2
        if len(different_cards) == 3:
            for key, value in different_cards.items():
                if value == 2:
                    play_hand = 3
                    break
                if value == 3:
                    play_hand = 4
                    break
        if len(different_cards) == 2:
            for key, value in different_cards.items():
                if value == 3:
                    play_hand = 5
                    break
                if value == 4:
                    play_hand = 6
                    break
        if len(different_cards) == 1:
            play_hand = 7
        game_hands.append({"0": play_hand, "1": get_value(hand[0][0]), "2": get_value(hand[0][1]), "3": get_value(hand[0][2]), "4": get_value(hand[0][3]), "5": get_value(hand[0][4]), "bid": hand[1] })
    return game_hands

def compare(hands: list):
    return sorted(hands, key=lambda x : (x["0"], x["1"], x["2"], x["3"], x["4"], x["5"]))

def multiplication(hands: list):
    product = 0
    for index, hand in enumerate(hands):
        print(index, hand["bid"], hand["0"], hand["1"], hand["2"], hand["3"], hand["4"], hand["5"])
        product += (index + 1) * hand["bid"]
    return product

def get_value(char: str):
    if char == "A":
        return 14
    if char == "K":
        return 13
    if char == "Q":
        return 12
    if char == "J":
        return 11
    if char == "T":
        return 10
    return int(char)

x = get_input("day7/input.txt")

y = make_hands(x)

z = compare(y)

print(multiplication(z))
