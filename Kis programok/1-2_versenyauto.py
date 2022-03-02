def autotipuska(autotipus):
    if autotipus[0] == "A" or autotipus[0] == "B":
        return("Német autó")
    else:
        return("Ismeretlen")
def gyartottak(gyartasiev):
    if gyartasiev > 2001:
        return("XXI. század")
    elif gyartasiev < 2000:
        return("XX. század")
    elif gyartasiev == 2022:
        return("Napjaink autója")
def seb(vegseb):
    if vegseb < 130:
        return("Az 9n autója lassú.")
    elif vegseb > 130 < 230:
        return("Maga autója átlagos.")
    else:
        return("Maga autója gyors!")


autotipus = input("Kérem adja meg az autótípusát!")
gyartasiev = int(input("Kérem adja meg a kocsija gyárási évét!"))
vegseb = int(input("Kérem adja meg kocsija végsebességét!"))
print(autotipuska(autotipus))
print(gyartottak(gyartasiev))
print(seb(vegseb))