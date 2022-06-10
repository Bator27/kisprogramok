def jogosult(bika):
    if bika <= 300:
        return True
    else:
        return False

farmer = "emberke"

while farmer:
    farmer = input("Add meg a farmer nevét!")
    if farmer:
        bika = int(input("Add meg a bikák számát!"))
        if jogosult(bika):
            print(f"{farmer} jogosult a támogatásra, közepes méretű farmja van.")
        else:
            print(f"{farmer} nem jogosult a támogatásra, a farmja nem közepes méretű.")