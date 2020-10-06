import time


class MEMORY:

    def __init__(self, initClock):
        self.data = [['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000']]
        self.clock = initClock

    def wall(self):
        time.sleep(0.0001*self.clock)

    def writeData(self, ledir, data):
        block = int('0b'+ledir[:2], 2)
        cell = int('0b'+ledir[2:], 2)
        self.wall()
        self.data[block][cell] = data

    def readData(self, ledir):
        block = int('0b'+ledir[:2], 2)
        cell = int('0b'+ledir[2:], 2)
        self.wall()
        return self.data[block][cell]

    def viewData(self):
        print(self.data)

    def updateCache(self):  # maso
        print("updateando caches")
