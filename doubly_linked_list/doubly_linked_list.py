from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: int = None, next: Node = None, prev: Node = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.tail = None
        self.current = None
        
    def __len__(self) -> int:
        return self.no
    
    # check
    def is_empty(self) -> bool:
        return self.no <= 0
    
    # insert
    def insert(self, data : int) -> None:
        cases = self.search(data)
        self.no += 1
        if cases == -1:
            self.head = self.tail = self.current = Node(data, None, None)
        else:
            # insert at head
            if self.current == self.head:
                ptr = self.head
                self.head = self.current = Node(data, None, ptr)
                ptr.prev = self.head
            # insert at tail
            elif self.current == self.tail:
                ptr = self.tail
                self.tail = self.current = Node(data, ptr, None)
                ptr.next = self.tail
            # insert at middle
            else:
                ptr = self.current
                self.current = Node(data, ptr, ptr.next)
                ptr.next.prev = self.current
                ptr.next = self.current
    
    # delete
    def delete(self, data: int) -> None:
        cases = self.search(data)
        if cases != 1:
            return
        self.no -= 1
        ptr = self.current
        # delete only one node
        if self.head == self.tail:
            self.head = self.tail = self.current = None
        # delete head
        elif ptr == self.head:
            self.head = self.current = ptr.next
            self.head.prev = None
        # delete tail
        elif ptr == self.tail:
            self.tail = self.current = ptr.prev
            self.tail.next = None
        # delete middle
        else:
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
            self.current = ptr.prev
    
    # search
    def search(self, data: int) -> int:
        if self.is_empty():
            return -1
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return 1
            if ptr.next is not None and ptr.next.data < data:
                self.current = ptr
                return 0
            ptr = ptr.next
        self.current = ptr.prev
        return 0
    
    # clear
    def clear(self) -> None:
        while not self.is_empty():
            self.delete(self.head.data)

    # print
    def print(self) -> None:
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = ' ')
            ptr = ptr.next
        print()
    
    # iterator
    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)
    
class LinkedListIterator:
    def __init__(self, head: Node):
        self.current = head
        
    def __iter__(self) -> LinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data