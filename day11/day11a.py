#!/usr/bin/env python3

import os
import math
import re

try:
    inputFile = open("./input.txt", "r")
    data = inputFile.read()
    inputFile.close()
except:
    pass

test = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
# differentPaths = 5
# data = test

differentPaths = 0

devices = {}
deviceConnectionsOut = {}
deviceConnectionsIn = {}


lines = data.splitlines()

for line in lines:
    connections = line.replace(":", "").split()
    startDevice = connections.pop(0)
    devices[startDevice] = {}
    deviceConnectionsOut[startDevice] = connections
    for endDevice in connections:
        if not endDevice in deviceConnectionsIn:
            deviceConnectionsIn[endDevice] = []
        deviceConnectionsIn[endDevice].append(startDevice)


def visitParents(node):
    global differentPaths
    if node in deviceConnectionsIn:
        for parentNode in deviceConnectionsIn[node]:
            if parentNode == "you":
                differentPaths += 1
            visitParents(parentNode)


visitParents("out")

print(differentPaths)
