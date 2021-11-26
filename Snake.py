class Snake :
    def __init__(self, snakenumber, snakename, snaketype, member = None) :
        self._snakenumber = snakenumber
        self._snakename = snakename
        self._snaketype = snaketype
        self._member = member
    # get
    def getSnakeNumber(self) :
        return self._snakenumber
    def getSnakeName(self) :
        return self._snakename
    def getSnakeType(self) :
        return self._snaketype
    def getMember(self) :
        return self._member
    # set
    def setSnakeName(self, snakename) :
        self._snakename = snakename
    def setSnakeType(self, snaketype) :
        self._snaketype = snaketype
    def setMember(self, member) :
        self._member = member
    # toString
    def toString(self) :
        return self._getSnakeName() + " has the id: " + str(self.getSnakeNumber()) + " and is a " + self.getSnakeType() + ". Its owner is: " + str(self.getMember())