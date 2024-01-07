# Zadanie 11: Zapytaj użytkownika o dwa wyrażenia, a następnie wyświetl wszystkie znaki
# wspólne dla obu tych wyrażeń. np. sala i balkon: powinno wyświetlić a oraz l



print(f'Podaj dwa dowolne słowa, a wyświetle wspólne litery.')

#Pierwsze słowo
text1 = set(input("Podaj pierwsze słowo: "))

#Drugie słowo
text2 = set(input("Podaj drugie słowo: "))


#Wyświetla tylko te same litery z dwóch słów.
print((text1 & text2))