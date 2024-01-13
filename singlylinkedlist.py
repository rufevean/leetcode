class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtHead(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            node.next = self.head
            self.head = node 
        self.size +=1 
    
    def addAtTail(self,data):
        node = Node(data)
        if not self.tail:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            self.tail = node
        self.size +=1
    def getIndex(self,index):
        if index < 0 or index >= self.size:
            return -1 
        else:
            counter = 0
            current = self.head
            while counter != index:
                current = current.next
                counter +=1
            return current.data
    def addAtIndex(self,data,index):
        if index < 0 or index > self.size:
            return -1
        elif index == 0:
            self.addAtHead(data)
        elif index == self.size:
            self.addAttail(data)
        else:
            node = node(data)
            counter = 0
            current = self.head
            while counter != index-1:
                current = current.next
                counter +=1
            node.next = current.next
            current.next = node
            self.size +=1
    def deleteAtIndex(self,index):
        if index < 0 or index >= self.size:
            return -1
        elif index == 0:
            self.head = self.head.next
            self.size -=1
        else:
            counter = 0
            current = self.head
            while counter != index-1:
                current = current.next
                counter +=1
            current.next = current.next.next
            self.size -=1

