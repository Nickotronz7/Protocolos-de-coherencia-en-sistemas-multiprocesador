import tkinter as tk
from tkinter import ttk
import threading
import time
from cpu import CPU
from cache import CACHE
from controller import CONTROLLER
from bus import BUS
from mem import MEMORY


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.appMode = tk.IntVar()
        self.appMode.set(0)
        self.checkBox_value = tk.BooleanVar(self)
        self.checkBox_value.set(False)
        self.checkMain_value = tk.BooleanVar(self)
        self.checkMain_value.set(False)

        self.runnig = False

        # Frames
        self.controlFrame = tk.Frame(self)
        self.controlFrame.grid(row=0, column=0)

        self.modeFrame = tk.Frame(self.controlFrame)
        self.modeFrame.grid(row=1, column=0)

        self.controlButtonsFrame = tk.Frame(self.controlFrame)
        self.controlButtonsFrame.grid(row=1, column=2)

        self.manualInstFrame = tk.Frame(self.controlButtonsFrame)
        self.manualInstFrame.grid(row=2, column=0)

        self.masterControlFrame = tk.Frame(self.controlButtonsFrame)
        self.masterControlFrame.grid(row=3)

        self.upperButtonFrame = tk.Frame(self.controlButtonsFrame)
        self.upperButtonFrame.grid(row=0, column=0)

        self.lowerButtonFrame = tk.Frame(self.controlButtonsFrame)
        self.lowerButtonFrame.grid(row=1, column=0)

        self.instrucctionFrame = tk.Frame(self)
        self.instrucctionFrame.grid(row=2, column=0)

        self.instrucctionBlockFrame = tk.Frame(self.instrucctionFrame)
        self.instrucctionBlockFrame.grid(row=2, column=0)

        self.memFrame = tk.Frame(self)
        self.memFrame.grid(row=0, column=2, rowspan=3)

        self.memBlockFrame = tk.Frame(self.memFrame)
        self.memBlockFrame.grid(row=1, rowspan=2)

        self.cacheFrame = tk.Frame(self)
        self.cacheFrame.grid(row=4, columnspan=3)

        self.p1CacheFrame = tk.Frame(self.cacheFrame)
        self.p2CacheFrame = tk.Frame(self.cacheFrame)
        self.p3CacheFrame = tk.Frame(self.cacheFrame)
        self.p4CacheFrame = tk.Frame(self.cacheFrame)
        self.p1CacheFrame.grid(row=1, column=0)
        self.p2CacheFrame.grid(row=1, column=1)
        self.p3CacheFrame.grid(row=1, column=2)
        self.p4CacheFrame.grid(row=1, column=3)

        self.pack()
        self.create_widgets()
        self.init_Compu()

    def init_Compu(self):
        clock = 1
        self.mainMem = MEMORY(clock)
        self.dataBus = BUS(self.mainMem)
        cache_1 = CACHE()
        cache_2 = CACHE()
        cache_3 = CACHE()
        cache_4 = CACHE()
        control_1 = CONTROLLER(cache_1, self.dataBus)
        control_2 = CONTROLLER(cache_2, self.dataBus)
        control_3 = CONTROLLER(cache_3, self.dataBus)
        control_4 = CONTROLLER(cache_4, self.dataBus)
        self.p1 = CPU(1, control_1, clock, self)
        self.p2 = CPU(2, control_2, clock, self)
        self.p3 = CPU(3, control_3, clock, self)
        self.p4 = CPU(4, control_4, clock, self)
        self.drawMem()
        self.drawInitCache()

    def create_widgets(self):

        # Separadores
        # Verticales
        self.vs1 = ttk.Separator(self.controlFrame, orient=tk.VERTICAL)
        self.vs1.grid(row=1, column=1, sticky='ns')

        self.vs2 = ttk.Separator(self, orient=tk.VERTICAL)
        self.vs2.grid(row=0, column=1, rowspan=3, sticky='ns', padx=2)

        # Horizontales
        self.hs1 = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.hs1.grid(row=1, column=0, sticky='we', pady=2)

        self.hs2 = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.hs2.grid(row=3, column=0, sticky='we', pady=5, columnspan=3)

        self.endLine = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.endLine.grid(row=5, columnspan=3, sticky='we', pady=5)

        # Etiquetas

        self.controlLabel = tk.Label(self.controlFrame, text='Control')
        self.controlLabel.grid(row=0, column=1)

        self.modoLabel = tk.Label(self.modeFrame, text='Modo')
        self.modoLabel.grid()

        self.instMLabel = tk.Label(self, text='Instruccion Manual')

        self.instTitle = tk.Label(self.instrucctionFrame, text='Instrucciones')
        self.instTitle.grid(row=0)

        self.memLabel = tk.Label(self.memFrame, text='Memory')
        self.memLabel.grid(row=0)

        self.h00Label = tk.Label(self.memBlockFrame, text='00')
        self.h00Label.grid(row=1, column=1)

        self.h01Label = tk.Label(self.memBlockFrame, text='01')
        self.h01Label.grid(row=1, column=2)

        self.h10Label = tk.Label(self.memBlockFrame, text='10')
        self.h10Label.grid(row=1, column=3)

        self.h11Label = tk.Label(self.memBlockFrame, text='11')
        self.h11Label.grid(row=1, column=4)

        self.v00Label = tk.Label(self.memBlockFrame, text='00')
        self.v00Label.grid(row=2, column=0)

        self.v01Label = tk.Label(self.memBlockFrame, text='01')
        self.v01Label.grid(row=3, column=0)

        self.v10Label = tk.Label(self.memBlockFrame, text='10')
        self.v10Label.grid(row=4, column=0)

        self.v11Label = tk.Label(self.memBlockFrame, text='11')
        self.v11Label.grid(row=5, column=0)

        self.cacheLabel = tk.Label(self.cacheFrame, text='Cache')
        self.cacheLabel.grid(row=0, columnspan=4)

        self.p1cacheLabel = tk.Label(self.p1CacheFrame, text='P1')
        self.p2cacheLabel = tk.Label(self.p2CacheFrame, text='P2')
        self.p3cacheLabel = tk.Label(self.p3CacheFrame, text='P3')
        self.p4cacheLabel = tk.Label(self.p4CacheFrame, text='P4')
        self.p1cacheLabel.grid(row=0)
        self.p2cacheLabel.grid(row=0)
        self.p3cacheLabel.grid(row=0)
        self.p4cacheLabel.grid(row=0)

        self.p1instLabel = tk.Label(self.instrucctionBlockFrame, text='P1')
        self.p2instLabel = tk.Label(self.instrucctionBlockFrame, text='P2')
        self.p3instLabel = tk.Label(self.instrucctionBlockFrame, text='P3')
        self.p4instLabel = tk.Label(self.instrucctionBlockFrame, text='P4')
        self.p1instLabel.grid(row=0, column=0)
        self.p2instLabel.grid(row=0, column=1)
        self.p3instLabel.grid(row=0, column=2)
        self.p4instLabel.grid(row=0, column=3)

        # Botones
        boton_padx = 2
        boton_pady = 2

        self.doitButton = tk.Button(
            self.manualInstFrame,
            text='Do it',
            command=self.doitButton_Clicked,
            state=tk.DISABLED
        )
        self.doitButton.grid(row=0, column=5, padx=boton_padx, pady=boton_pady)

        self.stopButton = tk.Button(
            self.upperButtonFrame,
            text='Detener',
            command=self.stopButton_Clicked,
            state=tk.DISABLED
        )
        self.stopButton.grid(row=0, column=2, padx=boton_padx, pady=boton_pady)

        self.initButton = tk.Button(
            self.upperButtonFrame,
            text='Iniciar',
            command=self.initiButton_Clicked
        )
        self.initButton.grid(row=0, column=0, padx=boton_padx, pady=boton_pady)

        self.resetButton = tk.Button(
            self.upperButtonFrame,
            text='Reset',
            command=self.resetButton_Clicked
        )
        self.resetButton.grid(
            row=0, column=1, padx=boton_padx, pady=boton_pady)

        self.nextButton = tk.Button(
            self.lowerButtonFrame,
            text='Siguiente',
            state=tk.DISABLED,
            command=self.nextButton_Clicked
        )
        self.nextButton.grid(row=0, column=0, padx=boton_padx, pady=boton_pady)

        self.continueButton = tk.Button(
            self.lowerButtonFrame,
            text='Continuar',
            command=self.continueButton_Clicked,
            state=tk.DISABLED
        )
        self.continueButton.grid(
            row=0, column=1, padx=boton_padx, pady=boton_pady)

        self.pauseButton = tk.Button(
            self.lowerButtonFrame,
            text='Pausa',
            state=tk.DISABLED,
            command=self.pauseButton_Clicked
        )
        self.pauseButton.grid(
            row=0, column=2, padx=boton_padx, pady=boton_pady)

        self.masterButton = tk.Button(
            self.masterControlFrame,
            text='Master',
            command=self.masterButton_Clicked
        )
        self.masterButton.config(state=tk.DISABLED)
        self.masterButton.grid(row=0, column=1)

        # RadioBotons
        self.contRadio = tk.Radiobutton(
            self.modeFrame, text='Continuo',
            variable=self.appMode,
            value=0,
            command=self.getSelected
        )
        self.contRadio.grid(row=1, column=0, sticky='w')

        self.stepsRadio = tk.Radiobutton(
            self.modeFrame, text='Steps',
            variable=self.appMode,
            value=1,
            command=self.getSelected
        )
        self.stepsRadio.grid(row=2, column=0, sticky='w')

        self.ciclosRadio = tk.Radiobutton(
            self.modeFrame, text='Ciclos',
            variable=self.appMode,
            value=2,
            command=self.getSelected
        )
        self.ciclosRadio.grid(row=3, column=0, sticky='w')

        # SpinBox
        self.ciclosSpin = tk.Spinbox(
            self.modeFrame,
            from_=1, to=10,
            state='disabled',
            width='5'
        )
        self.ciclosSpin.grid(row=3, column=1, sticky='w')

        # TextEntry
        self.manualInstTextBoxDir = tk.Entry(
            self.manualInstFrame,
            state=tk.DISABLED,
            width=5
        )
        self.manualInstTextBoxDir.grid(row=0, column=3, padx=2)

        self.manualInstTextBoxData = tk.Entry(
            self.manualInstFrame,
            state=tk.DISABLED,
            width=5
        )
        self.manualInstTextBoxData.grid(row=0, column=4, padx=2)

        # TextBox
        self.instProc1 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc1.config(state=tk.DISABLED)
        self.instProc1.grid(row=1, column=0, padx=2)

        self.instProc2 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc2.config(state=tk.DISABLED)
        self.instProc2.grid(row=1, column=1, padx=2)

        self.instProc3 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc3.config(state=tk.DISABLED)
        self.instProc3.grid(row=1, column=2, padx=2)

        self.instProc4 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc4.config(state=tk.DISABLED)
        self.instProc4.grid(row=1, column=3, padx=2)

        memblock_height = 3
        memblock_width = 15
        # 0000
        self.memBlock0000 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0000.grid(row=2, column=1, padx=2, pady=2)

        self.memBlock0001 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0001.grid(row=2, column=2, padx=2, pady=2)

        self.memBlock0010 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0010.grid(row=2, column=3, padx=2, pady=2)

        self.memBlock0011 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0011.grid(row=2, column=4, padx=2, pady=2)

        # 0100
        self.memBlock0100 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0100.grid(row=3, column=1, padx=2, pady=2)

        self.memBlock0101 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0101.grid(row=3, column=2, padx=2, pady=2)

        self.memBlock0110 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0110.grid(row=3, column=3, padx=2, pady=2)

        self.memBlock0111 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock0111.grid(row=3, column=4, padx=2, pady=2)

        # 1000
        self.memBlock1000 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1000.grid(row=4, column=1, padx=2, pady=2)

        self.memBlock1001 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1001.grid(row=4, column=2, padx=2, pady=2)

        self.memBlock1010 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1010.grid(row=4, column=3, padx=2, pady=2)

        self.memBlock1011 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1011.grid(row=4, column=4, padx=2, pady=2)

        # 1100
        self.memBlock1100 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1100.grid(row=5, column=1, padx=2, pady=2)

        self.memBlock1101 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1101.grid(row=5, column=2, padx=2, pady=2)

        self.memBlock1110 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1110.grid(row=5, column=3, padx=2, pady=2)

        self.memBlock1111 = tk.Text(
            self.memBlockFrame, height=memblock_height, width=memblock_width,
            state=tk.DISABLED)
        self.memBlock1111.grid(row=5, column=4, padx=2, pady=2)

        cacheblock_height = 3
        cacheblock_width = 16
        cacheblock_padx = 2
        cacheblock_pady = 2

        self.p1bock1 = tk.Text(
            self.p1CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p1bock2 = tk.Text(
            self.p1CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p1bock3 = tk.Text(
            self.p1CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p1bock4 = tk.Text(
            self.p1CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p1bock1.grid(row=1, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p1bock2.grid(row=2, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p1bock3.grid(row=3, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p1bock4.grid(row=4, padx=cacheblock_padx, pady=cacheblock_pady)

        self.p2bock1 = tk.Text(
            self.p2CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p2bock2 = tk.Text(
            self.p2CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p2bock3 = tk.Text(
            self.p2CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p2bock4 = tk.Text(
            self.p2CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p2bock1.grid(row=1, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p2bock2.grid(row=2, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p2bock3.grid(row=3, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p2bock4.grid(row=4, padx=cacheblock_padx, pady=cacheblock_pady)

        self.p3bock1 = tk.Text(
            self.p3CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p3bock2 = tk.Text(
            self.p3CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p3bock3 = tk.Text(
            self.p3CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p3bock4 = tk.Text(
            self.p3CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p3bock1.grid(row=1, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p3bock2.grid(row=2, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p3bock3.grid(row=3, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p3bock4.grid(row=4, padx=cacheblock_padx, pady=cacheblock_pady)

        self.p4bock1 = tk.Text(
            self.p4CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p4bock2 = tk.Text(
            self.p4CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p4bock3 = tk.Text(
            self.p4CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p4bock4 = tk.Text(
            self.p4CacheFrame, width=cacheblock_width, height=cacheblock_height,
            state=tk.DISABLED)
        self.p4bock1.grid(row=1, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p4bock2.grid(row=2, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p4bock3.grid(row=3, padx=cacheblock_padx, pady=cacheblock_pady)
        self.p4bock4.grid(row=4, padx=cacheblock_padx, pady=cacheblock_pady)

        # DropDown Menu
        self.instList = ['CALC', 'READ', 'WRITE']
        self.instVar = tk.StringVar(self)
        self.instVar.set(self.instList[0])
        self.instVar.trace_add('write', self.boxEnable)
        self.dropdown = tk.OptionMenu(
            self.manualInstFrame, self.instVar, *self.instList)
        self.dropdown.configure(state=tk.DISABLED)
        self.dropdown.grid(row=0, column=2)

        self.procList = ['P1', 'P2', 'P3', 'P4']
        self.procVar = tk.StringVar(self)
        self.procVar.set(self.procList[0])
        self.procDrop = tk.OptionMenu(
            self.manualInstFrame, self.procVar, *self.procList
        )
        self.procDrop.config(state=tk.DISABLED)
        self.procDrop.grid(row=0, column=1)

        # CheckBox
        self.checkManualInst = tk.Checkbutton(
            self.manualInstFrame,
            text='Instruccion Manual',
            variable=self.checkBox_value,
            command=self.checkBox_clicked
        )
        self.checkManualInst.grid(row=0, column=0)

        self.checkMaster = tk.Checkbutton(
            self.masterControlFrame,
            text='MasterCheck',
            variable=self.checkMain_value,
            command=self.checkMaster_Clicked
        )
        self.checkMaster.grid(row=0, column=0)

    # Funciones
    def checkMaster_Clicked(self):
        self.checkMain_value = not self.checkMain_value
        if (self.checkMain_value):
            self.masterButton.config(state=tk.NORMAL)
        else:
            self.masterButton.config(state=tk.DISABLED)

    def doitButton_Clicked(self):
        inst = self.instVar.get()
        proc = self.procVar.get()
        proc_id = int(proc[-1])

        if (inst == 'CALC'):
            manual_inst = proc+': '+inst
        elif (inst == 'READ'):
            memDir = self.manualInstTextBoxDir.get()
            manual_inst = proc+': '+inst+' '+memDir
        else:
            memDir = self.manualInstTextBoxDir.get()
            dato = self.manualInstTextBoxData.get()
            manual_inst = proc+': '+inst+' '+memDir+' '+dato

        if (proc_id == 1):
            threading.Thread(target=self.p1.manualCompute(manual_inst)).start()
        elif (proc_id == 2):
            threading.Thread(target=self.p2.manualCompute(manual_inst)).start()
        elif (proc_id == 3):
            threading.Thread(target=self.p3.manualCompute(manual_inst)).start()
        else:
            threading.Thread(target=self.p4.manualCompute(manual_inst)).start()

    def masterButton_Clicked(self):
        self.masterButton.config(state=tk.DISABLED)
        threading.Thread(target=self.programMainLoop).start()

    def boxEnable(self, a, b, c):
        varVal = self.instVar.get()
        if (varVal == 'CALC'):
            self.manualInstTextBoxDir['state'] = tk.DISABLED
            self.manualInstTextBoxData['state'] = tk.DISABLED
        elif (varVal == 'READ'):
            self.manualInstTextBoxDir['state'] = tk.NORMAL
            self.manualInstTextBoxData['state'] = tk.DISABLED
        else:
            self.manualInstTextBoxDir['state'] = tk.NORMAL
            self.manualInstTextBoxData['state'] = tk.NORMAL

    def checkBox_clicked(self):
        self.checkBox_value = not self.checkBox_value
        if(self.checkBox_value):
            self.dropdown.configure(state=tk.NORMAL)
            self.procDrop.config(state=tk.NORMAL)
            self.doitButton.config(state=tk.NORMAL)
            varVal = self.instVar.get()
            if (varVal == 'CALC'):
                self.manualInstTextBoxDir['state'] = tk.DISABLED
                self.manualInstTextBoxData['state'] = tk.DISABLED
            elif (varVal == 'READ'):
                self.manualInstTextBoxDir['state'] = tk.NORMAL
                self.manualInstTextBoxData['state'] = tk.DISABLED
            else:
                self.manualInstTextBoxDir['state'] = tk.NORMAL
                self.manualInstTextBoxData['state'] = tk.NORMAL
        else:
            self.doitButton.config(state=tk.DISABLED)
            self.dropdown.configure(state=tk.DISABLED)
            self.procDrop.config(state=tk.DISABLED)
            self.manualInstTextBoxDir['state'] = tk.DISABLED
            self.manualInstTextBoxData['state'] = tk.DISABLED

    def getSelected(self):
        if (self.appMode.get() == 2):
            self.ciclosSpin['state'] = 'readonly'
            self.nextButton.config(state=tk.DISABLED)
            self.continueButton.config(state=tk.NORMAL)
            self.p1.set_continuos_Flag(False)
            self.p2.set_continuos_Flag(False)
            self.p3.set_continuos_Flag(False)
            self.p4.set_continuos_Flag(False)
        elif (self.appMode.get() == 1):
            self.nextButton.config(state=tk.NORMAL)
            self.continueButton.config(state=tk.DISABLED)
            self.p1.set_continuos_Flag(False)
            self.p2.set_continuos_Flag(False)
            self.p3.set_continuos_Flag(False)
            self.p4.set_continuos_Flag(False)
        else:
            self.p1.set_continuos_Flag(True)
            self.p2.set_continuos_Flag(True)
            self.p3.set_continuos_Flag(True)
            self.p4.set_continuos_Flag(True)
            self.nextButton.config(state=tk.DISABLED)
            self.ciclosSpin['state'] = tk.DISABLED
            self.continueButton.config(state=tk.NORMAL)

    def initiButton_Clicked(self):
        self.runnig = True
        self.initButton.config(state=tk.DISABLED)
        self.resetButton.config(state=tk.DISABLED)
        self.resetButton.config(state=tk.DISABLED)
        self.continueButton.config(state=tk.DISABLED)
        self.pauseButton.config(state=tk.NORMAL)
        self.pauseButton.config(state=tk.NORMAL)
        self.stopButton.config(state=tk.NORMAL)

    def stopButton_Clicked(self):
        self.runnig = False
        self.p1.set_continuos_Flag(False)
        self.p2.set_continuos_Flag(False)
        self.p3.set_continuos_Flag(False)
        self.p4.set_continuos_Flag(False)
        self.initButton.config(state=tk.NORMAL)
        self.resetButton.config(state=tk.NORMAL)
        self.pauseButton.config(state=tk.DISABLED)
        self.stopButton.config(state=tk.DISABLED)

    def resetButton_Clicked(self):
        self.runnig = False
        self.initButton.config(state=tk.NORMAL)
        self.stopButton.config(state=tk.DISABLED)
        print(self.runnig)
        self.init_Compu()

    def pauseButton_Clicked(self):
        self.runnig = False
        self.p1.set_continuos_Flag(False)
        self.p2.set_continuos_Flag(False)
        self.p3.set_continuos_Flag(False)
        self.p4.set_continuos_Flag(False)
        self.continueButton.config(state=tk.NORMAL)
        self.pauseButton.config(state=tk.DISABLED)

    def continueButton_Clicked(self):
        self.runnig = True
        threading.Thread(target=self.programMainLoop).start()
        self.continueButton.config(state=tk.DISABLED)
        self.pauseButton.config(state=tk.NORMAL)

    def step(self):
        proc1_tred = threading.Thread(
            target=self.p1.compute())
        proc2_tred = threading.Thread(
            target=self.p2.compute())
        proc3_tred = threading.Thread(
            target=self.p3.compute())
        proc4_tred = threading.Thread(
            target=self.p4.compute())
        proc1_tred.start()
        proc2_tred.start()
        proc3_tred.start()
        proc4_tred.start()
        proc1_tred.join()
        proc2_tred.join()
        proc3_tred.join()
        proc4_tred.join()
        self.nextButton.config(state=tk.NORMAL)

    def nextButton_Clicked(self):
        self.nextButton.config(state=tk.DISABLED)
        x = threading.Thread(target=self.step)
        x.start()

    def programMainLoop(self):
        while (self.checkMain_value):
            if (self.runnig):
                if (self.appMode.get() == 0):
                    print('picha se mama con el modo continuo')
                elif (self.appMode.get() == 2):
                    n = int(self.ciclosSpin.get())
                    treds = []
                    while(n > 0):
                        proc1_tred = threading.Thread(target=self.p1.compute())
                        treds.append(proc1_tred)
                        proc1_tred.start()

                        proc2_tred = threading.Thread(target=self.p2.compute())
                        treds.append(proc2_tred)
                        proc2_tred.start()

                        proc3_tred = threading.Thread(target=self.p3.compute())
                        treds.append(proc3_tred)
                        proc3_tred.start()

                        proc4_tred = threading.Thread(target=self.p4.compute())
                        treds.append(proc4_tred)
                        proc4_tred.start()

                        n -= 1

                    self.runnig = False

    def drawMem(self):
        memData = self.mainMem.getData()

        self.memBlock0000.config(state=tk.NORMAL)
        self.memBlock0000.delete("1.0", tk.END)
        self.memBlock0000.insert("1.0", memData[0][0])
        self.memBlock0000.config(state=tk.DISABLED)

        self.memBlock0001.config(state=tk.NORMAL)
        self.memBlock0001.delete("1.0", tk.END)
        self.memBlock0001.insert("1.0", memData[0][1])
        self.memBlock0001.config(state=tk.DISABLED)

        self.memBlock0010.config(state=tk.NORMAL)
        self.memBlock0010.delete("1.0", tk.END)
        self.memBlock0010.insert("1.0", memData[0][2])
        self.memBlock0010.config(state=tk.DISABLED)

        self.memBlock0011.config(state=tk.NORMAL)
        self.memBlock0011.delete("1.0", tk.END)
        self.memBlock0011.insert("1.0", memData[0][3])
        self.memBlock0011.config(state=tk.DISABLED)

        self.memBlock0100.config(state=tk.NORMAL)
        self.memBlock0100.delete("1.0", tk.END)
        self.memBlock0100.insert("1.0", memData[1][0])
        self.memBlock0100.config(state=tk.DISABLED)

        self.memBlock0101.config(state=tk.NORMAL)
        self.memBlock0101.delete("1.0", tk.END)
        self.memBlock0101.insert("1.0", memData[1][1])
        self.memBlock0101.config(state=tk.DISABLED)

        self.memBlock0110.config(state=tk.NORMAL)
        self.memBlock0110.delete("1.0", tk.END)
        self.memBlock0110.insert("1.0", memData[1][2])
        self.memBlock0110.config(state=tk.DISABLED)

        self.memBlock0111.config(state=tk.NORMAL)
        self.memBlock0111.delete("1.0", tk.END)
        self.memBlock0111.insert("1.0", memData[1][3])
        self.memBlock0111.config(state=tk.DISABLED)

        self.memBlock1000.config(state=tk.NORMAL)
        self.memBlock1000.delete("1.0", tk.END)
        self.memBlock1000.insert("1.0", memData[2][0])
        self.memBlock1000.config(state=tk.DISABLED)

        self.memBlock1001.config(state=tk.NORMAL)
        self.memBlock1001.delete("1.0", tk.END)
        self.memBlock1001.insert("1.0", memData[2][1])
        self.memBlock1001.config(state=tk.DISABLED)

        self.memBlock1010.config(state=tk.NORMAL)
        self.memBlock1010.delete("1.0", tk.END)
        self.memBlock1010.insert("1.0", memData[2][2])
        self.memBlock1010.config(state=tk.DISABLED)

        self.memBlock1011.config(state=tk.NORMAL)
        self.memBlock1011.delete("1.0", tk.END)
        self.memBlock1011.insert("1.0", memData[2][3])
        self.memBlock1011.config(state=tk.DISABLED)

        self.memBlock1100.config(state=tk.NORMAL)
        self.memBlock1100.delete("1.0", tk.END)
        self.memBlock1100.insert("1.0", memData[3][0])
        self.memBlock1100.config(state=tk.DISABLED)

        self.memBlock1101.config(state=tk.NORMAL)
        self.memBlock1101.delete("1.0", tk.END)
        self.memBlock1101.insert("1.0", memData[3][1])
        self.memBlock1101.config(state=tk.DISABLED)

        self.memBlock1110.config(state=tk.NORMAL)
        self.memBlock1110.delete("1.0", tk.END)
        self.memBlock1110.insert("1.0", memData[3][2])
        self.memBlock1110.config(state=tk.DISABLED)

        self.memBlock1111.config(state=tk.NORMAL)
        self.memBlock1111.delete("1.0", tk.END)
        self.memBlock1111.insert("1.0", memData[3][3])
        self.memBlock1111.config(state=tk.DISABLED)

    def drawUpdateCache(self, proc, ledir):
        cSet = int(ledir[-1])  # 111_1_
        block = int(ledir[1])  # 1_1_11
        if (proc == 1):
            coer = self.p1.controller.cache.get_EC(ledir)
            cDir = self.p1.controller.cache.cdata[cSet][block].getDir()
            cDato = self.p1.controller.cache.cdata[cSet][block].getData()
            cStri = 'Estado: '+coer+'\n'+'Direccion: '+cDir+'\n'+'Dato: '+cDato
            cStri += '\n'
        elif (proc == 2):
            coer = self.p2.controller.cache.get_EC(ledir)
            cDir = self.p2.controller.cache.cdata[cSet][block].getDir()
            cDato = self.p2.controller.cache.cdata[cSet][block].getData()
            cStri = 'Estado: '+coer+'\n'+'Direccion: '+cDir+'\n'+'Dato: '+cDato
            cStri += '\n'
        elif (proc == 3):
            coer = self.p3.controller.cache.get_EC(ledir)
            cDir = self.p3.controller.cache.cdata[cSet][block].getDir()
            cDato = self.p3.controller.cache.cdata[cSet][block].getData()
            cStri = 'Estado: '+coer+'\n'+'Direccion: '+cDir+'\n'+'Dato: '+cDato
            cStri += '\n'
        else:
            coer = self.p4.controller.cache.get_EC(ledir)
            cDir = self.p4.controller.cache.cdata[cSet][block].getDir()
            cDato = self.p4.controller.cache.cdata[cSet][block].getData()
            cStri = 'Estado: '+coer+'\n'+'Direccion: '+cDir+'\n'+'Dato: '+cDato
            cStri += '\n'

        if (proc == 1):
            if (cSet):  # 1_
                if (block):  # 11
                    self.p1bock4.config(state=tk.NORMAL)
                    self.p1bock4.delete("1.0", tk.END)
                    self.p1bock4.insert(tk.END, cStri)
                    self.p1bock4.config(state=tk.NORMAL)
                else:  # 10
                    self.p1bock3.config(state=tk.NORMAL)
                    self.p1bock3.delete("1.0", tk.END)
                    self.p1bock3.insert(tk.END, cStri)
                    self.p1bock3.config(state=tk.NORMAL)
            else:  # 0_
                if (block):  # 01
                    self.p1bock2.config(state=tk.NORMAL)
                    self.p1bock2.delete("1.0", tk.END)
                    self.p1bock2.insert(tk.END, cStri)
                    self.p1bock2.config(state=tk.NORMAL)
                else:  # 00
                    self.p1bock1.config(state=tk.NORMAL)
                    self.p1bock1.delete("1.0", tk.END)
                    self.p1bock1.insert(tk.END, cStri)
                    self.p1bock1.config(state=tk.NORMAL)
        elif (proc == 2):
            if (cSet):  # 1_
                if (block):  # 11
                    self.p2bock4.config(state=tk.NORMAL)
                    self.p2bock4.delete("1.0", tk.END)
                    self.p2bock4.insert(tk.END, cStri)
                    self.p2bock4.config(state=tk.NORMAL)
                else:  # 10
                    self.p2bock3.config(state=tk.NORMAL)
                    self.p2bock3.delete("1.0", tk.END)
                    self.p2bock3.insert(tk.END, cStri)
                    self.p2bock3.config(state=tk.NORMAL)
            else:  # 0_
                if (block):  # 01
                    self.p2bock2.config(state=tk.NORMAL)
                    self.p2bock2.delete("1.0", tk.END)
                    self.p2bock2.insert(tk.END, cStri)
                    self.p2bock2.config(state=tk.NORMAL)
                else:  # 00
                    self.p2bock1.config(state=tk.NORMAL)
                    self.p2bock1.delete("1.0", tk.END)
                    self.p2bock1.insert(tk.END, cStri)
                    self.p2bock1.config(state=tk.NORMAL)
        elif (proc == 3):
            if (cSet):  # 1_
                if (block):  # 11
                    self.p3bock4.config(state=tk.NORMAL)
                    self.p3bock4.delete("1.0", tk.END)
                    self.p3bock4.insert(tk.END, cStri)
                    self.p3bock4.config(state=tk.NORMAL)
                else:  # 10
                    self.p3bock3.config(state=tk.NORMAL)
                    self.p3bock3.delete("1.0", tk.END)
                    self.p3bock3.insert(tk.END, cStri)
                    self.p3bock3.config(state=tk.NORMAL)
            else:  # 0_
                if (block):  # 01
                    self.p3bock2.config(state=tk.NORMAL)
                    self.p3bock2.delete("1.0", tk.END)
                    self.p3bock2.insert(tk.END, cStri)
                    self.p3bock2.config(state=tk.NORMAL)
                else:  # 00
                    self.p3bock1.config(state=tk.NORMAL)
                    self.p3bock1.delete("1.0", tk.END)
                    self.p3bock1.insert(tk.END, cStri)
                    self.p3bock1.config(state=tk.NORMAL)
        else:
            if (cSet):  # 1_
                if (block):  # 11
                    self.p4bock4.config(state=tk.NORMAL)
                    self.p4bock4.delete("1.0", tk.END)
                    self.p4bock4.insert(tk.END, cStri)
                    self.p4bock4.config(state=tk.NORMAL)
                else:  # 10
                    self.p4bock3.config(state=tk.NORMAL)
                    self.p4bock3.delete("1.0", tk.END)
                    self.p4bock3.insert(tk.END, cStri)
                    self.p4bock3.config(state=tk.NORMAL)
            else:  # 0_
                if (block):  # 01
                    self.p4bock2.config(state=tk.NORMAL)
                    self.p4bock2.delete("1.0", tk.END)
                    self.p4bock2.insert(tk.END, cStri)
                    self.p4bock2.config(state=tk.NORMAL)
                else:  # 00
                    self.p4bock1.config(state=tk.NORMAL)
                    self.p4bock1.delete("1.0", tk.END)
                    self.p4bock1.insert(tk.END, cStri)
                    self.p4bock1.config(state=tk.NORMAL)

    def drawInst(self, proc, inst):
        if (proc == 1):
            self.instProc1.config(state=tk.NORMAL)
            self.instProc1.insert("1.0", inst+'\n')
            self.instProc1.config(state=tk.DISABLED)
        elif (proc == 2):
            self.instProc2.config(state=tk.NORMAL)
            self.instProc2.insert("1.0", inst+'\n')
            self.instProc2.config(state=tk.DISABLED)
        elif (proc == 3):
            self.instProc3.config(state=tk.NORMAL)
            self.instProc3.insert("1.0", inst+'\n')
            self.instProc3.config(state=tk.DISABLED)
        else:
            self.instProc4.config(state=tk.NORMAL)
            self.instProc4.insert("1.0", inst+'\n')
            self.instProc4.config(state=tk.DISABLED)

    def drawInitCache(self):
        cStri = 'Estado: \n'+'Direccion: \n'+'Dato: \n'
        self.p1bock1.config(state=tk.NORMAL)
        self.p1bock1.delete("1.0", tk.END)
        self.p1bock1.insert(tk.END, cStri)
        self.p1bock1.config(state=tk.NORMAL)

        self.p1bock2.config(state=tk.NORMAL)
        self.p1bock2.delete("1.0", tk.END)
        self.p1bock2.insert(tk.END, cStri)
        self.p1bock2.config(state=tk.NORMAL)

        self.p1bock3.config(state=tk.NORMAL)
        self.p1bock3.delete("1.0", tk.END)
        self.p1bock3.insert(tk.END, cStri)
        self.p1bock3.config(state=tk.NORMAL)

        self.p1bock4.config(state=tk.NORMAL)
        self.p1bock4.delete("1.0", tk.END)
        self.p1bock4.insert(tk.END, cStri)
        self.p1bock4.config(state=tk.NORMAL)

        self.p2bock1.config(state=tk.NORMAL)
        self.p2bock1.delete("1.0", tk.END)
        self.p2bock1.insert(tk.END, cStri)
        self.p2bock1.config(state=tk.NORMAL)

        self.p2bock2.config(state=tk.NORMAL)
        self.p2bock2.delete("1.0", tk.END)
        self.p2bock2.insert(tk.END, cStri)
        self.p2bock2.config(state=tk.NORMAL)

        self.p2bock3.config(state=tk.NORMAL)
        self.p2bock3.delete("1.0", tk.END)
        self.p2bock3.insert(tk.END, cStri)
        self.p2bock3.config(state=tk.NORMAL)

        self.p2bock4.config(state=tk.NORMAL)
        self.p2bock4.delete("1.0", tk.END)
        self.p2bock4.insert(tk.END, cStri)
        self.p2bock4.config(state=tk.NORMAL)

        self.p3bock1.config(state=tk.NORMAL)
        self.p3bock1.delete("1.0", tk.END)
        self.p3bock1.insert(tk.END, cStri)
        self.p3bock1.config(state=tk.NORMAL)

        self.p3bock2.config(state=tk.NORMAL)
        self.p3bock2.delete("1.0", tk.END)
        self.p3bock2.insert(tk.END, cStri)
        self.p3bock2.config(state=tk.NORMAL)

        self.p3bock3.config(state=tk.NORMAL)
        self.p3bock3.delete("1.0", tk.END)
        self.p3bock3.insert(tk.END, cStri)
        self.p3bock3.config(state=tk.NORMAL)

        self.p3bock4.config(state=tk.NORMAL)
        self.p3bock4.delete("1.0", tk.END)
        self.p3bock4.insert(tk.END, cStri)
        self.p3bock4.config(state=tk.NORMAL)

        self.p4bock1.config(state=tk.NORMAL)
        self.p4bock1.delete("1.0", tk.END)
        self.p4bock1.insert(tk.END, cStri)
        self.p4bock1.config(state=tk.NORMAL)

        self.p4bock2.config(state=tk.NORMAL)
        self.p4bock2.delete("1.0", tk.END)
        self.p4bock2.insert(tk.END, cStri)
        self.p4bock2.config(state=tk.NORMAL)

        self.p4bock3.config(state=tk.NORMAL)
        self.p4bock3.delete("1.0", tk.END)
        self.p4bock3.insert(tk.END, cStri)
        self.p4bock3.config(state=tk.NORMAL)

        self.p4bock4.config(state=tk.NORMAL)
        self.p4bock4.delete("1.0", tk.END)
        self.p4bock4.insert(tk.END, cStri)
        self.p4bock4.config(state=tk.NORMAL)
