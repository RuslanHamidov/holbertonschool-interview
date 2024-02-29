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


boxes = [ [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6] ]



print(canUnlockAll(boxes))
