
#Utworzyliśmy Słownik ulubionych filmow
Films = [{
    'id': 1,
    'title': 'SKAZANI NA SHAWSHANK',
    'rezyser': 'Frank Darabont',
    'years': 1994
},
    {
        'id': 2,
        'title': 'NIETYKALNI',
        'rezyser': 'Olivier Nakachet',
        'years': 2011
    },

    {
        'id': 3,
        'title': 'POJEDYNEK NA SZOSIE',
        'rezyser': 'Steven Spielberg',
        'years': 1971
    }

]

#Wyświetliliśmy listę
print(Films)

#Pusta lista, gdzie będą wrzucone znalezione elementy
films_to_remove = []

#Petla wyszukujca dany element ze slownika Films
for film in Films:
    if film['rezyser'] == 'Steven Spielberg':
        films_to_remove.append(film)            #Dodajemy do listy znaleziony film

#Kolejna petla, aby w slowniku Films usunac znaleziony film
for film in films_to_remove:
    Films.remove(film)

#Wyswietlilismy cały słownik, ale bez znalezionego filmu, który miał został usunięty.
print(Films)



