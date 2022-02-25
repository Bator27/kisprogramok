modelnev = input("Model neve?:")
hanyeves = int(input("Hány éves?:"))
if hanyeves > 20:
    print("Őn vén!")
elif hanyeves == 20:
    print("Alkalmazható!")
else:
    print("Ön csitri!")

magassag = int(input("Kérem adja meg milyen magas(cm):"))

if magassag >= 170 and magassag <= 175:
    print("Kiválló!")
else:
    print("Elutasítva!")
