import random
import math


class Henger:
     def __init__(self,sugar,kozeppont =(0,0), magassag = 10):
        self.kozeppont = kozeppont
        self.sugar = sugar
        self.magassag = magassag
     def terulet (self):
       return self.sugar*pow(math.pi,2)
     def felszin (self):
         F= 2 * self.sugar * self.sugar * math.pi + \
         2 * self.sugar * math.pi *self.magassag
         return F

     def terfogat (self):
        V = self.sugar * self.sugar * math.pi * self.magassag
        V = math.pow(self.sugar,2)*math.pi * self.magassag
#objektum létrehozása
henger_01= Henger(5,(2,4),12)
henger_02= Henger(5,(2,4),12)
#objektum tesztelése
#hangszer = Henger(5,(2,4),12)
#print(f"A térfogata:{hangszer.térfogat:.2f} \nA felszíne:{hangszer.felszin:.2f}")

# terület, felszín és térfogat nevu metodus meghívása
print(henger_01)
print(type(henger_01))
print(isinstance(henger_01,Henger))

hengerek = []

for _ in range(5):
   henger = Henger(random.randint(0,10),2,4, random.randint(1,10))
   henger.append(hengerek)
for  hengerr in hengerek:
   hengerr.info()

print(f'A térfogata:{henger_01.terfogat:.2} \nA felszine:: {henger_01}')