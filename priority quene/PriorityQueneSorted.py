from Node import Node

class PriorityQueneSorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def print_all(self):
        if self.is_empty():
            print('Priority Queue is empty')
        else:
            current = self._head
            while current is not None:
                print('(''data :', current._data, ',' ,'priority : ', current._priority, ')', end='\n')
                current = current._next
        print()
    
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty() or priority < self._head._priority: 
            baru._next = self._head
            self._head = baru
            if self._tail is None:
                self._tail = baru
        else:
            bantu = self._head
            while bantu._next is not None and bantu._next._priority <= priority:
                bantu = bantu._next
            baru._next = bantu._next
            bantu._next = baru
            if baru._next is None:
                self._tail = baru
        self._size += 1
        
    def remove(self): 
        if self.is_empty():
            return None
        hapus = self._head
        self._head = self._head._next
        if self._head is None: 
            self._tail = None
        self._size -= 1
        return (hapus._data, hapus._priority)
    
    def peek(self):
        if self.is_empty():
            return None
        return (self._head._data, self._head._priority)
