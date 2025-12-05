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

freshIngredients = set()

for freshIngredientsDataItem in freshIngredientsData:
    start, end = freshIngredientsDataItem.split("-")
    freshIngredients.update(range(int(start), int(end) + 1))

freshAvailableIngredients = 0

for availableIngredient in availableIngredients:
    if availableIngredient in freshIngredients:
        freshAvailableIngredients += 1

print(freshAvailableIngredients)
