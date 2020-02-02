"""
EXERCISE-008


-   Define a function is_palindrome() that recognizes palindromes 
    (i.e. words that look the same written backwards). 
-   For example, is_palindrome("radar") should return True.


"""


def is_palindrome(text):
    
    if text == text[::-1]:
        return True
    else:
        return False


print(is_palindrome("radar"))
print(is_palindrome("non-palindrome-radar"))