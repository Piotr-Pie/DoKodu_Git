# Pętla while
# Zadanie 7: Napisz program, który będzie wykonywał pętlę while, która będzie pytała
# użytkownika o wprowadzenie liczby. Program będzie sprawdzał czy liczba jest parzysta i jeśli
# tak, to będzie ją dodawał do listy liczb parzystych, a jeśli nie, to do listy liczb nieparzystych.
# Pętla będzie kontynuowana dopóki użytkownik nie wprowadzi liczby 0. Po zakończeniu pętli
# program powinien wyświetlić liczbę liczb parzystych i nieparzystych oraz listy liczb parzystych
# i nieparzystych.
#


parzyste = []
nieparzyste = []

while True:
    number = int(input('Wprowadz dowolną cyfrę: '))
    if number == 0:
        break
    elif number % 2 == 0:
        parzyste.append(number)
    elif number % 2 != 0:
        nieparzyste.append(number)

print(f'Liczby Parzyste')
print(parzyste)
print()
print(f'Liczby nieparzyste')
print(nieparzyste)

