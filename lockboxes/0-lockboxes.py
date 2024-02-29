#!/usr/bin/python3

'''
Lockboxes algorithm
'''


def canUnlockAll(boxes):
    index_counter = 0
    box_open = set()
    for lists in boxes:
        for elements in lists:
            index_counter = 0
            for index_counter in range(1, len(boxes)):
                if elements == index_counter:
                    box_open.add(elements)
                    break
    list(box_open)
    if(len(box_open) == len(boxes) - 1):
        return True
    else:
        return False

boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))