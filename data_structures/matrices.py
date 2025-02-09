# ----------------------------------------------------------------------------------------------------------------------
# Matrix Implementation
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

class Matrix:
    """
    A simple implementation of a 2D matrix.
    Supports insertion, access, and display operations.
    """
    def __init__(self, rows, cols):
        """Initialize an empty matrix with given dimensions."""
        self.matrix = [[None] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def insert(self, row, col, value):
        """Insert a value at a specified row and column."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def access(self, row, col):
        """Retrieve the value at a specified row and column."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        """Print the matrix in a readable format."""
        for row in self.matrix:
            print(row)
