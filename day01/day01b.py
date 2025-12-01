#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
# zeroes == 6
# data = test

zeroes = 0
position = 50

lines = data.splitlines()
for instruction in lines:
    instruction = instruction.replace("L", "-")
    instruction = instruction.replace("R", "")
    instruction = int(instruction)
    eachClick = instruction / abs(instruction)

    for click in range(abs(instruction)):
        position += eachClick
        if position == 100:
            position = 0
        if position == -1:
            position = 99
        if position == 0:
            zeroes += 1
print(zeroes)
