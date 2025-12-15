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
# fewestPresses = 7
# data = test

fewestPresses = 0

pattern = r"\[([\#\.]+)\]([ \(\)\d\,]+)\{([\d,]+)}"
buttonPattern = r"\(([\d,]+)\)"
for match in re.finditer(pattern, data):
    lights = list(map(lambda x: x == "#", match.group(1)))

    buttons = []
    lightsByButton = {}
    buttonIndex = 0
    for buttonMatch in re.finditer(buttonPattern, match.group(2)):
        button = list(map(int, buttonMatch.group(1).split(",")))
        buttons.append(button)
        for light in button:
            if not light in lightsByButton:
                lightsByButton[light] = {}
            lightsByButton[light][buttonIndex] = True
        buttonIndex += 1

    pressRound = 1
    found = False

    while found == False:
        for combination in itertools.combinations(buttons, pressRound):
            checkLights = [False] * len(lights)
            for buttonToPress in combination:
                for light in buttonToPress:
                    checkLights[light] = not (checkLights[light])
            if checkLights == lights:
                found = True
                fewestPresses += pressRound
                break
        pressRound += 1

print(fewestPresses)
