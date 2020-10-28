class CONTROLLER:

    def __init__(self, initCache, initBus):
        self.bus = initBus
        self.cache = initCache
        initBus.addController(self)

    def write(self, ledir, data):
        result = self.cache.getData(ledir)
        if (result[0] != 'ReadMiss'):  # HIT
            self.cache.setData(ledir, data)
            self.bus.invalidateAlert(ledir)
            self.cache.set_EC(ledir, 'M')
            return data

        else:  # MISS
            newEC = self.cache.get_EC(ledir)
            if (newEC == 'I' or newEC == 'S'):
                self.cache.justSetData(ledir, data)
                self.bus.invalidateAlert(ledir)
                self.cache.set_EC(ledir, 'M')
                return data

            else:  # verificar todo los estados
                self.bus.WB(self.cache.get_ledir(ledir), self.cache.getDataWB(ledir))
                self.cache.justSetData(ledir, data)
                self.bus.invalidateAlert(ledir)
                self.cache.set_EC(ledir, 'M')
                return [data]

    def wirte_EC(self, ledir, data, ec):
        newEC = self.cache.get_EC(ledir)
        if (newEC == 'I' or newEC == 'S'):
            self.cache.setData(ledir, data)
            self.cache.set_EC(ledir, ec)

        else:  # verificar todo los estados
            self.bus.WB(self.cache.get_ledir(ledir), self.cache.getDataWB(ledir))
            self.cache.set_EC(ledir, ec)

    def update_EC(self, ledir, ec):
        self.cache.set_EC(ledir, ec)

    def writeBackMem(self, ledir, data):
        self.bus.WB(self.cache.get_ledir(ledir), data)

    def invalidate(self, ledir):
        self.cache.set_EC(ledir, 'I')

    def read(self, ledir): # REPARAR ESTA WEA
        cache_resp = self.cache.getData(ledir)
        ec = cache_resp[0]
        if (ec != 'ReadMiss'):  # HIT
            if (ec == 'I'):
                resp = self.bus.readMiss_Alert(ledir)  # [dato, ec]
                self.cache.justSetData(ledir, resp[0])
                self.wirte_EC(ledir, resp[0], resp[1])
                return resp[0]
            else:
                return cache_resp[1]
        else: # MISS
            resp = self.bus.readMiss_Alert(ledir)  # [dato, ec]
            actual_ec = self.cache.get_EC(ledir)
            if (actual_ec == 'M' or actual_ec == 'O'):
                self.bus.WB(self.cache.get_ledir(ledir), self.cache.getDataWB(ledir))
                self.cache.justSetData(ledir, resp[0])
                self.wirte_EC(ledir, resp[0], resp[1])
                return [resp[0]]
            else:
                self.cache.justSetData(ledir, resp[0])
                self.wirte_EC(ledir, resp[0], resp[1])
                return resp[0]

    def controllerGet(self, ledir):
        cahce_result = self.cache.getData(ledir)
        ec = cahce_result[0]
        if (ec != 'ReadMiss'):
            if (ec != 'I'):
                return cahce_result+[self]
            else:
                return []
        else:
            return []
