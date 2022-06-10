"""
eredmeny1 = int(input("Kérem az eredményt!"))
eredmeny2 = int(input("Kérem a másik eredményt!"))

if eredmeny1 < eredmeny2:
    print(f'A nagyobb érték {eredmeny2}')
elif eredmeny1 > eredmeny2:
    print(f'A nagyobb érték az {eredmeny1}')
else:
    print(f'A két érték egyenlő')
"""    
"""
def aru(suly):
    if suly >= 48:
        return True
    else:
        return False
aru1 = None
#aru1 = "valami"
while aru1 != " ":
    aru1 = input("Add meg a termék nevét!")
    suly = int(input("Add meg a súlyát"))
    if aru(suly) == True:
        print(f"A {aru1} mennyisége rektárrészletben elegendő!")
    else:
        print(f"A {aru1} mennyisége a raktár részletben hiány van!")
"""
"""
if aru(suly):
    print("megvalósult")
else:
    print("nem valósult meg") 
"""
class Hegy:
    def __init__(self, nev, tengerszint, orszag):
        self.nev = nev
        self.tengerszint = tengerszint
        self.orszag = orszag
    
hegyek = []

for _ in range(3):
    hegy_nev = input("Add meg a hegy nevét!")
    tengerszint = int(input("Mennyi a tengerszint feltti magasséga?"))
    orszag = input("Melyik országban található a hegy?")
    hegy1 = Hegy(hegy_nev, tengerszint, orszag)
    hegyek.append(hegy1)

for x in range(3):
    if hegyek[x] > hegyek [x+1]:
        legnagyobb = hegyek[x]
print(f"A legnagyobb hegy a {legnagyobb.nev} , magassága {legnagyobb.tengerszint} méter")

