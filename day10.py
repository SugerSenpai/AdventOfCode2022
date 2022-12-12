from util import *
INSTRUCTION_DATA = "day10_input.txt"


def calculateCycles(instructions: list):
    drawing = [['' for _ in range(40)]for _ in range(6)]
    sumSignalStrength = 0
    cycle = 0
    x = 1
    for instruction in instructions:
        if instruction[0:4] == 'addx':
            registerChange = instruction[5:len(instruction)]
            waitCycles = 2
        else:
            waitCycles = 1
        for _ in range(waitCycles):
            if (cycle % 40-1) <= (x) <= (cycle % 40+1):
                drawing[cycle//40][cycle % 40] = '#'
            else:
                drawing[cycle//40][cycle % 40] = ' '
            cycle += 1
            if (cycle+20) % 40 == 0:
                # print("Cycle strength during cycle",cycle, "is:" ,x*cycle)
                sumSignalStrength += x*cycle
        x += int(registerChange)
        registerChange = 0
    for row in drawing:
        print("".join(row))
    print(sumSignalStrength)


instructions = readFile(INSTRUCTION_DATA)
calculateCycles(instructions)
