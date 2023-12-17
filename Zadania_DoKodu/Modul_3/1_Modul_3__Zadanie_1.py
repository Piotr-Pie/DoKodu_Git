print()
print(f'Podaj pięć imion twoich znajomych, a ułożę je alfabetycznie!!')
print()
print()

name = []
count = 1

for x in range(0, 5):
    names = input(f'Podaj imię nr {count}: ')
    name.append(names)
    count += 1

print()
print(f'Podałeś pięć imion {name}')
print(f'*********************')
print(name)
print(f'*********************')
name.sort()

print(f'*********************')
print(f'Imiona posortowane alfabetycznie:')
print(name)
print(f'*********************')


