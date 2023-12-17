import random
from random import randint, shuffle



print(f'****************************************************')
print()
print(f'Zabawimyu się w REBUS, odgadnij o jakie słowo mi chodzi')
print()
print(f'****************************************************')

lista_slow = ['jabłko', 'kot', 'telewizor', 'samochód', 'lampa', 'książka', 'krzesło', 'drzewo', 'dom', 'pizza', 'kwiat', 'ręka', 'buty', 'rower', 'słońce', 'księżyc', 'telefon', 'piłka', 'ryba', 'ser', 'chleb', 'kawa', 'deszcz', 'łóżko', 'dziecko', 'telewizja', 'papuga', 'motocykl', 'kalendarz', 'okno']

komputer = lista_slow[randint(0, len(lista_slow)-1)]
print(komputer)
komputer2 = list(komputer)
komputer_szuflada = random.shuffle(komputer2)

print(f'****************************************************')
print(f'Odgadnij co to za słowo, masz 5 szans')
print(komputer2)
print(f'****************************************************')

proba = 1

for x in range(0, 5):
    szansa = input(f'Podaj słowo jest to twoja {proba} próba: ')
    proba += 1
    if szansa == komputer:
        print(f'Odgadłeś słowo !!')
        quit()
    else:
        print(f'Przykro mi, nie odgadłeś, spróbuj jeszcze raz!')