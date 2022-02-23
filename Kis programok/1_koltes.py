wr = open('koltes.txt', 'w')
Kedd = int(input('Mennyit költött kedden?'))
print(f'Ennyit költött Kedden: {Kedd}Ft')
wr.write(f'Ennyit költött Szerdán: {Kedd}Ft')
Szerda = int(input('Kérem adja meg mennyit költött szerdán:'))
print(f'Ennyit költött Szerdán: {Szerda}Ft')
wr.write(f'\nEnnyit költött Szerdán: {Szerda}Ft')
összesen = Kedd+Szerda
print(f'Ennyit költött összesen: {összesen}Ft')
wr.write(f'\nEnnyit költött összesen: {összesen}Ft')
if Szerda > Kedd:
    print('Szerdán ön többet költött!')
    különbség1 = Szerda - Kedd
    print(f'Ennyi a különbség: {különbség1}Ft')
    wr.write(f'\nEnnyi a különbség: {különbség1}Ft')
elif Szerda < Kedd:
    print('Kedden többet költött!')
    különbség2 = Kedd - Kedd
    print(f'Ennyi a különbség: {különbség2}Ft')
    wr.write(f'\nEnnyi a különbség: {különbség2}Ft')
else:
    print('Ön ugyanannyit költött mind kettő napon!')
    különbség1 = Szerda - Kedd
    print(f'Ennyi a különbség: {különbség1}Ft')
    wr.write(f'\nEnnyi a különbség: {különbség1}Ft')