fruits = {'apple': 15, 'banana': 5, 'orange': 12, 'pear': 5,}   #Słownik owocóe
print(fruits)                                                   #Wyświetla słownik owoców
fruits_need = {}                                                #Słownik do którego szukane owoce są kopiowane

for fruit in fruits:                                            #Pętla po słowniku
    if fruit == 'apple' in fruits:                              #Jeżeli znajdziesz dany owoc w słowniku owoców
        fruits_need.update({fruit: fruits[fruit]})              #To aktualizacja nowego słownika
        continue                                                #Kontynuuj tutaj się nie zatrzymuj
    elif fruit == 'banana' in fruits:                           #Jeżeli znajdziesz dany owoc w słowniku owoców
        fruits_need.update({fruit: fruits[fruit]})              #To aktualizacja nowego słownika

print(fruits_need)                                              #Wyświelt wynik wyszukiwanych owoców wraz z cenami.
