# ----------------------------------------------------------------------------------------------------------------------
# Queue Implementation
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

class Queue:
    """
    Queue (FIFO) implementation using an array.
    Supports enqueue, dequeue, peek, and is_empty operations.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, value):
        """Add a value to the end of the queue."""
        self.queue.append(value)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Queue underflow")

    def peek(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Return the queue representation."""
        return self.queue
