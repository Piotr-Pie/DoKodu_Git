# Zadanie 8: Sklep
# Przygotuj słownik zawierający produkty. Produkt to klucz, a cena to wartość. Zapytaj
# użytkownika który produkt chce dodać do koszyka, a następnie w jakiej ilości. Pytaj
# dopóki użytkownik nie odpowie “podsumuj”.
# Wartość zamówienia możesz przechowywać w pojedynczej zmiennej lub posiadać listę
# (dla chętnych) produktów lub słowników jeśli chcesz wyświetlić podsumowanie.


# Tworzenie listy produktów

produkty = [{
    'Banan': 5,
    'Ilosc': 0,
},

    {
        'Jablko': 2,
        'Ilosc': 0,
    },
    {
        'Pomarancz': 4,
        'Ilosc': 0,
    }

]

#Lista z podsumowaniem zakupów
podsumowanie =[]

#Asortyment
print(f'Asortyment: \n'
      f'- Banan \n'
      f'- Jablko \n'
      f'- Pomarancz')

#Pętla gdzie użytkownik wybiera asortyment oraz ilość.
while True:
    wybor_produktu = input('Podaj jaki produkt chcesz dodać do koszyka? (wpisując podsumuj) zatrzymasz program i '
                           'dostaniesz cenę: ')
    if wybor_produktu.lower() == 'podsumuj':
        break
    elif wybor_produktu.lower() == 'banan':
        print(f'Cena za sztukę: {produkty[0]['Banan']} zł')
        ilość = int(input('Podaj ilość: '))
        produkty[0]['Ilosc'] += ilość
        podsumowanie.append(produkty[0]['Banan'] * produkty[0]['Ilosc'])
    elif wybor_produktu.lower() == 'jablko':
        print(f'Cena za sztukę: {produkty[1]['Jablko']} zł')
        ilość = int(input('Podaj ilość: '))
        produkty[1]['Ilosc'] += ilość
        podsumowanie.append(produkty[1]['Jablko'] * produkty[1]['Ilosc'])
    elif wybor_produktu.lower() == 'pomarancz':
        print(f'Cena za sztukę: {produkty[2]['Pomarancz']} zł')
        ilość = int(input('Podaj ilość: '))
        produkty[2]['Ilosc'] += ilość
        podsumowanie.append(produkty[2]['Pomarancz'] * produkty[2]['Ilosc'])

#Podsumowanie zakupów.
print(f'Suma zakupów: {sum(podsumowanie)} zł')