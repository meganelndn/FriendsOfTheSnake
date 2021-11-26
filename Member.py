class Member :
    # constructor
    def __init__(self, membernumber, membername) :
        self._membernumber = membernumber
        self._membername = membername
    # get
    def getMemberNumber(self) :
        return self._membernumber
    def getMemberName(self) :
        return self._membername
    # set
    def setMemberName(self, membername) :
        self._membername = membername
    # toString
    def toString(self):
        return "Member with id " + str(self.getMemberNumber()) + " is called " + self.getMemberName()