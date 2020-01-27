"""
EXERCISE-002
SOLVED-20170422-234451

Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8

Then, the output should be: 40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


"""



factorial = lambda x: x * factorial(x-1) if x != 1 else x





"""
---------------------------
ORIGINAL-SOLUTION:


Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print fact(x)

"""