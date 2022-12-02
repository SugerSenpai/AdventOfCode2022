ELVE_DATA = "day1_input.txt"

def readFile(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    return lines


def assignToElves(calorieArray):
    elves = []
    counter = 0
    for line in calorieArray:
        if line == "":
            elves.append(counter)
            counter = 0
            continue
        counter = counter + int(line)
    return elves

def printArray(array):
    for line in array:
        print(line)

elves = assignToElves(readFile(ELVE_DATA))
# printArray(elves)
print(max(elves))
