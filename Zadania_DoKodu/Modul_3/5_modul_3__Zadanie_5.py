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

names = []
number = []
for x in animals:
    if x['Name'] not in names:
        names.append(x['Name'])

name_legs = [len(name) for name in names]
max_leg = max(name_legs)

longest_names = [name for name in names if len(name) == max_leg]
print(longest_names)

for x in animals:
    if x['Name'] == longest_names[0]:
        print(x['Name'], x['Rasa'])