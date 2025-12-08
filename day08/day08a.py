#!/usr/bin/env python3

import os
import math
import uuid
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
# data = test

circuitsToConnect = 1000

if data == test:
    circuitsToConnect = 10

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

distances.sort(key=lambda d: d.distance, reverse=True)

circuits = []
for box in boxes:
    circuit = set()
    circuit.add(box)
    circuits.append(circuit)

for i in range(circuitsToConnect):
    nextClosestPair = distances.pop()
    boxA = nextClosestPair.boxA
    boxB = nextClosestPair.boxB
    alreadyConnected = False

    for circuit in circuits:
        if boxA in circuit and boxB in circuit:
            alreadyConnected = True
            break
    if alreadyConnected:
        continue

    newCircuit = set()
    newCircuit.add(boxA)
    newCircuit.add(boxB)
    for circuit in circuits:
        if boxA in circuit:
            newCircuit.update(circuit)
            circuit.clear()
        if boxB in circuit:
            newCircuit.update(circuit)
            circuit.clear()
    circuits.append(newCircuit)

circuits = [circuit for circuit in circuits if circuit != set()]
circuits.sort(key=lambda circuit: len(circuit), reverse=True)

countOfThreeLargest = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

print(countOfThreeLargest)
