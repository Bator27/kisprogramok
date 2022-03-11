#nev = input('Mi a neve?')
#pontszam = int(input('Mennyi pontot ért el?'))
#2-es nehézség
"""
def sikeres():
    if pontszam >= 48:
        return"Vizsgája sikeres"
    elif pontszam == 48:
        return"Szerencséje van átment!"
    else:
        return"Vizsgája sikertelen!"
nev = None
while nev != "":
    nev = input('Mi a neve?')
    if nev:
        pontszam = int(input('Mennyi pontot ért el?'))
        if sikeres():
            print(nev, 'Vizsgája sikeres!')
        else:
            print(nev, 'vizsgája sikertelen!')
"""
#1-es nehézség
"""
if pontszam >= 48:
    print("Vizsgája sikeres!")
elif pontszam == 48:
    print("Szerencséje van éppen átment!")
else:
    print('Vizsgéja sikertelen!')
"""
#3-as nehézség
class Vizsgazo():
    def __init__(self, nev,pont): #Konstruktor
        self.nev = input("Adja meg a nevet")
        self.pont = int(input("Adja meg a pontszámot"))
    def sikeres(self):
        if self.pont >= 48:
            return True
        else:
            return False

diak = Vizsgazo() #példány
print(diak.sikeres)
