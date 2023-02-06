from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: int = None, next: Node = None, prev: Node = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class double_LinkedList:
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
            self.head = Node(data, None, None)
            self.tail = Node(data, None, None)
            self.current = Node(data, None, None)
        # insert at head
        if data < self.head.data:
            ptr = self.head
            self.head = Node(data, None, ptr)
            self.current = Node(data, None, ptr)
            ptr.prev = self.head
        # insert at tail
        elif data >= self.tail.data:
            ptr = self.tail
            self.tail = Node(data, ptr, None)
            self.current = Node(data, ptr, None)
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
        print(f"delete {data}")
        self.no -= 1
        ptr = self.current
        # delete only one node
        if self.head == self.tail:
            print("delete only one node")
            self.head = self.tail = self.current = None
        # delete head
        elif ptr == self.head:
            print("delete head")
            self.head = self.current = ptr.next
            self.head.prev = None
        # delete tail
        elif ptr == self.tail:
            print("delete tail")
            self.tail = self.current = ptr.prev
            self.tail.next = None
        # delete middle
        else:
            print("delete middle")
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
            self.current = ptr.prev
    
    # search
    def search(self, data: int) -> int:
        if self.is_empty():
            return -1
        ptr = self.head
        # error handling - head = tail
        if self.head == self.tail:
            if self.head.data == data:
                return 1
            else:
                return 0
        # search from head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return 1
            if ptr.next is not None and ptr.next.data < data:
                self.current = ptr
                return 0
            ptr = ptr.next
        if ptr is None:
            self.current = self.tail
        else:
            self.current = ptr.prev
        return 0
    
    # clear
    def clear(self) -> None:
        while not self.is_empty():
            self.delete(self.head.data)
    
    # iterator
    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)
    
class LinkedListIterator:
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next
        
    def __iter__(self) -> LinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data