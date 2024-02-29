#!/usr/bin/python3

'''
Lockboxes algorithm
'''


def canUnlockAll(boxes):
  box_open = set()
  for i, box in enumerate(boxes):
    if any(i in inner_box for inner_box in boxes[:i] + boxes[i+1:]):
      box_open.add(i)
  return len(box_open) == len(boxes)

