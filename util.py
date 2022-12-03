def readFile(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    return lines


def printArray(array):
    for line in array:
        print(line)
