#!/usr/bin/env python3

import os
import math

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
# timelines = 40
# data = test

timelines = 0

grid = []

lines = data.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)

maxY = len(grid)
maxX = len(grid[0])

startYPos = 0
startXPos = grid[startYPos].index("S")

stack = [(startXPos, startYPos)]
while len(stack) > 0:
    xPos, yPos = stack.pop()
    freeTravel = True
    increment = 0
    while freeTravel:
        increment += 1
        if (yPos + increment) == maxY:
            timelines += 1
            freeTravel = False
        else:
            nextValue = grid[yPos + increment][xPos]
            if nextValue == "^":
                freeTravel = False
                stack.append((xPos - 1, yPos + increment))
                stack.append((xPos + 1, yPos + increment))


# for gridline in grid:
#    print("".join(gridline))

print(timelines)
