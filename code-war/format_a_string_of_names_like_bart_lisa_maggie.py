"""
Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Sample Tests:
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa',
"Must work with two names")
Test.assert_equals(namelist([{'name': 'Bart'}]),
                   'Bart', "Wrong output for a single name")
Test.assert_equals(namelist([]), '', "Must work with no names")


best solution:

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

"""


def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


# def namelist(value):
#     string_graft = ''
#
#     for key in range(len(value)):
#         if key == 0:
#             string_graft += value[key]['name']
#         elif key == len(value) - 1:
#             string_graft += ' & ' + value[key]['name']
#         else:
#             string_graft += ', ' + value[key]['name']
#
#     return string_graft


array_test = [{'name': 'Bart'}, {'name': 'Lisa'}, {
    'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]

results = namelist(array_test)
print(results)
