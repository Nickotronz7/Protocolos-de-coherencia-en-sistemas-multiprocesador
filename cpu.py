import numpy as np
import random
import time


class CPU:

    def __init__(self, idInit, cacheInit, initControl, initClock, initBus):
        self.id = idInit
        self.cache = cacheInit
        self.control = initControl
        self.clock = initClock
        self.inst = ''
        self.bus = initBus

    def genMemDir(self):
        memDir = random.randrange(0, 16, 1)
        memDir = "{0:b}".format(memDir)
        gap = 4 - len(memDir)
        if (gap):
            while (gap != 0):
                memDir = '0'+memDir
                gap -= 1
            return memDir
        else:
            return memDir

    def genDato(self):
        dato = hex(random.randrange(0, 65536, 1))
        dato = dato[2:].upper()
        return dato

    def genInst(self):
        _type = np.random.rand()
        if (0 <= _type < 0.33):
            # inst calc
            inst = 'P'+str(self.id)+': CALC'
            self.inst = inst
        else:
            memDir = self.genMemDir()
            if (0.33 <= _type < 0.67):
                # inst escritura
                dato = self.genDato()
                inst = 'P'+str(self.id)+': WRITE ' + memDir + ' ' + dato
            else:
                # inst lectura
                inst = 'P'+str(self.id)+': READ ' + memDir
        self.inst = inst

    def compute(self):
        self.genInst()
        tinst = self.inst[4:].split(' ')
        op = tinst[0]
        if (op == 'CALC'):
            time.sleep(self.clock)
        elif (op == 'WRITE'):
            # print('write')
            self.cache.setData(tinst[1], tinst[2])
            self.bus.write(tinst[1], tinst[2]) # no necesariamente siempre ver el moesi
        else:
            print('read')
            # 
