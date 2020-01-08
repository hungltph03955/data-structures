class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def init(self):
        """Create an empty stack."""
        # nonpublic list instance
        self._data = []

    def len(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        # new item stored at end of list
        self._data.append(e)

    def top(self):
        """Return(but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty(Stack is empty)
            # the last item in the list

        return self._data[−1]

    def pop(self):
        """Remove and return the element from the top of the stack(i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty(Stack is empty)
            # remove last item from list

        return self._data.pop()


S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is empty())
print(S.pop())
print(S.is empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
