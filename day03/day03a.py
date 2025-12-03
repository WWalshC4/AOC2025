#!/usr/bin/env python3

import os

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """987654321111111
811111111111119
234234234234278
818181911112111
"""
# maxJoltage == 357
# data = test

maxJoltage = 0

lines = data.splitlines()
for batteryBank in lines:
    num1 = 0
    num2 = 0

    for index in range(len(batteryBank)):
        thisNum = int(batteryBank[index])
        if thisNum > num1 and index < (len(batteryBank) - 1):
            num1 = thisNum
            num2 = 0
        elif thisNum > num2:
            num2 = thisNum
    joltage = int(str(num1) + str(num2))
    maxJoltage += joltage

print(maxJoltage)
