def beker():
    barack = int(input("Mennyi barack termett?"))
    kereskedo = int(input("Mennyit rendeltek a kereskedők?"))
    return barack, kereskedo

def megnéz():
    if barack < kereskedo:
        print("Többet rendeltek a kereskedők ,mint amennyi termett, exportra van szükség.")
    elif barack > kereskedo:
        print("Többet termett,mint amennyit rendeltek a kereskedők , nincs szükség exportra.")
    else:
        print("Pont annyit rendeltek a kereskedők ,amennyi van, nincs szükség exportra.")

barck = 0
kereskedo = 0
barack, kereskedo = beker()
megnéz()