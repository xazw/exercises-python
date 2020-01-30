"""
EXERCISE-004
SOLVED-20190817-192249

Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.


"""


def char_is_vowel(char): 
    return True if char in ["a", "e", "i", "o", "u"]  \
      else False


print(char_is_vowel("m"))
print(char_is_vowel("a"))
