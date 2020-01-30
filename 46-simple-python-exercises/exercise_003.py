"""
EXERCISE-003
SOLVED-20190817-192044

Define a function that computes the length of a given list
or string. (Rewrite Python's len() function.)

"""


def compute_length(list_item):

    count = 0
    for i in list_item:
        count += 1
    return count

test_list = [1, "apples", 2, "chicken"]
print( compute_length(test_list) )
