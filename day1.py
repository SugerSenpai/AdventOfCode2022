from util import readFile


ELVE_DATA = "day1_input.txt"


def assignToElves(calorieArray: list):
    elves = []
    counter = 0
    for line in calorieArray:
        if line == "":
            elves.append(counter)
            counter = 0
            continue
        counter = counter + int(line)
    return elves


def getTopThreeElves(elves: list):
    tempElves = elves
    topThree = 0
    for i in range(3):
        topThree += max(tempElves)
        tempElves.remove(max(tempElves))
    return topThree


elves = assignToElves(readFile(ELVE_DATA))
print(max(elves))
print(getTopThreeElves(elves))
