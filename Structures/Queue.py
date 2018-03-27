from Structures.Lists import DoublyLinkedList
from Structures.CustomExceptions import QueueUnderFlow

class Queue:
    "implementation of Queue Data structure"

    def __init__(self):
        self.__queueHold = DoublyLinkedList()
        self.__size = None
        self.__firstElement = None
    
    @property
    def size(self):
        "Gets the size of the queue"
        return self.__queueHold.size
    
    @property
    def firstElement(self):
        "Returns the first element which is ready to be de-queued"
        return self.__queueHold.head.data
    
    def enqueue(self,value):
        "Inserts new element into the Queue"
        self.__queueHold.append(value)
    
    def dequeue(self):
        "Remove first element from the queue"
        head = self.__queueHold.head
        if head != None:
            self.__queueHold.remove(head)
            return head.data
        else:
            raise QueueUnderFlow("There are no elements to dequeue")
