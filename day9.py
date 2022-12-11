from util import *
MOVE_DATA = "day9_input.txt"

Head = (0,0)
Tail = [(0,0) for i in range(9)]
moveTuples = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}

def calculatePositions(Head, Tail):
    xDiff = Head[0] - Tail[0]
    yDiff = Head[1] - Tail[1]
    if abs(xDiff) >= 2:
        Tail = (Head[0]+1 if Tail[0]>Head[0] else Head[0]-1, Head[1] )
    elif abs(yDiff) >= 2:
        Tail = (Head[0], Head[1]+1 if Tail[1]>Head[1] else Head[1]-1)
    return Tail
    

moves = readFile(MOVE_DATA)
visitedPositions = set()
visitedPositionsTail = set()
for move in moves:
    direction, repetitions = move.split()
    for repetition in range(int(repetitions)):
        Head = (Head[0] + moveTuples[direction][0], Head[1] + moveTuples[direction][1])
        Tail[0] = calculatePositions(Head,Tail[0])
        for i in range(1,9):
            Tail[i] = calculatePositions(Tail[i-1],Tail[i])
        visitedPositions.add(Tail[0])
        visitedPositionsTail.add(Tail[8])
        
print(len(visitedPositions))
print(len(visitedPositionsTail))