#!/usr/bin/env python3

import os

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
# freshAvailableIngredients = 3
# data = test

sections = data.split("\n\n")

freshIngredientsData = sections[0].splitlines()
availableIngredients = list(map(int, sections[1].splitlines()))

freshIngredients = []

for freshIngredientsDataItem in freshIngredientsData:
    start, end = freshIngredientsDataItem.split("-")
    freshIngredients.append((int(start), int(end)))

sorted(freshIngredients)

freshAvailableIngredients = 0

for availableIngredient in availableIngredients:
    for freshIngredient in freshIngredients:
        if freshIngredient[0] <= availableIngredient:
            if freshIngredient[1] >= availableIngredient:
                freshAvailableIngredients += 1
                break

print(freshAvailableIngredients)
