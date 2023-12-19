miesiac = input(f'Podaj miesiąc w liczbie całkowitej: ')

miesiac = int(miesiac)

match miesiac:
    case 1:
        print(f'{miesiac} to miesiąc Stycznień')
    case 2:
        print(f'{miesiac} to miesiąc Luty')
    case 3:
        print(f'{miesiac} to miesiąc Marzec')
    case 4:
        print(f'{miesiac} to miesiąc Kwiecień')
    case 5:
        print(f'{miesiac} to miesiąc Maj')
    case 6:
        print(f'{miesiac} to miesiąc Czerwiec')
    case 7:
        print(f'{miesiac} to miesiąc Lipiec')
    case 8:
        print(f'{miesiac} to miesiąc Sierpień')
    case 9:
        print(f'{miesiac} to miesiąc Wrzesień')
    case 10:
        print(f'{miesiac} to miesiąc Październik')
    case 11:
        print(f'{miesiac} to miesiąc Listopad')
    case 12:
        print(f'{miesiac} to miesiąc Grudzień')
    case _:
        print(f'Nie ma takiego miesiąca!')

print()
print()
print('Słownik')
miesiac_slownik = {1: 'Styczeń',
                   2: 'Luty',
                   3: 'Marzec',
                   4: 'Kwiecień',
                   5: 'Maj',
                   6: 'Czerwiec',
                   7: 'Lipiec',
                   8: 'Sierpień',
                   9: 'Wrzesień',
                   10: 'Październik',
                   11: 'Listopad'
                   }
print(f'{miesiac} to miesiąc {miesiac_slownik[miesiac]}')
