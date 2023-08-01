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
    n = len(boxes)
    visited_boxes = [False] * n
    visit_box(0, visited_boxes, boxes)
    """the all function returns true if all its values are true"""
    return all(visited_boxes)
