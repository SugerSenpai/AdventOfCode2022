from util import *
ASSINGMENT_DATA = "day4_input.txt"

# could have done it with sets too, but realized later 
# for example: checking if intersection is equal to assignment length
def getFullyContainedAssignments(assignments: list):
    fullyContainedAssignments = 0
    for assignment in assignments:
        assignmentOne, assignmentTwo = assignment.split(",", 1)
        assignmentOne_1, assignmentOne_2 = assignmentOne.split("-", 1)
        assignmentTwo_1, assignmentTwo_2 = assignmentTwo.split("-", 1)
        temp1 = int(assignmentOne_1) - int(assignmentTwo_1)
        temp2 = int(assignmentOne_2) - int(assignmentTwo_2)
        if (temp1 <= 0 and temp2 >= 0) or (temp1 >= 0 and temp2 <= 0):
            fullyContainedAssignments += 1
    return fullyContainedAssignments

def getOverlappingAssignments(assignments: list):
    overlappingAssingments = 0
    for assignment in assignments:
        assignmentOne, assignmentTwo = assignment.split(",", 1)
        assignmentOne_1, assignmentOne_2 = assignmentOne.split("-", 1)
        assignmentTwo_1, assignmentTwo_2 = assignmentTwo.split("-", 1)
        assignmentOneSet = set(range(int(assignmentOne_1), int(assignmentOne_2)+1))
        assignmentTwoSet = set(range(int(assignmentTwo_1), int(assignmentTwo_2)+1))
        if assignmentOneSet.intersection(assignmentTwoSet):
            overlappingAssingments += 1
    return overlappingAssingments

assignmentList = readFile(ASSINGMENT_DATA)
print(getFullyContainedAssignments(assignmentList))
print(getOverlappingAssignments(assignmentList))

