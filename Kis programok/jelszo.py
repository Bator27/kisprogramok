import random
bejutott = False

while not bejutott:
    felhasznalonev = input("kérem adja meg a felhasználónevét")
    jelszo=input("Kérem adja meg a jelszavat!")

if felhasznalonev == "teknos99" and jelszo == "Tokmag<3":
    print('Belépés engedélyezve')
    bejutott
else:
    print('Belépés tiltva')
def nevelo(szo, maganhangzok):
    maganhangzok = 'aáeéiíoóöőuúüű'
    if szo[0].lower() in maganhangzok:
        return 'az'
    else: 
        return 'a'

def jelzo():
    return random.choice(['piros', 'nagy', 'konnyed'])

#3 főnév - felhaszn
#nevelo vizsgálat -a, az
#nagybetűs ki írás

print('Adj meg egy 3 főnevet!')
for szám in range(1,4):
    fonev = input(str(szam) + 'főnév' )
    print(f'{nevelo(fonev).capitalize()},{fonev} {jelszo()} sep=" "')

class Henger:
    def __init__(self,sugar,kozeppont = (0,0), magassag = 10):
        self.kozeppont = kozeppont
        self.sugar = sugar
        self.magassag = magassag
    def terulet (self):
        return self.sugar*pow
    def felszin(self):
        pass
    def terfogat(self):
        pass

hanger_01 = Henger()