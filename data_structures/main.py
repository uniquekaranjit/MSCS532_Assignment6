# ----------------------------------------------------------------------------------------------------------------------
# Main Driver code to implement LinkedList, Matrices, Queues, Stacks and Array
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

from arrays import Array
from linked_list import SinglyLinkedList
from matrices import Matrix
from queues import Queue
from stacks import Stack


if __name__ == "__main__":
    print("\n---------------------------------------")
    print("Array Implementation")
    print("---------------------------------------")

    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    print("Initial Array of size 5       :", arr.display())
    print("Accessing index 1 of the array:", arr.access(1))
    print("\n***Deleting element at index 1\n")
    arr.delete(1)
    print("Array after Deletion          :", arr.display())

    print("\n---------------------------------------")
    print("Matrix Implementation")
    print("---------------------------------------")
    mat = Matrix(3, 3)
    mat.insert(0, 0, 1)
    mat.insert(1, 1, 5)
    mat.insert(2, 2, 9)
    mat.display()

    print("\n---------------------------------------")
    print("Stack Implementation")
    print("---------------------------------------")
    stack = Stack()  #LIFO
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print("Inserting 3 elements in stack and displaying...")
    print("Stack:", stack.display())
    print("Popping out the elemennt from stack and displaying...")
    print("Popped:", stack.pop())
    print("Stack after pop:", stack.display())

    print("\n---------------------------------------")
    print("Queue Implementation")
    print("---------------------------------------")
    queue = Queue() #FIFO
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print("Inserting 3 elements in queue and displaying...")
    print("Queue:", queue.display())
    print("Dequeing out the elemennt from queue and displaying...")
    print("Dequeued:", queue.dequeue())
    print("Queue after dequeue:", queue.display())

    print("\n---------------------------------------")
    print("Singly Linked List Implementation")
    print("---------------------------------------")
    sll = SinglyLinkedList()
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    print("Inserting 3 elements in LinkedList and displaying...")
    print("Linked List:")
    sll.traverse()
    print("Deleting element at index 2 in LinkedList and displaying...") 
    sll.delete(20)
    print("After Deletion:")
    sll.traverse()
