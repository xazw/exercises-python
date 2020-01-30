"""
EXERCISE-006
SOLVED-20200130-175229

-   Define a function sum() and a function multiply() that
    sums and multiplies (respectively) all the numbers in a list of numbers.
-   E.g. sum([1, 2, 3, 4]) should return 10,
    and multiply([1, 2, 3, 4]) should return 24.


"""

import operator


def x_operation(list_item, op_type):
    if op_type == 'sum':
        op_type = 'add'
        results = 0

    if op_type == 'multiply':
        op_type = 'mul'
        results = 1

    for n, i in enumerate(list_item):
        results = getattr(operator, op_type)(results, i)

    return results


def test_assumptions(list_item):
    assert x_operation(list_item, 'sum') == 10, "Failed to sum"
    assert x_operation(list_item, 'multiply') == 24, "Failed to multiply"


test_list = [1, 2, 3, 4]
test_assumptions(test_list)
