#!/usr/bin/env python3

import os
import math

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
# totalSum = 4277556
# data = test

totalSum = 0

lines = data.splitlines()


def calculateProblem(problem):
    operand = problem.pop()
    if operand == "+":
        operand = sum
    elif operand == "*":
        operand = math.prod
    problem = list(map(int, problem))
    result = operand(problem)
    return result


moreSums = True
while moreSums:
    thisProblem = []
    restOfLines = []
    for line in lines:
        try:
            nextData, restOfLine = line.split(None, maxsplit=1)
        except:
            nextData = line.strip()
            restOfLine = None
            moreSums = False
        thisProblem.append(nextData)
        restOfLines.append(restOfLine)
    lines = restOfLines
    problemSum = calculateProblem(thisProblem)
    totalSum += problemSum

print(totalSum)
