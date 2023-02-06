from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: Any = None, next: Node = None, prev: Node = None):
        self.data = data
        self.next = next
        self.prev = prev
        
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
    
    # delete
    
    # search
    
    # print
    
    # iterator