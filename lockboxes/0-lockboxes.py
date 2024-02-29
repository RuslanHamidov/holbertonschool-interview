#!/usr/bin/python3

'''
Lockboxes algorithm
'''

def canUnlockAll(boxes):
    index_counter = 0
    box_open = []
    for lists in boxes:
        for elements in lists:
            index_counter = 0
            for index_counter in range(1, len(boxes)):  
                if elements == index_counter:
                    box_open.append('opened')
                    break

    if(len(box_open) == len(boxes)-1):
        print(True)
    else:
        print(False)

boxes = [[5], [4], [1], [2], []]

