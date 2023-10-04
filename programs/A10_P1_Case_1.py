class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self, *args):
        self._first=None
        self._last=None
        self._count=0
        self.append(*args)
        

    def append(self, *args):
        for value in args:
            self._append(value)


    def _append(self, value):
        node=Node(value,previous=self._first)
        if not self._first:
            self._first=node
        else:
            self._last._next=node
        self._last=node
        self._count+=1
                  
                  
    #def info(self):
    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    #def size(self):
    def __len__(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

        

    def __locate(self,index):
        if index>=len(self):
            raise IndexError(f'Invalid Index :{index}')
        
        n=self._first
        for i in range(index):
            n=n._next
            
        return n


             
    #def get(self,index):
    def __getitem__(self,index):
        n=self.__locate(index)
        return n._value  #if n else None
    

    #def set(self,index,value):
    def __setitem__(self,index,value):
        n=self.__locate(index)
        n._value=value

    def insert(self, index, value):
        y=self.__locate(index)
        x=y._previous 

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            self._first=new_node

        y._previous=new_node
        self._count+=1

    def remove(self, index):
        n=self.__locate(index)
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            self._first=y

        if y:
            y._previous=x
                  
        self._count-=1
        return n._value
    
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    

                  
    def __iter__(self):
        return LinkedList.Prime(self._first)
    
    class Prime:
        def __init__(self, current):
            self.current = list._first
            self.previous = list._first

        def __iter__(self):
            return self

        def __next__(self):
            while self.current._next:
                data = self.current._value
                self.previous = self.current          
                self.current = self.current._next      
                self.data = self.current._value
                if(LinkedList.is_prime(data)):
                    return data
            raise StopIteration
    

        

list = LinkedList()
for x in range(10, 20):
        list.append(x)

print(list.info())
print('Adding elements to list')
list.insert(1, 12)
list.insert(2, 17)
list.insert(0, 11)
print(list.info())



prime_iterator = iter(list)
for prime in prime_iterator:
    print(prime, end = '\t')



        


