#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for num in my_list:
        if my_list.count(num) == 1: 
            result = result + num
        else:
            i = 0
            
            if i == 0:
                temp = num
            if i > 0:
                while i != my_list.count(num):
                    my_list[my_list.index(num)] = 0
                    i+=1
            result = result + temp
    return result
