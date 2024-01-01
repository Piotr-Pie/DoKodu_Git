# Zadanie 4: Napisz program symulujący działanie bankomatu. Pętla while będzie pytać
# użytkownika o wybór operacji (np. wpłata, wypłata, sprawdzenie stanu konta) i będzie
# kontynuowana dopóki użytkownik nie wybierze opcji "wyjście".

print(f'************************************')
print(f'*           MENU Bankomatu         *')
print(f'************************************')
print(f'* 1 - Stan Konta                   *')
print(f'* 2 - Wpłata                       *')
print(f'* 3 - Wypłata                      *')
print(f'*                                  *')
print(f'* 5 - Wyjście                      *')
print(f'************************************')

stan_konta = 2000

while True:
    choise = int(input(f'Wybierz opecajcę'))
    if choise == 1:
        print(f'Konta: {stan_konta} zł')
    elif choise == 2:
        wplata = int(input('Ile chcesz wpłacić pieniędzy?: '))
        stan_konta += wplata
        print(f'Po operacji twój stan konta: {stan_konta} zł')
    elif choise == 3:
        wyplata = int(input('Ile chcesz pobrać gotówki?: '))
        stan_konta -= wyplata
        print(f'Po operacji stan konta {stan_konta} zł')
    elif choise == 5:
        print(f'Dziękujjemy za wybranie naszego bankomatu')
        print(f'Stan Konta: {stan_konta} zł')
