#!/usr/bin/python3
"""
0-lockboxes.py
"""


def visit_box(box_id, visited_boxes, boxes):
    """
    helper function to solve the lockboxes problem
    using depth-first-search.
    """
    visited_boxes[box_id] = True
    for key in boxes[box_id]:
        """
        ensure the key has a box and the box has not been visited
        """
        if key < len(boxes) and visited_boxes[key] is False:
            """ visit the box """
            visit_box(key, visited_boxes, boxes)
        continue


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
    if len(unlocked_keys) == len(boxes):
        return True
    else:
        return False
