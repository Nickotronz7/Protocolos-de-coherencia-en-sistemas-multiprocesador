from cacheCell import CACHE_BLOCK


class CACHE:

    def __init__(self):
        self.cdata = []
        # [[CACHE_BLOCK(0), CACHE_BLOCK(1)], [CACHE_BLOCK(2), CACHE_BLOCK(3)]]
        for i in range(0, 2):
            t_set = []
            for j in range(0, 2):
                t_cacheBlock = CACHE_BLOCK(i+j)
                t_set += [t_cacheBlock]
            self.cdata += [t_set]

    def printCache(self):
        # cSet = int(ledir[-1])  # 111_1_
        # block = int(ledir[1])  # 1_1_11
        for cSet in range(0, 2):
            for block in range(0, 2):
                print(cSet, block, self.cdata[cSet][block].getData(
                ), self.cdata[cSet][block].getCoer())

    def getData(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        if (self.cdata[cSet][block].getDir() == ledir):
            return [self.cdata[cSet][block].getCoer(), self.cdata[cSet][block].getData()]
        else:
            return ['ReadMiss']

    def getDataWB(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        return self.cdata[cSet][block].getData()

    def setData(self, ledir, data):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11

        if (self.cdata[cSet][block].getDir() == ledir):
            self.cdata[cSet][block].setData(data)
            return ['WriteHit']
        else:
            return ['WriteMiss']

    def justSetData(self, ledir, data):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        self.cdata[cSet][block].setDir(ledir)
        self.cdata[cSet][block].setData(data)

    def set_EC(self, ledir, new_EC):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        self.cdata[cSet][block].setCoer(new_EC)

    def get_EC(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        return self.cdata[cSet][block].getCoer()
    
    def get_ledir(self, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        return self.cdata[cSet][block].getDir()
