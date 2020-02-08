"""
Duplicate Encoder

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes:

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")

Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")

Test.assert_equals(duplicate_encode("(( @"),"))((")
"""


def duplicate_encode(word):
    string = ""
    prev = ""
    word_lower = list(word.lower())
    for i in range(len(word_lower)):
        print(i)
        print(word_lower[i])
        if i == 0:
            string += '('
            prev = word_lower[i]
        elif word_lower[i] == prev:
            string += '('
            prev = word_lower[i]
        else:
            string += ')'

    print(string)
    return string


value = "recede"
# value = "Success"
result = duplicate_encode(value)
print(result)
