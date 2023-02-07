from enum import Enum
from pointer_linked_list import LinkedList

Menu = Enum('Menu',
            ['Add_First', 'Add_Last', 'Remove_First',
            'Remove_Last', 'Print_current_node', 'Next',
            'Remove_current_node', 'Clear', 'Search',
            'check', 'Print_all_node', 'Scan',
            'Terminate'])

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
    
    if menu == Menu.Add_First:
        lst.add_first(int(input('Enter the number to add first: ')))
    elif menu == Menu.Add_Last:
        lst.add_last(int(input('Enter the number to add last: ')))
    elif menu == Menu.Remove_First:
        lst.remove_first()
    elif menu == Menu.Remove_Last:
        lst.remove_last()
    elif menu == Menu.Print_current_node:
        lst.print_current_node()
    elif menu == Menu.Next:
        lst.next()
    elif menu == Menu.Remove_current_node:
        lst.remove_current_node()
    elif menu == Menu.Clear:
        lst.clear()
    elif menu == Menu.Search:
        pos = lst.search(int(input('Enter the number to search: ')))
        if pos >= 0:
            print(f'The number is in {pos + 1}th node')
        else:
            print('The number is not in the list')
    elif menu == Menu.check:
        print('The number of nodes is ' + 'included' 
            if int(input('Enter the number to check: ')) in lst 
            else 'not included')
    elif menu == Menu.Print_all_node:
        lst.print_all_node()
    elif menu == Menu.Scan:
        for e in lst:
            print(e)
    else:
        break