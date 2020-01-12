import stackClassBase


def reverse_file(filename):
    """ Overwrite given file with its contents line-by-line reversed """
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
        # we will re-insert newlines when writing
    original.close()


# now we overwrite with contents in LEFO order
output = open(filename, 'w')
# reopening file overwrites original
while not s.is_empty():
    output.write(s.pop() + '\n')
    # re - insert newline characters
output.close()
