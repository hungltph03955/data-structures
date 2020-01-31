"""
Examples
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true
isSquare(26) returns  false
Sample Tests:
test.describe( is_square )
test.it( should work for some examples )
test.assert_equals(is_square(-1), False,  -1: Negative numbers cannot be square  numbers )
test.assert_equals(is_square( 0), True,  0 is a square number )
test.assert_equals(is_square( 3), False,  3 is not a square number )
test.assert_equals(is_square( 4), True,  4 is a square number )
test.assert_equals(is_square(25), True,  25 is a square number )
test.assert_equals(is_square(26), False,  26 is not a square number )

best solution :

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

"""

import math


def is_square(input_int):
    if input_int < 0:
        return False
    else:
        babylon = math.sqrt(input_int)
        if int(babylon + 0.5) ** 2 != input_int:
            return False
        else:
            return True

    # if input_int < 0:
    #     return False
    # else:
    #     x = input_int // 2
    #     seen = set([x])
    #     while x * x != input_int:
    #         x = (x + (input_int // x)) // 2
    #         if x in seen:
    #             return False
    #         seen.add(x)
    #     return True


value_test = 25
result = is_square(value_test)
print(result)
