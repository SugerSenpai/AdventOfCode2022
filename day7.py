from collections import defaultdict
from util import *
import json
FILE_DIRECTORY_DATA = "day7_input.txt"

def createFileSystem():
    directorySizes = defaultdict(int)
    path = []
    for line in cmdHistory:
        arguments = line.split()
        if arguments[1] == 'cd':
            if arguments[2] == '/':
                path = []
            if arguments[2] == '..':
                path.pop()
            else:
                path.append(arguments[2])
        elif arguments[1] == 'ls' or arguments[0] == 'dir':
            continue
        else:
            sizeOfDir = int(arguments[0])
            for i in range(1, len(path)+1):
                directorySizes["/".join(path[:i])] += sizeOfDir
    return directorySizes
    # credit to https://github.com/jonathanpaulson
    # i tried using a normal dict, trying to index it whenever i change the directory
    # but that lead to files missing in some areas and also wasn't quite as beautiful as using a defaultdic
    # and indexing it with the path
    # honestly I would have been pretty lost if it wasn't for discovering defaultdic through his solution
    """
            def createFileSystem():
            path = []
            directorySizes = {}
            directorySize = 0
            dictionaryIndex = 0
            for line in file_directory:
                arguments = line.strip().split()
                if arguments[1] == 'cd':
                    directorySize = 0
                if arguments[2] == '/':
                    path = []
                if arguments[2] == '..':
                    path.pop()
                else:
                    path.append(arguments[2])
                    dictionaryIndex += 1
                elif arguments[1] == 'ls' or arguments[0] == 'dir':
                    continue
                else:
                    directorySize += int(arguments[0])
                    directorySizes[dictionaryIndex] = {
                        "dirName": path[-1],
                        "dirSize": directorySize
                    }
            return directorySizes

        def calculateDirectories(directorySizes: dict, minSize: int, maxSize: int):
            sumOfDirs = 0
            for index in directorySizes:
                directorySize = directorySizes[index]['dirSize']
                if directorySize <= maxSize and minSize >= 0:
                    sumOfDirs += directorySize
            return sumOfDirs
    """

def calculateDirectories(directorySizes: dict, minSize: int, maxSize: int):
    sumOfDirs = 0
    for dir, size in directorySizes.items():
        if size <= maxSize and minSize >= 0:
            sumOfDirs += size
    return sumOfDirs

def freeDiskSpace(directorySizes: dict, spaceToBeDeleted: int):
    spaceToBeFreed = dirSizes['/']
    for dir, size in directorySizes.items():
        if size >= spaceToBeDeleted:
            spaceToBeFreed = spaceToBeFreed if size > spaceToBeFreed else size
    return spaceToBeFreed


cmdHistory = readFile(FILE_DIRECTORY_DATA)
dirSizes = createFileSystem()

# print(json.dumps(dirSizes, ensure_ascii=False, indent=4))
partOneSum = calculateDirectories(dirSizes, 0, 100000)
print(partOneSum)

spaceToBeDeleted = dirSizes['/'] - 40000000
# disk space: 70000000, unused space: 30000000

dirToBeDeleted = freeDiskSpace(dirSizes, spaceToBeDeleted)
print(dirToBeDeleted)


    


