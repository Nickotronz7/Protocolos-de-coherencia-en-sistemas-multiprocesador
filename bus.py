class BUS:

    def __init__(self, initMem):
        self.mem = initMem

    def write(self, ledir, data):
        self.mem.writeData(ledir, data)

    def read(self, ledir):
        return self.mem.readData(ledir)
