"""
wr = open("nyitva.txt", "w")
ora = int(input("Hány óra?"))
if ora >= 8 and ora<= 16:
    print(f"{ora} óra van , ezért nyitva van!")
    wr.write(f"{ora} óra van , ezért nyitva van!")
else:
    print(f"{ora} óra van , ezért zárva van!")
    wr.write(f"{ora} óra van , ezért zárva van!")
wr.close()
"""
wr = open("Bolt.txt", "w")
def hanyora(ora):
    if ora >=8 and ora <= 16:

        return(f'{ora} óra van, ezért nyitva van!')

    else:

        return(f'{ora} óra van , ezért zárva van!')

ora = int(input("Hány óra van?"))
print(hanyora(ora))
wr.write(f"{ora} óra van\n")
wr.write(f"hanyora{ora}")
wr.close()