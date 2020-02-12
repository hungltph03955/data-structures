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


besst solution:

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

"""

from collections import Counter


def duplicate_encode(word):
    # Counter: ham dung de thong ke tan xuat xuat hien cua 1 gia tri trong mang
    word = word.lower()
    new_string = ''
    count = Counter(word)
    print(count)
    for x in word:
        if count[x] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string


# value = "recede"
value = "Success"
result = duplicate_encode(value)
print(result)
