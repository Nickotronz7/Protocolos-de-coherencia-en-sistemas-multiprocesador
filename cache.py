# implementar SNOOPING

class CACHE:

    def __init__(self):
        self.cdata = [
            [{'#block': 0, 'ec': 'N', 'dir': '', 'data': ''},
             {'#block': 1, 'ec': 'N', 'dir': '', 'data': ''}],
            [{'#block': 2, 'ec': 'N', 'dir': '', 'data': ''},
             {'#block': 3, 'ec': 'N', 'dir': '', 'data': ''}]]

    def getData(self, ledir):
        block = int(ledir[0])
        cell = int(ledir[1])
        if (self.cdata[block][cell]['dir'] == ledir):
            return self.cdata[block][cell]['data']
        else:
            return 'Miss'

    def setData(self, ledir, data):
        block = int(ledir[0])
        cell = int(ledir[1])
        self.cdata[block][cell]['dir'] = ledir
        self.cdata[block][cell]['data'] = data
        self.cdata[block][cell]['ec'] = 'M'