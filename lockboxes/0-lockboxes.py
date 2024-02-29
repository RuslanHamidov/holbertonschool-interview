#!/usr/bin/python3

'''
Lockboxes algorithm
'''


def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    for i, box_keys in enumerate(boxes):
        for key in box_keys:
            if 0 <= key < len(boxes) and not unlocked[key]:
                unlocked[key] = True

    return all(unlocked)
