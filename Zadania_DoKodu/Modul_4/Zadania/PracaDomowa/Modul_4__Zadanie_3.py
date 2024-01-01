# Pętla while


# Zadanie 3: Zdefiniuj hasło w zmiennej, a następnie napisz program, który za pomocą pętli
# while będzie pytać użytkownika o wprowadzenie hasła. Jeśli hasło jest poprawne, program
# powinien wyświetlić komunikat "Poprawne hasło", a jeśli hasło jest niepoprawne, program
# powinien wyświetlić komunikat "Niepoprawne hasło, spróbuj ponownie".

password_user = input('Enter your password: ')
print()
while True:
    jour_password = input('Enter your password: ')
    if password_user == jour_password:
        print('Congratulations!')
    else:
        print('Spróbuj jeszcze raz!!')