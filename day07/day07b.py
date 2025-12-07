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
    line = line.replace("S", "|")
    gridline = list(line)
    grid.append(gridline)

maxY = len(grid)
maxX = len(grid[0])

for yPos, row in enumerate(grid):
    timelinesThisRow = 0
    splittersThisRow = 0
    for xPos, value in enumerate(row):
        if value == "^":
            splittersThisRow += 1
        if value == "|":
            timelinesThisRow += 1
            newX = xPos
            newY = yPos + 1
            if newY >= maxY:
                break
            nextValue = grid[newY][newX]
            if nextValue == "^":
                grid[newY][newX - 1] = "|"
                grid[newY][newX + 1] = "|"
            else:
                grid[newY][newX] = "|"
    if splittersThisRow > 0:
        timelines += timelinesThisRow

for gridline in grid:
    print("".join(gridline))

print(timelines)
