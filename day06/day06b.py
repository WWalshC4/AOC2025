#!/usr/bin/env python3

import os
import math

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = "".join(
    [
        "123 328  51 64 \n",
        " 45 64  387 23 \n",
        "  6 98  215 314\n",
        "*   +   *   +  \n",
    ]
)

# totalSum = 3263827
# data = test

totalSum = 0

lines = data.splitlines()


def calculateProblem(problem):
    print(problem)
    operand = problem.pop()
    if operand == "+":
        operand = sum
    elif operand == "*":
        operand = math.prod
    problem = list(map(int, problem))
    result = operand(problem)
    return result


lineCount = len(lines)
lineLength = 0
for line in lines:
    if (len(line)) > lineLength:
        lineLength = len(line)

problems = []
lastPos = 0

for pos in range(lineLength + 1):
    allSpaces = True
    for lineIndex in range(lineCount):
        thisLineLength = len(lines[lineIndex])
        if pos >= thisLineLength:
            char = " "
        else:
            char = lines[lineIndex][pos : pos + 1]
        if char != " ":
            allSpaces = False
    if allSpaces:
        thisProblem = []
        for lineIndex in range(lineCount):
            thisLine = lines[lineIndex][lastPos:pos]
            thisProblem.append(thisLine)
        lastPos = pos + 1
        problems.append(thisProblem)


for problem in problems:
    operand = problem.pop().strip()
    if operand == "+":
        operand = sum
    elif operand == "*":
        operand = math.prod

    newProblem = []

    for pos in range(len(problem[0]) - 1, -1, -1):
        newNum = ""
        for num in problem:
            char = num[pos : pos + 1]
            if char == " ":
                char = ""
            newNum += char
        newProblem.append(int(newNum))

    problemTotal = operand(newProblem)
    totalSum += problemTotal

print(totalSum)
