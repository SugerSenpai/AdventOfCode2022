import math
from util import *

MONKEY_DATA = "day11_input.txt"

file = open(MONKEY_DATA, "r")
monkeys = file.read()
monkeys = monkeys[:-1].split("\n\n")

monkeyItems = []
monkeyOperations = []
monkeyTest = []
monkeyTrue = []
monkeyFalse = []


def configureMonkeys(monkeys: list):
    for monkey in monkeys:
        monkeyNumber,items,operation,test,true,false = monkey.split("\n")
        monkeyItems.append(items.split(': ')[1].split(', '))
        monkeyOperations.append(operation.split('= ')[1].split(','))
        monkeyTest.append(int(test.split('by ')[1].split(',')[0]))
        monkeyTrue.append(int(true[-1:].split(',')[0]))
        monkeyFalse.append(int(false[-1:].split(',')[0]))


def calculateMonkeyBusiness(rounds: int):
    inspected = [0 for _ in range(len(monkeys))]
    for _ in range(rounds):
        for monkey in range(len(monkeys)):
            for item in monkeyItems[monkey]:
                item = eval("".join(monkeyOperations[monkey]).replace("old",str(item)))
                if rounds == 20:
                    item = item//3
                else:
                    item = item%divs
                isDividable = (item % monkeyTest[monkey]) == 0
                if isDividable:
                    monkeyItems[(monkeyTrue[monkey])].append(item)
                else:
                    monkeyItems[(monkeyFalse[monkey])].append(item)
                inspected[monkey] += 1
            monkeyItems[monkey] = []
    inspected.sort()
    print(inspected[-1]*inspected[-2])

configureMonkeys(monkeys)
part1 = calculateMonkeyBusiness(20)

divs = math.prod(monkeyTest)

monkeyItems = []
configureMonkeys(monkeys)
part2 = calculateMonkeyBusiness(10000)
