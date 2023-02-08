from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['add', 'remove', 'search', 'dump', 'exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
hash = ChainedHash(13)

while True:
    menu = select_menu()
    
    if menu == Menu.add:
        key = int(input('input key: '))
        val = int(input('input value: '))
        if not hash.add(key, val):
            print('add failed')
    elif menu == Menu.remove:
        key = int(input('input key: '))
        if not hash.remove(key):
            print('remove failed')
    elif menu == Menu.search:
        key = int(input('input key: '))
        t = hash.search(key)
        if t is not None:
            print(f'key: {key} value: {t}')
        else:
            print('search failed')
    elif menu == Menu.dump:
        hash.dump()
    else:
        break