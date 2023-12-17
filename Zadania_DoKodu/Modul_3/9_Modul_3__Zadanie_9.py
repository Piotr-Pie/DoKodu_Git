from random import random, choice

talia = {
    'As': ['pik', 'kier', 'trefl', 'karo'],
    'Król': ['pik', 'kier', 'trefl', 'karo'],
    'Dama': ['pik', 'kier', 'trefl', 'karo'],
    'Jeździec': ['pik', 'kier', 'trefl', 'karo'],
    'Walet': ['pik', 'kier', 'trefl', 'karo'],
    'Dziesiątka': ['pik', 'kier', 'trefl', 'karo'],
    'Dziewiątka': ['pik', 'kier', 'trefl', 'karo'],
    'Ósemka': ['pik', 'kier', 'trefl', 'karo'],
    'Siudemka': ['pik', 'kier', 'trefl', 'karo'],
    'Szustka': ['pik', 'kier', 'trefl', 'karo'],
    'Piątka': ['pik', 'kier', 'trefl', 'karo'],
    'Czwórka': ['pik', 'kier', 'trefl', 'karo'],
    'Trójka': ['pik', 'kier', 'trefl', 'karo'],
    'Dwójka': ['pik', 'kier', 'trefl', 'karo'],
}

karta = []

for x in talia:
    if x not in karta:
        karta.append(x)

karta_random = choice(karta)
karta_kolor = talia[choice(karta)]

print(f'Karta: {karta_random}, Kolor: {choice(karta_kolor)}')