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
14-17

1
5
8
11
17
32
"""
# totalFreshIngredients = 14
# data = test

sections = data.split("\n\n")

freshIngredientsData = sections[0].splitlines()

freshIngredients = []

for freshIngredientsDataItem in freshIngredientsData:
    start, end = freshIngredientsDataItem.split("-")
    freshIngredients.append((int(start), int(end)))

freshIngredients.sort()


def combineRanges(range1, range2):
    newRange = None
    start1 = range1[0]
    start2 = range2[0]
    end1 = range1[1]
    end2 = range2[1]

    if start2 == end1 + 1:
        newRange = (start1, end2)
    elif start1 == end2 + 1:
        newRange = (start2, end1)
    else:
        if start1 >= start2:
            if end1 <= end2:
                newRange = range2
            else:
                if start1 <= end2:
                    if end1 >= end2:
                        newRange = (start2, end1)
        elif start2 >= start1:
            if end2 <= end1:
                newRange = range1
            else:
                if start2 <= end1:
                    if end2 >= end1:
                        newRange = (start1, end2)

    return newRange


combinedThisLoop = True
while combinedThisLoop:
    combinedIngredients = []
    combinedThisLoop = False
    while len(freshIngredients) > 0:
        thisIngredient = freshIngredients.pop(0)
        combinedIndexes = []
        for index in range(0, len(freshIngredients)):
            newRange = combineRanges(thisIngredient, freshIngredients[index])
            if newRange is not None:
                combinedThisLoop = True
                combinedIndexes.append(index)
                thisIngredient = newRange
        deletedIndices = 0
        for index in combinedIndexes:
            del freshIngredients[index - deletedIndices]
            deletedIndices += 1
        combinedIngredients.append(thisIngredient)
    freshIngredients = combinedIngredients
    freshIngredients.sort()

totalFreshIngredients = 0

for ingredientRange in freshIngredients:
    thisRangeCount = ingredientRange[1] - ingredientRange[0] + 1
    totalFreshIngredients += thisRangeCount

print(totalFreshIngredients)
