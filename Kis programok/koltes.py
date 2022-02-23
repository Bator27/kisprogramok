wr = open('koltes.txt', 'w')
Kedd = int(input('Mennyit költött kedden?'))
print(f'Ennyit költött Kedden: {Kedd}')
wr.write(f'Ennyit költött Szerdán: {Kedd}')
Szerda = int(input('Kérem adja meg mennyit költött szerdán'))
print(f'Ennyit költött Szerdán: {Szerda}')
wr.write(f'\nEnnyit költött Szerdán: {Szerda}')
összesen = Kedd+Szerda
print(f'Ennyit költött összesen: {összesen}')
wr.write(f'\nEnnyit költött összesen: {összesen}')
if Szerda > Kedd:
    print('Szerdán ön többet költött!')
    különbség1 = Szerda - Kedd
    print(f'Ennyi a különbség: {különbség1}')
    wr.write(f'\nEnnyi a különbség: {különbség1}')
elif Szerda < Kedd:
    print('Kedden többet költött!')
    különbség2 = Kedd - Kedd
    print(f'Ennyi a különbség: {különbség2}')
    wr.write(f'\nEnnyi a különbség: {különbség2}')
else:
    print('Ön ugyanannyit költött mind kettő napon!')
    különbség1 = Szerda - Kedd
    print(f'Ennyi a különbség: {különbség1}')
    wr.write(f'\nEnnyi a különbség: {különbség1}')