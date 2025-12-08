#!/usr/bin/env python3

import os
import math
from collections import namedtuple

Box = namedtuple("Box", "x y z")

Distance = namedtuple("Distance", "distance boxA boxB")

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
# countOfThreeLargest = 40
data = test

lines = data.splitlines()

boxes = []

for line in lines:
    box = Box(*map(int, line.split(",")))
    boxes.append(box)


def straightLineDistance(boxA, boxB):
    xDiff = abs(boxA.x - boxB.x) ** 2
    yDiff = abs(boxA.y - boxB.y) ** 2
    zDiff = abs(boxA.z - boxB.z) ** 2

    distance = math.sqrt(xDiff + yDiff + zDiff)
    return distance


distances = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        boxA = boxes[i]
        boxB = boxes[j]
        distance = straightLineDistance(boxA, boxB)
        info = Distance(distance, boxA, boxB)
        distances.append(info)

distances.sort(key=lambda d: d.distance)

circuits = []

for distance in distances:
    boxA = distance.boxA
    boxB = distance.boxB

    alreadyConnected = False
    for circuit in circuits:
        if found:
            break
        for circuitDistance in circuit:
            circuitBoxA = circuitDistance.boxA
            circuitBoxB = circuitDistance.boxB
            if (
                boxA == circuitBoxA
                or boxA == circuitBoxB
                or boxB == circuitBoxA
                or boxB == circuitBoxB
            ):
                circuit.append(distance)
                found = True
                break
    if not found:
        circuits.append([distance])

print(len(circuits[0]))
