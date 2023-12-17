#Słownik zwierząt
animals = [
    {
    'ID': 1,
    'Name': 'Luna',
    'Rasa': 'Pies',
    'Ilosc_nog': 4
},

    {
    'ID': 2,
    'Name': 'Kryska',
    'Rasa': 'Agama Brodata',
    'Ilosc_nog': 4
},

    {
    'ID': 3,
    'Name': 'Barbara',
    'Rasa': 'Pajak',
    'Ilosc_nog': 8
},

    {
    'ID': 4,
    'Name': 'Monika',
    'Rasa': 'Zona',
    'Ilosc_nog': 2
},

]
print(animals)

#Znalezienie zwierzęta, który ma najwięcej nóg
max_legs = max(animal['Ilosc_nog'] for animal in animals)

#Pusta lista
animal_max_legs = []
print(max_legs)

#Pętla wyszukująca zwiezięcia z największą ilością nóg.
for animal in animals:
    if animal['Ilosc_nog'] == max_legs:
        animal_max_legs.append(animal)  #Dodaje do listy zwierze

print(animal_max_legs)