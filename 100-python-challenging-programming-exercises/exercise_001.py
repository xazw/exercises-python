"""
EXERCISE-001
SOLVED-20170422-152911

- Find all numbers divisible by 7 that are not a multiple of 5, and between 2000 and 3200 (both included). 
- The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:  Consider use range(#begin, #end) method

"""


l = [str(x) for x in range(2000, 3201)
        if (x % 7 == 0) and (x % 5 != 0)]
print(", ".join(l))

