class CACHE_BLOCK:
    def __init__(self, idInit):
        self.id = idInit
        self.coer = 'I'
        self.dir = ''
        self.data = '0000'

    def getId(self):
        return self.id

    def setId(self, newID):
        self.id = newID

    def getCoer(self):
        return self.coer

    def setCoer(self, newCoer):
        self.coer = newCoer
    
    def getDir(self):
        return self.dir
    
    def setDir(self, newDir):
        self.dir = newDir

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData
