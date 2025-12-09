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
# biggestRectangle = 50
# data = test

lines = data.splitlines()

points = []

for line in lines:
    point = Point(*map(int, line.split(",")))
    points.append(point)

maxArea = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = points[i]
        b = points[j]
        xDiff = abs(a.x - b.x) + 1
        yDiff = abs(a.y - b.y) + 1
        area = xDiff * yDiff
        if area > maxArea:
            maxArea = area

print(maxArea)
