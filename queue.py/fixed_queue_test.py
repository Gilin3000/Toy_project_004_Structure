from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', 
        ['enque', 'deque', 'peek', 'find',
        'dump', 'clear', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
q = FixedQueue(64)

while True:
    print(f'The number of data: {len(q)} / {q.capacity}')
    menu = select_menu()
    
    if menu == Menu.enque:
        x = int(input('Enter the number to enque: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('The queue is full')
    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'The number dequeued is {x}')
        except FixedQueue.Empty:
            print('The queue is empty')
    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f'The number at the front is {x}')
        except FixedQueue.Empty:
            print('The queue is empty')
    elif menu == Menu.find:
        x = int(input('Enter the number to find: '))
        if x in q:
            print(f'The number {x} is in the queue, {q.count(x)} times, at {q.find(x)}')
        else:
            print(f'The number {x} is not in the queue')
    elif menu == Menu.dump:
        q.dump()
    elif menu == Menu.clear:
        q.clear()
    else:
        break