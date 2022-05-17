from pathlib import Path

fájl_path = (r"M:\\JanzsóG\\_10B_2021\\python10.txt")
fájl = open(fájl_path , "r")
tartalom = fájl.readlines()

sorok_száma = 0

for sor in tartalom:
    sor = sor.rstrip()
    print(sor)
    sorok_száma +=1

print(f"A szöveg {sorok_száma} sorból áll.")

fájl.close()
