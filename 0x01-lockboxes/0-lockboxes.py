# usr/bin/python3
"""
Solves the lock boxes puzzle
"""


def canUnlockAll(boxes):
    """
    boxes: list of box container keys
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
