from collections import deque
from copy import deepcopy
from util import *
HEATMAP_DATA = "day12_input.txt"
MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def startAndEndPoint(heatmap: list):
    for row in range(len(heatmap)):
        for position in range(len(heatmap[row])):
            if heatmap[row][position] == 'S':
                startPos = row, position
            if heatmap[row][position] == 'E':
                endPos = row, position
    return startPos, endPos


def mapToHeight(heatmap: list):
    temp = deepcopy(heatmap)
    heightMap = [[0 for _ in range(len(temp[0]))] for _ in range(len(temp))]
    for row in range(len(temp)):
        for position in range(len(temp[row])):
            if ord(temp[row][position]) > 96:
                heightMap[row][position] = ord(temp[row][position])-96
            elif ord(temp[row][position]) == 'S':
                heightMap[row][position] = 1
            elif ord(temp[row][position]) == 'E':
                heightMap[row][position] = 26
    return heightMap


# because i never implemented dijkstra in python and didn't know deque exists, I used code from
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/12.py's solution
# for the calculatePath() function so I could learn from it
def calculatePath(part: int):
    Q = deque()
    path = set()
    if part == 1:
        Q.append((startPos, 0))
    elif part == 2:
        for row in range(len(heightMap)):
            for position in range(len(heightMap[row])):
                if heightMap[row][position] == 1:
                    Q.append(((row, position), 0))
    while (Q):
        (row, column), distance = Q.popleft()
        if (row, column) in path:
            continue
        path.add((row, column))
        if (endPos == (row, column)):
            return distance
        for x, y in MOVES:
            targetRow = row + x
            targetColumn = column+y
            if 0 <= targetRow < len(heightMap) and 0 <= targetColumn < len(heightMap[0]):
                if heightMap[targetRow][targetColumn] <= heightMap[row][column] + 1:
                    Q.append(((targetRow, targetColumn), distance+1))


heatmap = readFile(HEATMAP_DATA)
startPos, endPos = startAndEndPoint(heatmap)
heightMap = mapToHeight(heatmap)
steps1 = calculatePath(1)
print(steps1)
steps2 = calculatePath(2)
print(steps2)
