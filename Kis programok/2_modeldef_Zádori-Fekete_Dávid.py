def model(modelnev, hanyeves):
    if hanyeves > 20:
        return("Őn vén!")
    elif hanyeves == 20:
        return("Alkalmazható!")
    else:
        return("Ön csitri!")

def magas (magassag):
    if magassag >= 170 and magassag <= 175:
        return("Kiválló!")
    else:
        return("Elutasítva!")
    
modelnev = input("Model neve?:")
print(modelnev)
hanyeves = int(input("Hány éves?:"))
print(hanyeves)
magassag = int(input("Kérem adja meg milyen magas(cm):"))
print(magassag)
print(model(modelnev, hanyeves))
print(magas(magassag))