# Przygotuj funkcję o nazwie word_counter, powinna jako argument
# odbierać dowolny test i zwracać ilość słów z których ten tekst się
# składa.

def word_count(word):
    return len(word)


print(f'Długość słowa to {word_count(input("Podaj słowo"))} liter')