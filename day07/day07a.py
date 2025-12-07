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
# beamSplits = 21
# data = test

beamSplits = 0

grid = []

lines = data.splitlines()

for line in lines:
    line = line.replace("S", "|")
    gridline = list(line)
    grid.append(gridline)


# for gridline in grid:
#   print("".join(gridline))

maxY = len(grid)
maxX = len(grid[0])

for yPos, row in enumerate(grid):
    for xPos, value in enumerate(row):
        if value == "|":
            newX = xPos
            newY = yPos + 1
            if newY >= maxY:
                break
            nextValue = grid[newY][newX]
            if nextValue == "^":
                beamSplits += 1
                leftValue = grid[newY][newX - 1]
                rightValue = grid[newY][newX + 1]
                if leftValue == "^":
                    print("panic Left")
                if rightValue == "^":
                    print("panic Right")
                grid[newY][newX - 1] = "|"
                grid[newY][newX + 1] = "|"
            else:
                grid[newY][newX] = "|"

print(beamSplits)
