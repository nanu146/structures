from Structures.CustomExceptions import *


class _Node:
    def __init__(self,data):
        self._data=data
        self._nextNode=None
    
    @property
    def data(self):
        """Returns the value of the Node"""
        return self._data

    @property
    def nextNode(self):
        """returns the next node"""
        return self._nextNode

    @data.setter
    def data(self,value):
        """sets the value of the present Node"""
        self._data = value
    
    @nextNode.setter
    def nextNode(self,node):
        """sets the pointer to the next node"""
        if node == None or isinstance(node,_Node):
            self._nextNode = node
        else:
            raise ValueError("cannot set next to a value of type {}".format(type(node)))
    
    def __str__(self):
        return str(self._data)


class _DoublyLinkedNode(_Node):
    """This class represents a doubly linked Node"""

    def __init__(self,data):
        super().__init__(data)
        self._previousNode=None

    @property
    def previousNode(self):
        """Returns previous node"""
        return self._previousNode
    
    @previousNode.setter
    def previousNode(self,node):
        if node == None or isinstance(node,_DoublyLinkedNode):
            self._previousNode = node
        else:
            raise ValueError("cannot set the value of previous node to value of type {}".format(type(node)))



class LinkedList:
    """Linked list implementation"""
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    

    @classmethod
    def fromList(cls,list):
        listObj = cls()

        for item in list:
            listObj.append(item)
        
        return listObj
    
    
    def insertAtStart(self,data):
        "Inserts node at the begining of the Linked List"
        
        self.size =self.size+1
        newNode = _Node(data)

        if not self.head:
            self.head =  newNode
            self.tail = newNode
            return True
        else:
            newNode.nextNode = self.head
            self.head=newNode
            return True


    def append(self,data):
        "Appends new data as a node at the of the list"
        
        self.size = self.size + 1
        newNode = _Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        else:
            tempTail = self.tail
            tempTail.nextNode = newNode
            self.tail = newNode

    
    def insertAt(self, findData, data):
        "inserts the data at a "
        self.size += 1

        newNode = _Node(data)

        if not self.head:
            return False

        else:
            currentNode = self.head
            previousNode = self.head

            while currentNode.nextNode != None:
                if(currentNode.data != findData ):
                    previousNode = currentNode
                    currentNode = currentNode.nextNode
                else:
                    break
            
            if currentNode == previousNode:
                TempNode = currentNode

                self.head = newNode

                newNode.nextNode =TempNode

                return True
            
            else:
                previousNode.nextNode = newNode
                newNode.nextNode = currentNode
            
    
    def remove(self, findData):


        currentNode, previousNode = self.__findConjNode(findData)

        
        if currentNode == None and previousNode == None:
            return False
        elif currentNode == previousNode and currentNode != previousNode!= None:
            self.head=None
            self.tail=None

            self.size -=1

            return True

        else:
            previousNode.nextNode= currentNode.nextNode
            self.size -= 1
            return True

        

    def __findConjNode(self, findData):

        if not self.head:
            return (None,None)
        
        currentNode = self.head
        previousNode =self.head
        
        while currentNode!= None:
            if(currentNode.data == findData):
                return (currentNode,previousNode)
            else:
                previousNode=currentNode
                currentNode = currentNode.nextNode
        
        return (None,None)
    
   
    def __str__(self):

        strholder =""

        currentNode = self.head

        while currentNode != None:
            strholder +=" "+ str(currentNode.data)
            currentNode = currentNode.nextNode

        return strholder



class DoublyLinkedList:
    "DOubly Linked LIst implementation"

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @classmethod
    def fromList(cls,list):
        listObj = cls()

        for item in list:
            listObj.append(item)
        
        return listObj


    @property
    def head(self):
        "Returns head element"

        return self._head
    

    @property
    def tail(self):
        "Returns tail element"

        return self._tail


    @property
    def size(self):
        "Returns size of the Doubly Linked List"
        
        return self._size
    

    def insertAtStart(self, data):
        "inserts data at the begining of the list"

        newNode = _DoublyLinkedNode(data)
        
        if self._head == None:
            self._size += 1
            self._head = newNode
            self._tail = newNode
            return 
        else:
            tempNode = self._head
            self._head = newNode
            newNode.nextNode = tempNode
            tempNode.previousNode = self._head
            self._size += 1
            return 

        
    def append(self, data):
        "Appends the new node at the end of the List"

        newNode = _DoublyLinkedNode(data)

        if self._size == 0:
            self.insertAtStart(data)
        else:
            tempNode = self._tail
            self._tail = newNode
            self._tail.previousNode = tempNode
            tempNode.nextNode = self._tail
            self._size += 1
            return 

    
    def insertAt(self, data, findData):
        "Find the node with the value present in findData and inserts new node before it with value data"

        newNode = _DoublyLinkedNode(data)

        if self._head.data == findData:
            self.insertAtStart(data)
        else:
            currentNode = self._head
            
            while currentNode != None:
                if currentNode.data == findData:
                    break
                else:
                    currentNode = currentNode.nextNode
            
            if currentNode == None:
                raise ValueNotFound("item {} not found in the list".format(findData))
            else:
                tempNode = currentNode
                currentNode = newNode
                newNode.nextNode = tempNode
                tempNode.previousNode.nextNode = newNode
                tempNode.previousNode = newNode
                self._size += 1
                return 
        
    
    def remove(self,node):
        "removes element by node"
        if isinstance(node,_DoublyLinkedNode):
            
            if node == self._head:
                node.nextNode.previousNode = None
                self._head = node.nextNode
                self._size -= 1
                return
            
            elif node == self._tail:
                node.previousNode.nextNode = None
                self._tail = node.previousNode
                self._size -= 1
            else:
                node.previousNode.nextNode = node.nextNode
                node.nextNode.previousNode = node.previousNode
                self._size -= 1
        else:
            raise ValueError("cannot handle a value of type {}".format(type(node)))


    def find(self, findData):
        "Finds a node by its data, returns node if found or else returns null if node not found"
        
        currentNode = self._head

        while currentNode != None:
                if currentNode.data == findData:
                    break
                else:
                    currentNode = currentNode.nextNode

        return currentNode


    def __str__(self):
        "Returns the string interpretation of DoublyLinkedList Object"

        strHold = ""
        currentNode = self._head

        while  currentNode != None:
            strHold += str(currentNode.data) +" "
            currentNode = currentNode.nextNode
        
        return strHold



