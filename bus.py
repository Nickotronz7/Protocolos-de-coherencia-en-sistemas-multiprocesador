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

    def readMiss_Alert(self, ledir, who):
        getted_From_cache = False
        getted_Data = {'M': [], 'O': [], 'E': [], 'S': [], 'I': []}
        for cacheController in self.cachesController:
            controller_resp = cacheController.controllerGet(ledir)
            getted_Data[controller_resp[:1]] = controller_resp[1:]

        if (getted_Data['E'] != []):
            getted_Data['E'][1].update_EC(ledir, 'S')
            return [getted_Data['E'][0], 'S']

        elif (getted_Data['O'] != []):
            return [getted_Data['E'][0], 'S']

        elif (getted_Data['M'] != []):
            getted_Data['M'][1].update_EC(ledir, 'O')
            return [getted_Data['E'][0], 'S']

        else:
            getted_From_cache = True

        if (not getted_From_cache):
            return [self.read(ledir), 'E']

    def read(self, ledir):
        return self.mem.readData(ledir)
