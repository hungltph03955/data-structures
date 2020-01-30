"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])


best solution :

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

"""


def unique_in_order(string_test):
    string_aray = list(string_test)
    array_uni = []
    i = 0
    while i < len(string_aray):
        if i == 0:
            array_uni.append(string_aray[0])
        else:
            if string_aray[i] != array_uni[-1]:
                array_uni.append(string_aray[i])
        i += 1

    return array_uni


string_test = 'ABBCcAD'

result = unique_in_order(string_test)
print(result)
