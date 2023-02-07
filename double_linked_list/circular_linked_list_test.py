from enum import Enum
from circular_linked_list import circular_LinkedList

Menu = Enum('Menu',
            ['len', 'add_first', 'add_last', 'add_current',
            'remove_first', 'remove_last', 'remove_current',
            'next', 'prev', 'print_current', 'clear',
            'search', 'check', 'scan', 'scan_reverse', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
lst = circular_LinkedList()

while True:
    menu = select_menu()
    
    if menu == Menu.len:
        print(f'The number of nodes is {len(lst)}')
    elif menu == Menu.add_first:
        lst.add_first(int(input('Enter the number to add first: ')))
    elif menu == Menu.add_last:
        lst.add_last(int(input('Enter the number to add last: ')))
    elif menu == Menu.add_current:
        lst.add(int(input('Enter the number to add current: ')))
    elif menu == Menu.remove_first:
        lst.remove_first()
    elif menu == Menu.remove_last:
        lst.remove_last()
    elif menu == Menu.remove_current:
        lst.remove_current_node()
    elif menu == Menu.next:
        lst.next()
    elif menu == Menu.prev:
        lst.prev()
    elif menu == Menu.print_current:
        lst.print_current_node()
    elif menu == Menu.clear:
        lst.clear()
    elif menu == Menu.search:
        pos = lst.search(int(input('Enter the number to search: ')))
        if pos >= 0:
            print(f'The number is in {pos + 1}th node')
        else:
            print('The number is not in the list')
    elif menu == Menu.check:
        print('The number of nodes is ' + 'included' 
            if int(input('Enter the number to check: ')) in lst 
            else 'not included')
    elif menu == Menu.scan:
        for e in lst:
            print(e)
    elif menu == Menu.scan_reverse:
        for e in reversed(lst):
            print(e)
    