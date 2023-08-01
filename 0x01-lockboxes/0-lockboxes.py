#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    function to solve the lockboxes problem.
    """
    unlocked_keys = [0]
    for id, box in enumerate(boxes):
        if len(box) == 0:
            continue
        for key in box:
            """
            ensure the key has a box and the box has not been visited
            """
            if key != id and key < len(boxes) and key not in unlocked_keys:
                unlocked_keys.append(key)
    return len(unlocked_keys) == len(boxes)
