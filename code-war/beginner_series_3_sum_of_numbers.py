"""
Beginner Series #3 Sum of Numbers

Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2


Sample Tests:
Test.assert_equals(get_sum(0,1),1)
Test.assert_equals(get_sum(0,-1),-1)
"""


def get_sum(value_1, value_2):
    result = 0
    for x in range(value_1, value_2 + 1):
        result += x
    return result


result = get_sum(0, 14)
print(result)
