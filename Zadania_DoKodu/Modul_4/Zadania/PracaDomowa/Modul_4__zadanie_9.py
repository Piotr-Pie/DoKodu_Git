# Zadanie 9: Przygotuj program, który będzie szyfrował i odszyfrowywał wyrażenia
# korzystając z szyfru Cezara. Podpowiedź: mogą Ci się przydać funkcję ord() oraz chr().

#Zakodowanie słowa
def encrypt(messaga, key):
    encrypted = ""
    for letter in messaga:
        if ord(letter) + key > ord('z'):
            encrypted += chr(ord(letter) + key - 26)
        else:
            encrypted += chr(ord(letter) + key)
    return encrypted

#Odkodowanie słowa
def dencrypt(messaga, key):
    encrypted = ""
    for letter in messaga:
        if ord(letter) - key < ord('a'):
            encrypted += chr(ord(letter) - key + 26)
        else:
            encrypted += chr(ord(letter) - key)
    return encrypted


print(encrypt("mucha", 3))
print(dencrypt("pxfkd", 3))
