CRATE_DATA = "day5_input.txt"
Stacks = [['N','C','R','T','M','Z','P'],
 ['D','N','T','S','B','Z'],
 ['M','H','Q','R','F','C','T','G'],
 ['G','R','Z'],
 ['Z','N','R','H'],
 ['F','H','S','W','P','Z','L','D'],
 ['W','D','Z','R','C','G','M'],
 ['S','J','F','L','H','W','Z','Q'],
 ['S','Q','P','W','N']]

def readFile(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    return lines[10:]

def makeMoves(moves: list):
    for move in moves:
        splittedMove = move.split(" ")
        for i in range(int(splittedMove[1])):
            poppedLetter = Stacks[int(splittedMove[3])-1].pop()
            Stacks[int(splittedMove[5])-1].append(poppedLetter)

def makeMovesEnhanced(moves: list):
    for move in moves:
        splittedMove = move.split(" ")
        poppedLetters = []
        for i in range(int(splittedMove[1])):
            poppedLetters += Stacks[int(splittedMove[3])-1].pop()
        for i in range(len(poppedLetters)-1,-1,-1):
            Stacks[int(splittedMove[5])-1].append(poppedLetters[i])

crateMoves = readFile(CRATE_DATA)
# because we directly access the variable Stack, only one function can be called at a time
# makeMoves(crateMoves)
# makeMovesEnhanced(crateMoves)
for stack in Stacks:
    print(stack[len(stack)-1])
