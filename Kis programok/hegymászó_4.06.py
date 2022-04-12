from ossaudiodev import SNDCTL_DSP_GETBLKSIZE


hegym1 = int(input('Kérem adja meg a hegy magasságát!'))
hegym2 = int(input('Kérem adja meg a másik hegy magasságát!'))
if hegym1 > hegym2:
    print(f'Az első {hegym1} magasabb, mint a {hegym2}')
elif hegym1 < hegym2:
    print(f'Az második {hegym2} magasabb. ,mint a {hegym1}')
else:
    print("A két hegy egyenlő magas!")
#2 átváltás defbe
def magas(m):
    return m/1000
def nev(hegymaszo_nev):
    mgh = ["a","á","e","é","i","í","o","ó","ö","ő","ü","ű","A","Á","E","É","I","Í","O","Ó","Ö","Ő","Ü","Ű"]
    if hegymaszo_nev[0] in mgh:
        return "Az"
    else:
        return "A"
def nagybetű(hegymaszo_nev):
    return hegymaszo_nev.upper()
for _ in range(3):
    hegymaszo_nev = input("Kérem adja meg a hegymászó nevét!")
    mászás = int(input("Kérem adja meg ,hogy milyen magasra jutott fel a hegymászó!"))
    váltás = float(magas(mászás))
    méter = mászás
    print(f'{hegymaszo_nev} {váltás} km magasagra jutott fel.')

#3
class Szuperhos:
    def __init__(self, nev, szuperero = 50):
        self.nev = nev
        self.szuperero = szuperero

hos1 = Szuperhos('Thor', 70)
hos2 = Szuperhos('Hulk', 70)
print(hos1)
print(hos2)

def erosebb(hos1 = Szuperhos='',0))