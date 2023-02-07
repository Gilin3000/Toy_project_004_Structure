from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: int = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self
        
class circular_LinkedList:
    def __init__(self) -> None:
        self.head = self.current = Node()
        self.no = 0
                
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def search(self, data: int) -> int:
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: int) -> bool:
        return self.search(data) >= 0
    
    def print_current_node(self) -> None:
        if self.is_empty():
            print('The list is empty')
        else:
            print(self.current.data)
    
    def print(self, forward: bool = True) -> None:
        if self.is_empty():
            print('The list is empty')
        else:
            ptr = self.head.next if forward else self.head.prev
            while ptr is not self.head:
                print(ptr.data)
                ptr = ptr.next if forward else ptr.prev
    
    def print_reverse(self) -> None:
        self.print(False)
    
    def next(self) -> bool:
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True
    
    def prev(self) -> bool:
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True
    
    def add(self, data: int) -> None:
        newNode = Node(data, self.current, self.current.next)
        self.current.next.prev = newNode
        self.current.next = newNode
        self.current = newNode
        self.no += 1
    
    def add_first(self, data: int) -> None:
        self.current = self.head
        self.add(data)
    
    def add_last(self, data: int) -> None:
        self.current = self.head.prev
        self.add(data)
        
    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next
    
    def remove(self, p: Node) -> None:
        ptr = self.head.next
        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next
    
    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()
    
    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()
    
    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0
    
    def __iter__(self) -> circular_LinkedListIterator:
        return circular_LinkedListIterator(self.head)
    
    def __reversed__(self) -> circular_LinkedListReverseIterator:
        return circular_LinkedListReverseIterator(self.head)
    
class circular_LinkedListIterator:
    def __init__(self, head: Node) -> None:
        self.head = head
        self.current = head.next
    
    def __iter__(self) -> circular_LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
    
class circular_LinkedListReverseIterator:
    def __init__(self, head: Node) -> None:
        self.head = head
        self.current = head.prev
    
    def __iter__(self) -> circular_LinkedListReverseIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
        
