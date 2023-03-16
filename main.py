
from spillebrett import spillebrett

def main():

    dim = input("Hva er dimensjonen på spillbrettet? format: 1x1: ")
    dim = dim.split("x")
    #print(dim)
    bredde = int(dim[0])
    hoyde = int(dim[1])

    en = spillebrett(bredde,hoyde)
    en.Tegnbrett()
    print(f"Antall celler: {bredde*hoyde}, antall levende: {en.finnAntallLevende()} og antall døde: {bredde*hoyde-en.finnAntallLevende()}")

    verdi = ""
    tall = 0


    while tall == 0:
        fortsette = input("Tast q for quit og enter for fortsette: ")
        if fortsette == verdi:
            en.oppdater()
            en.Tegnbrett()
            print(f"Antall celler: {bredde*hoyde}, antall levende: {en.finnAntallLevende()} og antall døde: {bredde*hoyde-en.finnAntallLevende()}")


        if fortsette == "q":
            print("spillet stoppet")
            tall = 1
        elif fortsette != verdi:
            print("du skrev noe feil!")


main()


"""
Tester
en = spillebrett(4,4)
#print(en.ruttenett())
#(en._generer())
#en.Tegnbrett()

(en.finnNabo(0,3))
en.oppdater()
en.oppdater()
print(en.finnAntallLevende())


"""
