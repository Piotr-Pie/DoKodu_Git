# Przygotuj funkcję, która będzie odbierała od użytkownika słowo,
# a następnie zwróci zbiór samogłosek znajdujących się w tym słowie.


def samogloski(slowo):
    slowo2 = set(slowo)
    volwels = {'a', 'e', 'i', 'o', 'u', 'ą', 'ę'}
    return slowo2 & volwels


print(samogloski('Piotrunia'))
