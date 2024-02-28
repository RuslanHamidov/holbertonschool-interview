#!/usr/bin/python3

'''
Lockboxes algorithm
'''



def boxCheck(box_list):
    bool_list = []
    for array in box_list:
        if (len(array)):
            bool_list.append(True)
        else:
            bool_list.append(False)
    
    all_except_last = bool_list[:-1]
    
    print(all_except_last)
    for boolean in all_except_last:
        if(all(all_except_last) == True):
            return True
        else:
            return False
            
    