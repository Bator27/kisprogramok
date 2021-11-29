bulizok = int(input('Hányan buliznak?'))
print('Ennyien Buliznak:' ,bulizok)
rendorok  = int(input('Hány rendőri egység ér ki időben a helyszínre?'))
print('Rendőrök létszáma:', rendorok )

if rendorok == 0:
    print('Minden bulizó megmenekült')
else:
    elkapottak_szama = 0
    for i in range(1, rendorok + 1):
        elkapottak_szama += i
        
    if elkapottak_szama < bulizok:
        elmenekultek_szama = bulizok - elkapottak_szama
        print(elkapottak_szama, "bulizot elkaptak,", elmenekultek_szama, "pedig elmenekult.")
    else:
        print("Ajaja  minenkit elkaptak!")
