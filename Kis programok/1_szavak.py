szo1 = input("Kérem adja meg az első szót!")
szo2 = input("Kérem adja meg a második szót!")
print(f'Az első szó: {szo1}')
print(f'A második szó:{szo2}')
if len(szo1) > len(szo2):
    print("Az első szó hosszabb")
elif len(szo1) < len(szo2):
    print("A második szó hosszabb")
else:
    print("A két szó ugyan olyan hosszú!")