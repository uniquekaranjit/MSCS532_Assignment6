# ----------------------------------------------------------------------------------------------------------------------
# Stack Implementation
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

class Stack:
    """
    Stack (LIFO) implementation using an array.
    Supports push, pop, peek, and is_empty operations.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, value):
        """Push a value onto the stack."""
        self.stack.append(value)

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack underflow")

    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Return the stack representation."""
        return self.stack
