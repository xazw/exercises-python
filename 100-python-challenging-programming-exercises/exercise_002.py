"""
EXERCISE-002
SOLVED-20170422-234451

- Compute the factorial of given numbers. 
- The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8

Then, the output should be: 40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


"""



factorial = lambda x: x * factorial(x-1) if x != 1 else x

test_random_numbers = [3, 24, 38, 60, 63, 23, 42, 41, 20]
for num in test_random_numbers:
    print(factorial(num), end=", ")