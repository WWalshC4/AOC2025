#!/usr/bin/env python3

import os

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
# accessibleRolls = 13

# data = test

grid = []

lines = data.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)

# for gridline in grid:
#    print("".join(gridline))

maxY = len(grid)
maxX = len(grid[0])

accessibleRolls = 0

for yPos, row in enumerate(grid):
    for xPos, position in enumerate(row):
        if position == "@":
            adjacentRolls = 0
            for xDiff in range(-1, 2):
                for yDiff in range(-1, 2):
                    if xDiff == 0 and yDiff == 0:
                        continue
                    newX = xPos + xDiff
                    newY = yPos + yDiff
                    if 0 <= newX < maxX and 0 <= newY < maxY:
                        if grid[newY][newX] == "@":
                            adjacentRolls += 1
            if adjacentRolls < 4:
                accessibleRolls += 1

print(accessibleRolls)
