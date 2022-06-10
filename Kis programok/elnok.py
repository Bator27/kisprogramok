class Elnök:
    def __init__(self,név, ország, nem):
        self.név = név
        self.ország = ország
        self.nem = nem
    def elotag(self):
        if self.nem == "n":
            return "asszony"
        else:
            return "úr"

elnokok = []

for _ in range(3):
    név = input("Add meg a miniszter elnök nevét!")
    ország = input("Add meg az ország nevét!")
    nem = input("Add meg a nemét (f/n)!")
    elnok = Elnök(név, ország,nem)
    elnokok.append(elnok)

for miniszter in elnokok:
    print(f"{miniszter.ország} miniszterelnöke {miniszter.név} {miniszter.elotag}.")