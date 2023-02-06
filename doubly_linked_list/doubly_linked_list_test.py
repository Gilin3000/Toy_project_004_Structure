from enum import Enum
from doubly_linked_list import LinkedList

Menu = Enum('Menu',
            ['len', 'check', 'insert', 'delete',
            'search', 'clear', 'scan', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
lst = LinkedList()

while True:
    menu = select_menu()
    
    if menu == Menu.len:
        print(f'The number of nodes is {len(lst)}')
    elif menu == Menu.check:
        print('The list is ' + ('not ' if not lst.is_empty() else '') + 'empty')
    elif menu == Menu.insert:
        lst.insert(int(input('Enter the number to insert: ')))
    elif menu == Menu.delete:
        lst.delete(int(input('Enter the number to delete: ')))
    elif menu == Menu.search:
        cases = lst.search(int(input('Enter the number to search: ')))
        if cases == 1:
            print('The number is in the list')
        elif cases == 0:
            print('The number is not in the list')
        else:
            print('The list is empty')
    elif menu == Menu.clear:
        lst.clear()
    elif menu == Menu.scan:
        lst.scan()
    else:
        break
    