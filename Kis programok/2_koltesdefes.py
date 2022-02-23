wr = open('koltes.txt', 'w')
def kivonás(Kedd,Szerda):
    if Szerda > Kedd:
        print('Szerdán ön többet költött!')
    elif Szerda < Kedd:
        print('Kedden többet költött!')
    else:
        print('Ön ugyanannyit költött mind kettő napon!')
        return "Ugyanannyi"
Kedd = int(input('Mennyit költött kedden?'))
print(f'Ennyit költött Kedden: {Kedd}Ft')
wr.write(f'Ennyit költött Szerdán: {Kedd}Ft')

Szerda = int(input('Kérem adja meg mennyit költött szerdán:'))
print(f'Ennyit költött Szerdán: {Szerda}Ft')
wr.write(f'\nEnnyit költött Szerdán: {Szerda}Ft')

összesen = Kedd+Szerda
print(f'Ennyit költött összesen: {összesen}Ft')
wr.write(f'\nEnnyit költött összesen: {összesen}Ft')

print('Ennyi a különbség:')
print(kivonás(Kedd,Szerda))
wr.close
