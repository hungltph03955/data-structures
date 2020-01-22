"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case


Sample Tests:
Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )


Besst solution :

def is_isogram(string):
    return len(string) == len(set(string.lower()))

"""


def is_isogram(string):
    if string != "":
        string_lower = string.lower()
        array_string = list(string_lower)
        arrayDupliacte = list(set(array_string))
        if len(arrayDupliacte) < len(array_string):
            return False
        else:
            return True
    else:
        return True


value = "moOse"
result = is_isogram(value)
print(result)
