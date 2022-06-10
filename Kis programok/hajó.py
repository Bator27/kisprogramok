class Hajó:
    def __init__(self, neve, típus , tulajdonos, nemzetiség, szín , tőke, gyártás):
        self.neve = neve
        self.típus = típus
        self.tuladjdonos = tulajdonos
        self.nemzetiség = nemzetiség
        self.szín = szín
        self.tőke = tőke
        self.gyártás = gyártás

hajók = []
neve = " "
while neve:
    neve = input("Add meg a hajó nevét!")
    if neve:
        tulajdonos = input("Add meg a tulaj nevét!")
        nemzetiség = input("Add meg a hajó nemzetiségét!")
        típus = input("Add meg a típusát!")
        szín = input("Add meg a hajó színét!")
        tőke = input("Add meg a hajó tőke súlyát!")
        gyártás = int(input("Add meg a hajó gyártási évét!"))
        hajócska = Hajó(neve, típus, tulajdonos, nemzetiség, szín , tőke, gyártás ) 
        hajók.append(hajócska)
    
for hajócska in hajók:
    print(f"A(z) {hajócska.neve} nevű {hajócska.típus} típusú {hajócska.nemzetiség} nemzetiségű {hajócska.gyártás}. évben gyártott hajó, {hajócska.szín} színű, {hajócska.tőke} tőke súlyú hajónak a tulaja {hajócska.tulajdonos}")
