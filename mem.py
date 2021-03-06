import time


class MEMORY:

    def __init__(self, initClock):
        self.data = [['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000'],
                     ['0000', '0000', '0000', '0000']]
        self.clock = initClock

    def wall(self):
        # time.sleep(5*self.clock)
        print("Memoria super Rapida")

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

    def getData(self):
        return self.data
