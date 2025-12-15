#!/usr/bin/env python3

import os
import math
import re
import itertools

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
# fewestPresses = 33
data = test

fewestPresses = 0

pattern = r"\[([\#\.]+)\]([ \(\)\d\,]+)\{([\d,]+)}"
buttonPattern = r"\(([\d,]+)\)"
for match in re.finditer(pattern, data):
    joltages = list(map(int, match.group(3).split(",")))

    buttons = []
    buttonIndex = 0
    for buttonMatch in re.finditer(buttonPattern, match.group(2)):
        button = list(map(int, buttonMatch.group(1).split(",")))
        buttons.append(button)
        buttonIndex += 1

    pressRound = 1
    found = False

    while found == False:
        for combination in itertools.combinations_with_replacement(buttons, pressRound):
            checkJoltages = [0] * len(joltages)
            for buttonToPress in combination:
                for index in buttonToPress:
                    checkJoltages[index] += 1
            if checkJoltages == joltages:
                found = True
                fewestPresses += pressRound
                break
        pressRound += 1

print(fewestPresses)
