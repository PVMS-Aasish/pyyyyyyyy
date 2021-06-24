class Cricket(object):
    def __init__(self,playerteam,playertype):
        self.playerteam = playerteam
        self.playertype = playertype

    def setplayerteam(self,playerteam):
        self.playerteam = playerteam 

    def setplayertype(self,playertype):
        self.playertype=playertype

    def getdetails(self):
        print(self.playerteam)
        print(self.playertype)

Aasish = Cricket("rcb","wicketkeeper-batsman")
Aasish.getdetails()