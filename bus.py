class BUS:

    def __init__(self, initMem):
        self.mem = initMem
        self.cachesController = set()

    def addController(self, newCacheController):
        self.cachesController.add(newCacheController)

    def removeController(self, cacheController):
        self.cachesController.discard(cacheController)

    def WB(self, ledir, data):
        self.mem.writeData(ledir, data)

    def readMiss_Alert(self, ledir):
        getted_Data = {'M': [], 'O': [], 'E': [], 'S': [], 'I': []}
        for cacheController in self.cachesController:
            controller_resp = cacheController.controllerGet(ledir)
            if (controller_resp != []):
                getted_Data[controller_resp[0]] = controller_resp[1:]

        if (getted_Data['E'] != []):
            getted_Data['E'][1].update_EC(ledir, 'S')
            return [getted_Data['E'][0], 'S']

        elif (getted_Data['O'] != []):
            self.WB(ledir, getted_Data['O'][0])
            return [getted_Data['O'][0], 'S']

        elif (getted_Data['M'] != []):
            getted_Data['M'][1].update_EC(ledir, 'O')
            return [getted_Data['M'][0], 'S']

        else:
            return [self.read(ledir), 'E']

    def read(self, ledir):
        return self.mem.readData(ledir)
