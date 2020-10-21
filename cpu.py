import numpy as np
import random
import time
import threading


class CPU:

    def __init__(self, idInit, initController, initClock, gui):
        self.id = idInit
        self.controller = initController
        self.clock = initClock
        self.inst = ''
        self.continuos_Flag = False
        self.gui = gui

    def set_continuos_Flag(self, newFlag):
        self.continuos_Flag = newFlag

    def genMemDir(self):
        memDir = np.random.poisson(lam=9)
        if (memDir > 16):
            memDir = 16
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
        _type = np.random.normal(50.0, 10)/100
        if (0.33 <= _type < 0.67):
            # inst calc
            inst = 'P'+str(self.id)+': CALC'
            self.inst = inst
        else:
            memDir = self.genMemDir()
            if (0 <= _type < 0.33):
                # inst lectura
                inst = 'P'+str(self.id)+': READ ' + memDir
            else:
                # inst escritura
                dato = self.genDato()
                inst = 'P'+str(self.id)+': WRITE ' + memDir + ' ' + dato
        self.inst = inst

    def compute(self):
        self.genInst()
        threading.Thread(target=self.gui.drawInst(self.id, self.inst)).start()
        tinst = self.inst[4:].split(' ')
        op = tinst[0]
        if (op == 'CALC'):
            time.sleep(self.clock)
        else:
            ledir = tinst[1]
            if (op == 'WRITE'):
                data = tinst[2]
                r = self.controller.write(ledir, data)
                if (type(r) == list):
                    threading.Thread(target=self.gui.drawMem).start()
                threading.Thread(
                    target=self.gui.drawUpdateCache(self.id, ledir)).start()
            else:
                r = self.controller.read(ledir)
                if (type(r) == list):
                    threading.Thread(target=self.gui.drawMem).start()
                threading.Thread(
                    target=self.gui.drawUpdateCache(self.id, ledir)).start()

    def continuosCompute(self):
        while(self.continuos_Flag):
            self.genInst()
            threading.Thread(target=self.gui.drawInst(
                self.id, self.inst)).start()
            tinst = self.inst[4:].split(' ')
            op = tinst[0]
            if (op == 'CALC'):
                time.sleep(self.clock)
            else:
                ledir = tinst[1]
                if (op == 'WRITE'):
                    data = tinst[2]
                    r = self.controller.write(ledir, data)
                    if (type(r) == list):
                        threading.Thread(target=self.gui.drawMem).start()
                    threading.Thread(
                        target=self.gui.drawUpdateCache(self.id, ledir)).start()
                else:
                    r = self.controller.read(ledir)
                    if (type(r) == list):
                        threading.Thread(target=self.gui.drawMem).start()
                    threading.Thread(
                        target=self.gui.drawUpdateCache(self.id, ledir)).start()

    def manualCompute(self, manual_inst):
        self.inst = manual_inst
        threading.Thread(target=self.gui.drawInst(self.id, self.inst)).start()
        tinst = self.inst[4:].split(' ')
        op = tinst[0]
        if (op == 'CALC'):
            time.sleep(self.clock)
        else:
            ledir = tinst[1]
            if (op == 'WRITE'):
                data = tinst[2]
                r = self.controller.write(ledir, data)
                if (type(r) == list):
                    threading.Thread(target=self.gui.drawMem).start()
                threading.Thread(
                    target=self.gui.drawUpdateCache(self.id, ledir)).start()
            else:
                r = self.controller.read(ledir)
                if (type(r) == list):
                    threading.Thread(target=self.gui.drawMem).start()
                threading.Thread(
                    target=self.gui.drawUpdateCache(self.id, ledir)).start()
