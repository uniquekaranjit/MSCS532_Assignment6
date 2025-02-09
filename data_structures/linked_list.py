# ----------------------------------------------------------------------------------------------------------------------
# LinkedList Implementation
# Author: Unique Karanjit
# Date: 2025-02-09
# ----------------------------------------------------------------------------------------------------------------------

class Node:
    """
    Node class for a singly linked list.
    Contains a value and a reference to the next node.
    """
    def __init__(self, value):
        """Initialize a node with a given value."""
        self.value = value
        self.next = None

class SinglyLinkedList:
    """
    Singly linked list implementation.
    Supports insertion, deletion, and traversal.
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, value):
        """Insert a new node at the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, value):
        """Delete the first occurrence of a node with the given value."""
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.value != value:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

    def traverse(self):
        """Traverse and print the linked list."""
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
