"""
EXERCISE-007
SOLVED-20200130-175435

- Define a function reverse() that computes the reversal of a string. 
- E.g. reverse("I am testing") should return the string "gnitset ma I".


"""


def reverse(text):
    return text[::-1]


assert reverse("I am testing") == "gnitset ma I"
