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


best solution:

def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

"""


def get_sum(value_1, value_2):
    if value_1 == value_2:
        return value_1
    else:
        result = 0
        dir_start = value_1
        dir_end = value_2
        if value_2 < value_1:
            dir_start = value_2
            dir_end = value_1
        for x in range(dir_start, dir_end):
            result += x
        result += dir_end
        return result


result = get_sum(-5, 5)
print(result)
