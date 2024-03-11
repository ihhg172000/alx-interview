#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    if not isinstance(boxes, list):
        return False

    boxes = [{"opened": False, "keys": keys} for keys in boxes]
    keys_stack = [0]
    while keys_stack:
        top = keys_stack.pop()
        if top < len(boxes) and not boxes[top]["opened"]:
            boxes[top]["opened"] = True
            keys_stack.extend(boxes[top]["keys"])
    return all(box["opened"] for box in boxes)
