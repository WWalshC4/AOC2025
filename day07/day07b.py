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
# timeLines = 40
# data = test

timeLines = 0

grid = []

lines = data.splitlines()

for line in lines:
    gridline = [0 if char == "." else 1 if char == "S" else char for char in line]
    grid.append(gridline)


maxY = len(grid)
maxX = len(grid[0])

for yPos, row in enumerate(grid):
    for xPos, value in enumerate(row):
        if value != "^" and value > 0:
            newX = xPos
            newY = yPos + 1
            if newY >= maxY:
                break
            nextValue = grid[newY][newX]
            if nextValue == "^":
                grid[newY][newX - 1] += value
                grid[newY][newX + 1] += value
            else:
                grid[newY][newX] += value


timeLines = sum(grid[maxY - 1])

print(timeLines)
