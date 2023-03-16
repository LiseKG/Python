from celle import celle
from random import randint

class spillebrett():
    def __init__(self,kolonner,rader):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjon = 0
        #lager først er spillebrett
        rutenett = []
        i = 0
        while i < self._rader:
            y = 0
            kolonner = []
            while y < self._kolonner:
                ce = celle()
                kolonner.append(ce)
                y = y+1
            rutenett.append(kolonner)
            i = i+1
        self._rutenett = rutenett
        self._generer()

    def Tegnbrett(self):
        print(" ")
        print(f"Dette er generasjon {self._generasjon}:")
        #self.oppdater()

        # For å tomme teminalvinduet - syns ikke dette ser fint ut derfor skrevet ut
        """
        if self._rader:
            i = 0
            while i < 10:
                print(" ")
                i = i+1
        """
        for rad in self._rutenett:
            for verdi in rad: #hvert element sitt tegn blir skrevet ut
                print(verdi.hentStatusTegn(),end=" ")
            print(" ") #rad print

        print(" ") #style print


    def oppdater(self):
        self._generasjon = self._generasjon+1
        #print("Dette er generasjon "+str(self._generasjon))
        dodeceller = []
        levendeceller = []

        list = []
        for rad in self._rutenett:
            for verdi in rad:
                a = self._rutenett.index(rad) #setter verdiene til index
                b = rad.index(verdi)
                nabolist = self.finnNabo(a,b)
                lev = 0

                for i in (nabolist):
                    if i.erLevende():
                        lev = lev+1

                #print(f" {lev} poeng")
                #spillregler
                if self._rutenett[a][b].erLevende():
                    if lev < 2:
                        dodeceller.append(self._rutenett[a][b])
                    elif lev > 3:
                        dodeceller.append(self._rutenett[a][b])
                    #print(f"cellen er {self._rutenett[a][b][1]} er død" )
                elif self._rutenett[a][b].erLevende() == False:
                    if lev == 3:
                        levendeceller.append(self._rutenett[a][b])
                        #print(f"cellen er {self._rutenett[a][b]} er levende" )
                b = b+1
            a = a+1

        for rad in self._rutenett:
            for r in rad:
                if r in dodeceller:
                    r.settDoed() #endrer status
                if r in levendeceller:
                    r.settLevende() #endrer status


    def finnAntallLevende(self):
        lev = 0
        dod = 0
        i = 0
        while i < self._rader:
            y = 0
            while y < self._kolonner:
                if self._rutenett[i][y].hentStatusTegn() == "O":
                    lev = lev+1
                else:
                    dod = dod+1

                y = y+1
            i = i+1
        return lev #returnere antalllevende verdi
        #f"Det er {self._rader*self._kolonner} celler: {lev} levende og {dod} døde"


    def _generer(self):
        for rad in self._rutenett:
            for celle in rad:
                verdi = randint(1,3)
                #print(verdi) Verdi som er 1,2 eller 3.
                if verdi == 2: #er verdien 2 blir cellen levende
                    celle.settLevende()
                else: #dor pa 1 og 2
                    celle.settDoed()


    def finnNabo(self,rad,kol):
        naboverdi = []
        #skjekker om verdiene er i rutenettet
        if rad > self._rader:
            return None
        if kol > self._kolonner:
            return None
        #lister med nabo verdi
        listeR = [rad-1,rad,rad+1]
        listeK = [kol-1,kol,kol+1]

        for i in listeR:
            if i < 0 or i > self._rader-1: #fjerner verdier utenfor nettet
                listeR.remove(i)
        #print(listeR)
        for i in listeK:
            if i < 0 or i > self._kolonner-1: #fjerner verdier utenfor
                listeK.remove(i)
        #print(listeK)

        for R in listeR:
            for K in listeK:
                if R == rad and K == kol:
                    valgtcelle = self._rutenett[R][K] #Dette er cellen vi valgte
                else:
                    naboverdi.append(self._rutenett[R][K]) #nabocelle legges inn i listen

                    """
                   if self._rutenett[R][K][0] == "O":
                        antalllevende= antalllevende+1
                    if self._rutenett[R][K][0] == "X":
                        antalldode = antalldode+1
                    """

                #print(naboverdi)
        return(naboverdi) #returnerer liste med naboverdiene
