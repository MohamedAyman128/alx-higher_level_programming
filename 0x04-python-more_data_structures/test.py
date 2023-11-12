#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for num in my_list:
        trial = my_list.count(num)
        print(trial)
        if trial > 1:
            i = 0
            index = my_list.index(num)
            while i != trial:
                my_list[index] = 0
                i += 1
    for num in my_list:
        result = result + num
    return result
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))


# ----------------------------------------

# first

def uniq_add(my_list=[]):
    result = 0
    for num in my_list:
        trial = my_list.count(num)
        if trial == 1:
            result = result + num
        else:
            i = 0
            result = result + num
            while i > trial:
                my_list[my_list.index(num)] = 0
                i += 1

    return result
