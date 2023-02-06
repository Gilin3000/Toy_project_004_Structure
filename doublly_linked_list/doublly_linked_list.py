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
    
    # print
    
    # iterator