# Zadanie 2: Napisz program, który będzie konwertował różne jednostki masy na
# podstawie wyboru użytkownika. Użytkownik powinien mieć możliwość konwersji
# między kilogramami, funtami i uncjami.
# Przelicznik jest 1 kilogram = 35.274 uncji oraz 1 kilogram = 2.20462 funtów


print(f'************************************')
print(f'*           MENU                   *')
print(f'************************************')
print(f'* 1 - kg / funty                   *')
print(f'* 2 - funty / kg                   *')
print(f'*                                  *')
print(f'* 5 - Wyjście                      *')
print(f'************************************')

while True:
    choice = int(input('Jaki chycesz przelicznik?: '))
    if choice == 5:
        quit()
    # elif choice ! 1 or choice != 2:
    #     print(f'Nie ma takiej opcji')
    #     continue
    if choice == 1:
        kg = float(input('Podaj kg: '))
        print(f'podałeś {kg} kg, przeliczając na funty to wychodzi {kg * 2.20462:.2f} funty')

    elif choice == 2:
        funty = float(input('Podaj funty: '))
        print(f'podałeś {funty}, przeliczając na funty to wychodzi {funty / 2.20462:.2f} kg')
