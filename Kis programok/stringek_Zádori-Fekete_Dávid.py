wr = open("string.txt" , 'w')
mondat = "Egyszer volt, hol nem volt, hetedhét országon is túl, volt egyszer egy szegény asszony. Annak volt egy fia meg egy kis tehénkéje."

def hossz(mondat):
    return len(mondat)
print(f'A mondat hossza:{hossz(mondat)} betű')
wr.write(f'A mondat hossza:{hossz(mondat)} betű')

def capitalize(mondat):
    return capitalize(mondat)
print(f'A mondat nagybetűvel: {capitalize(mondat)}')
wr.write(f'A mondat nagybetűvel: {capitalize(mondat)}')

def center(mondat):
    return center(mondat)
print(f'A közepe a mondatnak: {center(mondat)}')
wr.write(f'A közepe a mondatnak: {center(mondat)}')

def endswith(mondat):
    return endswith(mondat)
print(f'A mondat vége pl: . :{endswith(mondat)}')
wr.write(f'A mondat vége pl: . :{endswith(mondat)}')

def find(mondat):
    return find(mondat)
print(f'Keres:{find(mondat)}')
wr.write(f'Keres:{find(mondat)}')

def isalnum(mondat):
    return isalnum(mondat) 
print(f'isalnum: {isalnum(mondat)}')
wr.write(f'isalnum: {isalnum(mondat)}')

def isalpha(mondat):
    return isalpha(mondat)
print(f'megnézi ,hogy az ősszes karakter betű e: {isalpha(mondat)}')
wr.write(f'megnézi ,hogy az ősszes karakter betű e: {isalpha(mondat)}')

def islower(mondat):
    return islower(mondat)
print(f'megnézi ezt:{islower(mondat)}')
wr.write(f'megnézi ezt:{islower(mondat)}')

def join(mondat):
    return join(mondat)
print(f'Becsatlazik ehhez: {join(mondat)}')
wr.write(f'Becsatlazik ehhez: {join(mondat)}')
    
def lower(mondat):
    return lower(mondat)
print(f'Valami:{lower(mondat)}')
wr.write(f'Valami:{lower(mondat)}')

def Istrip(mondat):
    return Istrip(mondat)
print(f'Istrip_{Istrip(mondat)}')
wr.write(f'Istip:{Istrip(mondat)}')

def replace(mondat):
    return replace(mondat)
print(f'Kicserélés:{replace(mondat)}')
wr.write(f'Kicserélés:{replace(mondat)}')

def rfind(mondat):
    return rfind(mondat)
print(f'{rfind(mondat)}')
wr.write(f'{rfind(mondat)}')

def rstrip(mondat):
    return rstrip(mondat)
print(f'{rstrip(mondat)}')
wr.write(f'{rstrip(mondat)}')
def split(mondat):
    return split(mondat)
print(f'Elfelezi a mondatot:{split(mondat)}')
wr.write(f'Elfelezi a mondatot:{split(mondat)}')

def startswith(mondat):
    return startswith(mondat)
print(f'{startswith(mondat)}')
wr.write(f'{startswith(mondat)}')
def strip(mondat):
    return strip(mondat)
print(f'{strip(mondat)}')
wr.write(f'{strip(mondat)}')
def swapcase(mondat):
    return swapcase(mondat)
print(f'{swapcase(mondat)}')
wr.write(f'{swapcase(mondat)}')
def title(mondat):
    return title(mondat)
print(f'{title(mondat)}')
wr.write(f'{title(mondat)}')
def upper(mondat):
    return upper(mondat)
print(f'{upper(mondat)}')
wr.write({upper(mondat)})

wr.close()