# Zadanie 6: Pytaj użytkownika o imion dopóki nie napisze “koniec” program powinien
# wyświetlić słownik prezentujący imiona wraz z ilością ich wystąpień oraz unikatową listę imion
# posortowanych alfabetycznie.
#

#Tworzenie listy z imionami
imiona = []
print(f'Wprowadź imiona (aby zakończyć wprwoadzanie wpisz słowo "koniec"')

while True:
    imie = input('Podaj imię: ')
    if imie.lower() == 'koniec': break
    imiona.append(imie)

print(f'Lista wprowadzonych imion:')
print(imiona)

#Zliczenie ilości imion
ilosc_imion = {}
for i in imiona:
    if i in ilosc_imion:
        ilosc_imion[i] += 1
    else:
        ilosc_imion[i] = 1
print(ilosc_imion)

#Imiona posortowane
print(f'Imiona posortowane alfabetycznie')
print(sorted(ilosc_imion))