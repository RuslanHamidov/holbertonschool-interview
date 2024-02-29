#!/usr/bin/python3

'''
Lockboxes algorithm
'''


def canUnlockAll(boxes):
  unlocked = [False] * len(boxes)  # Initialize a list to track unlocked boxes
  unlocked[0] = True  # Mark the first box as unlocked

  for i, box_keys in enumerate(boxes):
    for key in box_keys:
      if 0 <= key < len(boxes) and not unlocked[key]:  # Check key validity and unlocked status
        unlocked[key] = True

  return all(unlocked)
