from cacheCell import CACHE_BLOCK


class CACHE:

    def __init__(self):
        self.cdata = [[CACHE_BLOCK(0), CACHE_BLOCK(1)], [
            CACHE_BLOCK(2), CACHE_BLOCK(3)]]

    def getData(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        if (self.cdata[cSet][block].dir == ledir):
            return [self.cdata[cSet][block].coer, self.cdata[cSet][block].data]
        else:
            return ['ReadMiss']
    
    def getDataWB(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        return self.cdata[cSet][block].data

    def setData(self, ledir, data):
        # implementar politica de reemplazo
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11

        if (self.cdata[cSet][block].dir == ledir):
            self.cdata[cSet][block].data = data
            return ['WriteHit']
        else:
            return ['WriteMiss']

    def set_EC(self, ledir, new_EC):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        self.cdata[cSet][block].coer = new_EC

    def get_EC(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        return self.cdata[cSet][block].coer
