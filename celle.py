class celle:

#kontruktør
    def __init__(self):
        self._status = "død"

#Endre status
    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

#hente status
    def erLevende(self):
        return self._status == "levende"

    def hentStatusTegn(self):
        if self._status == "levende":
            return "O"
        elif self._status == "død":
            return "."

#kaller på de
