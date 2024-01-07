# Zadanie 10: Napisz program, który będzie usuwał z tekstu wszystkie słowa zaczynające
# się na wybraną literę.

#Podaj dowolny tekst
text = input("Podaj dowolny tekst, a wszystkie słoza zaczynające się na literę [P] zostaną usunięte: ")

#Lsita, która będzie przyjmowała tekst.
coubt = []

#Pętla wpisanego tekstu
for x in text:
    #Sprawdza czy na początku słowa znajduje się duża i mała litera P
    if x.startswith("P") or x.startswith("p"):
        #Zmienia wartość małej i dużej litery P na pusty znak
        x = x.replace("P", "").replace("p", "")
        #Dodaje co coubt słowo z usuniętą pierwszą literą
        coubt.append(x)
    else:
        #Dodaje wszystko do coubt co nie zostało wykryte w if
        coubt.append(x)

#Łączy listę
print("".join(coubt))

