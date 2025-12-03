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
# maxJoltage == 3121910778619
# data = test

maxJoltage = 0

lines = data.splitlines()
for batteryBank in lines:
    batteriesToTurnOn = [-1] * 12

    for bankIndex in range(len(batteryBank)):
        thisBattery = int(batteryBank[bankIndex])
        remainingBatteries = len(batteryBank) - 1 - bankIndex
        for checkIndex in range(len(batteriesToTurnOn)):
            remainingSlots = len(batteriesToTurnOn) - 1 - checkIndex
            if thisBattery > batteriesToTurnOn[checkIndex]:
                if remainingSlots <= remainingBatteries:
                    batteriesToTurnOn[checkIndex] = thisBattery
                    for resetIndex in range(checkIndex + 1, len(batteriesToTurnOn)):
                        batteriesToTurnOn[resetIndex] = -1
                    break
    joltage = int("".join(map(str, batteriesToTurnOn)))

    maxJoltage += joltage

print(maxJoltage)
