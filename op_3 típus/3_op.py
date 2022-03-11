"""
class Tortek:
    pass
tort = Tortek()
tort.nevezo = 6
tort.szamlalo = 12
print(tort.szamlalo/tort.nevezo)
"""
"""
class Tortek:
    def kiír(self):
        print("%d/%d" % (self.szamlalo,\
            self.nevezo),end= " ")
tort = Tortek()
tort.szamlalo = 180
tort.nevezo = 120
tort.kiír()
"""
"""
class Tortek:
    def kiír(self):
        print("%d/%d" % (self.szamlalo,\
            self.nevezo),end= " ")
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót:"))
        self.nevezo = int(input("Kérem a nevezőt:"))

tort = Tortek()
tort.beker()
tort.kiír()
"""
class Tortek:
    def __init__(self):
        self.szamlalo = 0
        self.nevezo = 1
    def kiír(self):
        print("%d/%d" % (self.szamlalo,\
            self.nevezo),end= " ")
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót:"))
        self.nevezo = int(input("Kérem a nevezőt:"))
    def szamlalotad(self):
        return self.szamlalo
    def nevezotad(self):
        return self.nevezo

tort = Tortek()
tort.kiír()
tort.beker()
#print(tort.kiír())
print(tort.szamlalotad())
print(tort.nevezotad())