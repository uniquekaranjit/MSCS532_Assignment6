class Array:
    """
    A simple implementation of a fixed-size array.
    Supports insertion, deletion, and access operations.
    """
    def __init__(self, size):
        """Initialize an empty array with a fixed size."""
        self.array = [None] * size
        self.size = size

    def insert(self, index, value):
        """Insert a value at a specified index."""
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def delete(self, index):
        """Delete a value at a specified index by setting it to None."""
        if 0 <= index < self.size:
            self.array[index] = None
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        """Retrieve the value at a specified index."""
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        """Return the array representation."""
        return self.array
