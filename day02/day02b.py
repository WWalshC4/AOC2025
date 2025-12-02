#!/usr/bin/env python3

import os

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
# invalidIdsTotal == 4174379265
# data = test

invalidIdsTotal = 0

idRanges = data.split(",")
for idRange in idRanges:
    ends = idRange.split("-")
    start = int(ends[0])
    end = int(ends[1])

    for id in range(start, end + 1):
        idString = str(id)
        idStringLength = len(idString)
        isInvalid = False
        for subStringLength in range(1, int(idStringLength / 2) + 1):
            if isInvalid:
                continue
            if idStringLength % subStringLength == 0:
                repeats = int(idStringLength / subStringLength)
                substringStart = idString[0:subStringLength]
                testMatch = substringStart * repeats
                if testMatch == idString:
                    invalidIdsTotal += int(testMatch)
                    isInvalid = True

print(invalidIdsTotal)
