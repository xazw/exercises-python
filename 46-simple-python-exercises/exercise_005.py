"""
EXERCISE-005
SOLVED-20190817-193001

-   Write a function translate() that will translate a text into
    "rövarspråket" (Swedish for "robber's language"). 
-   Double every consonant and place an occurrence of "o" in between. 
-   For example, translate("this is fun") should return the 
    string "tothohisos isos fofunon".

"""


text = "this is fun"
text_expected_output = "tothohisos isos fofunon"

VOWELS = ["a", "e", "i", "o", "u"]
VOWELS += [c.upper() for c in VOWELS]

text_robber = "".join(
                        [c if (c in VOWELS) or (c == " ")
                           else c + "o" + c
                           for c in text
                        ])

print(text_robber)
print(text_expected_output)
assert text_robber == text_expected_output, "Not the same!"
