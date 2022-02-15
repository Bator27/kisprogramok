szam1 = int(input("Kérem ajdon meg számot!"))
print(f'A első szám: {szam1}')
szam2 = int(input("Kérem adjon meg még egy számot!"))
print(f'A második szám: {szam2}')

if szam1 == szam2:
    print("Egyenlő a két szám!")
elif szam1 > szam2:
    print("Az első szám nagyobb ,mint a második")
else:
    print("A második szám a nagyobb,mint az első")

