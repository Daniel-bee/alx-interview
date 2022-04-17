#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    if type(boxes) is not list:
        return False
    if len(boxes[0]) == 1:
        issamenumber = True
        for list_ in range(1, len(boxes)):
            if len(boxes[list_]) == 0:
                continue
            if len(boxes[0]) != len(boxes[list_]):
                issamenumber = False
                break
        return issamenumber
    first = boxes[0][0]
    last = boxes[0][len(boxes[0]) - 1]
    flag = 0
    for x in range(1, len(boxes)):
        for y in range(len(boxes[x])):
            if boxes[x][y] >= first and boxes[x][y] <= last:
                flag = 1
            else:
                flag = 0
                break
    if flag == 0:
        return False
    return True
