# Pętla while
# Zadanie 5: Napisz program, który będzie wykonywał pętlę while, która będzie pytać
# użytkownika o nazwę miasta oraz temperaturę w stopniach Celsjusza. Program będzie
# przechowywał te informacje w słowniku, gdzie kluczem będzie nazwa miasta, a wartością
# temperatura. Pętla będzie kontynuowana dopóki użytkownik nie wprowadzi "koniec".
# Po zakończeniu pętli program powinien wyświetlić średnią temperaturę dla wszystkich miast
# oraz nazwę miasta o najwyższej i najniższej temperaturze.

temperatur = {}
print("Podaj Miejscowość oraz temperaturę")
print("Podam Ci średnią temperatury")
print("Podam Ci najniższą temperaturę")
print("Podam Ci najwyższą temperaturę")
print()
print()

while True:
    city = input("Podaj miejscowość: ")
    if city == 'koniec':
        break
    temperatur[city] = float(input("Podaj temperaturę: "))

print(temperatur)
print(f'Średnia temperatura dla wszystkich miast to: {sum(temperatur.values()) / len(temperatur)} C')
misto_z_najwysza_temperatura = max(temperatur, key=temperatur.get)
misto_z_najnizsza_temperatura = min(temperatur, key=temperatur.get)
print(f'Najwyższa temperatura: {misto_z_najwysza_temperatura}')
print(f'Najniższa temperatura: {misto_z_najnizsza_temperatura}')
