#!/usr/bin/python3

'''
Lockboxes algorithm
'''

def canUnlockAll (box_list):
    bool_list = []
    for array in box_list:
        if (len(array)):
            bool_list.append(True)
        else:
            bool_list.append(False)
    all_except_last = bool_list[:-1]
    for boolean in all_except_last:
        return all(all_except_last) is True
