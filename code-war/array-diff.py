"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]

array_diff([1,2,2,2,3,5,5,6,7],[2,6]) == [1,3,5,5,7]
"""
"""
Besst solution :
    def array_diff(a, b):
        return [x for x in a if x not in set(b)]


xx = []
for x in a:
    if x not in set(b):
        xx.append(x)


"""


def array_to_duplicate_diff(array_raw, array_to_cut):
    if len(array_to_cut) == 1:
        array_beauty = []
        i = 0
        while i < len(array_raw):
            if array_raw[i] != array_to_cut[0]:
                array_beauty.append(array_raw[i])
            i += 1
        return array_beauty
    elif len(array_to_cut) > 1:
        i = 0
        while i < len(array_raw):
            k = 0
            while k < len(array_to_cut):
                if array_raw[i] == array_to_cut[k]:
                    array_raw[i] = "unique"
                k += 1
            i += 1
        return array_raw
    else:
        return array_raw


def array_diff(array_raw, array_to_cut):
    array_to_clean = array_to_duplicate_diff(array_raw, array_to_cut)
    return array_to_clean


result = array_diff([-12, -1, 15, 0, -16, 0, -6,
                     11, -7, -7, 15, 20], [-7, -5, 17])
print(result)
