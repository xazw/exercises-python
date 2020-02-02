"""
EXERCISE-009
SOLVED-20200202-102937

-   Write a function is_member() that takes a value (i.e. a number, string, 
    etc) x and a list of values a, and returns True if x is a member of a, 
    False otherwise. 
-   (Note that this is exactly what the in operator does, but for the sake 
    of the exercise you should pretend Python did not have this operator.)

"""


def is_member(x, a):
    if x in a:
        return True
    else:
        return False



test_seq = [45, 17, 82, 85, 17, 49, 98, 9, 48, 64, 66, 43, 6, 9, 59, 94, 4, 11, 14, 77]
test_val = 98

print(is_member(test_val, test_seq))
print(is_member(28, test_seq))