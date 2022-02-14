nev = None

def siker(pontszám):
    if pontszám >=48:
        return True
    else:
        return False

#siker = False
while nev != "":
    nev = input("Kérem adja meg a nevét!")
    if nev:
        pontszam = int(input("Adja meg a pontot!"))
        if siker(pontszam):
            print(f"{nev} vizsgája sikeres")
            break
        else:
            print(f"{nev} vizsgája sikertelen")