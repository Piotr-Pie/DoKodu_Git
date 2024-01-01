# Zadanie 1: Napisz program, który będzie wykonywał różne operacje matematyczne
# w zależności od wyboru użytkownika. Użytkownik powinien mieć możliwość wyboru
# między dodawaniem, odejmowaniem, mnożeniem i dzieleniem.

print(f'************************************')
print(f'*           MENU                   *')
print(f'************************************')
print(f'* 1 - Dodawanie                    *')
print(f'* 2 - Odejmowanie                  *')
print(f'* 3 - Mnożenie                     *')
print(f'* 4 - Dzielenie                    *')
print(f'*                                  *')
print(f'* 5 - Wyjście                      *')
print(f'************************************')


while True:
    choice = int(input('Wprowadź nr działania: '))
    if choice == 5:
        quit()
    numbers_1 = int(input('Podaj pierwszą liczbę: '))
    numbers_2 = int(input('Podaj drugą liczbę: '))
    if choice == 1:
        print(f'Wynik z dodawania = {numbers_1 + numbers_2}')
    elif choice == 2:
        print(f'Wynik z odejmowania = {numbers_1 - numbers_2}')
    elif choice == 3:
        print(f'Wynik z mnożenia = {numbers_1 * numbers_2}')
    elif choice == 4:
        print(f'Wynik z dzielenia = {numbers_1 / numbers_2}')



print(f'Wybrałęś zły nr, menu jest od 1 - 4')