class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None and self.tail==None:
            self.head = new_node

        elif self.head == self.tail:
            self.head.next = new_node

        else:
            self.tail.next = new_node

        self.tail = new_node
        self.len += 1
        
    def info(self):
        if self.head == None:
            return "LinkedList(empty)"
        str = "LinkedList(\t"
        node = self.head
        while node:
            str+= f'{node.data}\t'
            node = node.next
        str+= ")"
        return str
    
    def size(self):
        node = self.head
        count = 0
        while node:
            node= node.next
            count+=1
        return count 
        
    
    def __locate(self, index):
        if index> self.size():
            return None
        
        node = self.head
        for i in range(index):
            node = node.next

        return node
    
    def get(self, index):
        node = self.__locate(index)
        return node.data if node else None
    
    def set(self, index, data):
        node = self.__locate(index)
        if node:
            node.data = data

    def insert(self, index, data):
        y = self.__locate(index)
        if not y:
            return 
        x = y.previous

        new_node = Node(data)
        new_node.previous = x
        new_node.next = y

        if x:
            x.next = new_node
        else:
            self.head = new_node

        y.previous = new_node

    def remove(self, index):
        node = self.__locate(index)
        if not node:
            return
        
        x = node.previous
        y = node.next

        if x:
            x.next = y
        else:
            self.head = y
        
        if y:
            y.previous = x
        return node.data
    


    