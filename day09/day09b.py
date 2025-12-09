#!/usr/bin/env python3

import os
import math
from collections import namedtuple

Point = namedtuple("Point", "x y")

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
# biggestRectangle = 24
# data = test

lines = data.splitlines()

redTiles = []
greenTiles = []

maxX = 0
maxY = 0

for line in lines:
    point = Point(*map(int, line.split(",")))
    redTiles.append(point)
    if point.x > maxX:
        maxX = point.x
    if point.y > maxY:
        maxY = point.y

maxArea = 0

for i in range(len(redTiles)):
    thisRedTile = redTiles[i]
    if i == len(redTiles) - 1:
        nextRedTile = redTiles[0]
    else:
        nextRedTile = redTiles[i + 1]
    thisX = thisRedTile.x
    nextX = nextRedTile.x
    thisY = thisRedTile.y
    nextY = nextRedTile.y

    xDiff = thisX - nextX
    yDiff = thisY - nextY

    if yDiff != 0:
        delta = yDiff // abs(yDiff)
        for j in range(1, abs(yDiff)):
            greenTiles.append(Point(thisX, thisY - (j * delta)))

    elif xDiff != 0:
        delta = xDiff // abs(xDiff)
        for j in range(1, abs(xDiff)):
            greenTiles.append(Point(thisX - (j * delta), thisY))


def printVis(scaleFactor=1):

    grid = []
    for row in range((maxY // scaleFactor) + 1):
        column = ["."] * ((maxX // scaleFactor) + 1)
        grid.append(column)

    for tile in redTiles:
        grid[(tile.y // scaleFactor)][(tile.x // scaleFactor)] = "0"

    for tile in greenTiles:
        grid[(tile.y // scaleFactor)][(tile.x // scaleFactor)] = "o"

    for row in grid:
        print("".join(row))


printVis(1000)
