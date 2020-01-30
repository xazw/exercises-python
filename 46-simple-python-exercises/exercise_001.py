"""
EXERCISE-01
SOLVED-20190817-191807

Define a function max() that takes two numbers as arguments and returns the largest of them. 
Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

"""


def new_max(a, b):

    assert b != a, "Values are the same."
    if a > b:
        return a
    elif b > a:
        return b

print(new_max(46, 46.5))
