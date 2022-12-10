from util import *
MOVE_DATA = "day9_input.txt"

Head = (0,0)
Tail = (0,0)
moveTuples = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}

def calculatePositions(Head, Tail):
    xDiff = Head[0] - Tail[0]
    yDiff = Head[1] - Tail[1]
    if abs(xDiff) == 2:
        Tail = (Head[0]+1 if Tail[0]>Head[0] else Head[0]-1, Head[1] )
    elif abs(yDiff) == 2:
        Tail = (Head[0], Head[1]+1 if Tail[1]>Head[1] else Head[1]-1)
    visitedPositions.add(Tail)
    return Tail
    

moves = readFile(MOVE_DATA)
visitedPositions = set()
for move in moves:
    direction, repetitions = move.split()
    for repetition in range(int(repetitions)):
        Head = (Head[0] + moveTuples[direction][0], Head[1] + moveTuples[direction][1])
        Tail = calculatePositions(Head,Tail)
print(len(visitedPositions))

#part 2 seems actually easy to implement, but somehow i can't get it right
#what i tried:
#implement another 8 Tails that take the tail before them as head and add 
#the position of the last tail to a set
# for me it returns 2340 which should be 2562 so idk where I went wrong (deleted part 2)