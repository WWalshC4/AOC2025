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
# zeroes == 3
# data = test

zeroes = 0
position = 50

lines = data.splitlines()
for instruction in lines:
    instruction = instruction.replace("L", "-")
    instruction = instruction.replace("R", "")

    position += int(instruction)
    position = position % 100
    if position == 0:
        zeroes += 1

print(zeroes)
