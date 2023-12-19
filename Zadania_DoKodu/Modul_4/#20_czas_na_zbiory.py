# W grze komputerowej gracz może zdobywać różne przedmioty,
# które są przechowywane w zbiorze. Napisz funkcję, która sprawdzi,
# czy gracz posiada określony przedmiot. Co stanie się, gdy drugi raz
# dodasz ten sam produkt?


from random import choice

items = ['latarka', 'konewka', 'miecz', 'helm', 'rekawice', 'buty']
player_items = set()

for _ in range(20):
    item = choice(items)
    print(f'Znalazłem item {item}')
    if item in player_items:
        print(f'Ten przedmiot już znalazłem !!!')
    player_items.add(item)

print(player_items)


# Odbierz od użytkownika 10 adresów email. Sprawdź, czy adres
# zawiera @ oraz .com lub .pl, jeśli tak to dodaj adres do listy
# Na koniec zamień listę na zbiór aby usunąć wszystkie duplikaty.
# Wyświetl ilość wpisów przed usunięciem duplikatów oraz po

mail_box =[]
ilosc = 1

for x in range(3):
    mail = input(f"Podaj {ilosc} adres mailowy: ")
    if "@" in mail and (".pl" in mail or ".com" in mail):
        mail_box.append(mail)
    ilosc += 1

mail_box = set(mail_box)

print(mail_box)