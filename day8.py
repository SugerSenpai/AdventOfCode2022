from util import *
TREE_DATA = "day8_input.txt"
Directions = [(1,0),(0,1),(-1,0),(0,-1)]
def geVisibleTrees(trees: list):
    visibleCount = 0
    for row in range(len(trees)):
        for column in range(len(trees[row])):
            for x,y in Directions:
                targetRow = row
                targetColumn = column
                isVisible = True
                while(isVisible):
                    targetRow += x
                    targetColumn += y
                    if 0 <= targetRow<len(trees) and 0 <= targetColumn<len(trees[row]):
                        if trees[targetRow][targetColumn] >= trees[row][column]:
                            isVisible = False
                    else:
                        break
                if isVisible:
                    visibleCount += 1
                    break
    return visibleCount

def getScenicScore(trees: list):
    scenicScore = []
    for row in range(len(trees)):
        for column in range(len(trees[row])):
            score = 1
            for x,y in Directions:
                distance = 0
                targetRow = row
                targetColumn = column
                while(True):
                    targetRow += x
                    targetColumn += y
                    if 0 <= targetRow<len(trees) and 0 <= targetColumn<len(trees[row]):
                        distance +=1
                        if trees[targetRow][targetColumn] >= trees[row][column]:
                            break
                    else:
                        break
                score = distance * score
            scenicScore.append(score)
    return max(scenicScore)


trees = readFile(TREE_DATA)
visibleTrees = geVisibleTrees(trees)
print(visibleTrees)
maxScenicScore = getScenicScore(trees)
print(maxScenicScore)