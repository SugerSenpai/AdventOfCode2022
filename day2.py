from util import readFile

ROUND_DATA = "day2_input.txt"
# this is honestly a really boring way to solve this, but it's really fast
possibleMatchesPartOne = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

possibleMatchesPartTwo = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}


def calculatePoints(matches: list, matchResults: dict):
    sumPoints = 0
    for match in matches:
        sumPoints += matchResults[match]
    return sumPoints


rounds = readFile(ROUND_DATA)
print(calculatePoints(rounds, possibleMatchesPartOne))
print(calculatePoints(rounds, possibleMatchesPartTwo))
