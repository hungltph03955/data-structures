"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(array_raw, array_to_cut):
    array_unique = []
    if len(array_to_cut) > 0:
        i = 0
        while i < len(array_raw):
            k = 0
            while k < len(array_to_cut):
                if array_raw[i] != array_to_cut[k]:
                    if len(array_unique) > 0:
                        l = 0
                        while l < len(array_unique):
                            if array_raw[i] != array_unique[l]:
                                array_unique.append(array_raw[i])
                            l += 1
                    else:
                        array_unique.append(array_raw[i])
                k += 1
            i += 1
    else:
        array_unique = array_raw

    return array_unique


array_raw = [1, 1, 2, 3, 4, 5, 2, 2, 5, 5]
array_to_cut = [2, 5]
result = array_diff(array_raw, array_to_cut)
print(result)
