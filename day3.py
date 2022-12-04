from util import readFile, printArray

COMPARTMENT_DATA = "day3_input.txt"


def getPriority(compartments: list):
    priorityList = []
    for compartment in compartments:
        firstPart = compartment[:len(compartment)//2]
        secondPart = compartment[len(compartment)//2:]
        for char in firstPart:
            if char in secondPart:
                priorityList += [ord(char) - 38 if ord(char)
                                 < 97 else ord(char)-96]
                break
    return priorityList


def getGroupPriority(compartments: list):
    groupPriorityList = []
    for x in range(0, len(compartments), 3):
        firstRucksack = compartments[x]
        secondRucksack = compartments[x+1]
        thirdRucksack = compartments[x+2]
        for char in firstRucksack:
            if char in secondRucksack and char in thirdRucksack:
                groupPriorityList += [ord(char) -
                                      38 if ord(char) < 97 else ord(char)-96]
                break
    return groupPriorityList


rucksacks = readFile(COMPARTMENT_DATA)
compartmentPriorityList = getPriority(rucksacks)
print(sum(compartmentPriorityList))
groupPriorityList = getGroupPriority(rucksacks)
print(sum(groupPriorityList))
