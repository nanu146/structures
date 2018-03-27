from Structures.Lists import DoublyLinkedList
from Structures.CustomExceptions import StackUnderFlow
    

class Stack:
    "Stack data structure"

    def __init__(self):
        self.__top = None
        self.__stackHolder = DoublyLinkedList()
        self.__size = None

    
    @property
    def top(self):
        "Getter for top property"
        return self.__stackHolder.tail.data

    
    @property
    def size(self):
        "Gets the size or depth of the stack"
        return self.__stackHolder.size

    
    def push(self,value):
        "push operation inserts new element into the stack"
        self.__stackHolder.append(value)


    def pop(self,value):
        "Pops the top element of the stack"
        if(self.size >0):
            tail = self.__stackHolder.tail
            self.__stackHolder.remove(tail)
            return tail.data
        else:
            raise StackUnderFlow("There are no elements in the stack to pop")
    


    
