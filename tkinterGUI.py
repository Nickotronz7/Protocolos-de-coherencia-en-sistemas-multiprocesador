import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.appMode = tk.IntVar()
        self.appMode.set(0)
        self.checkBox_value = tk.BooleanVar(self)
        self.checkBox_value.set(False)

        # Frames
        self.controlFrame = tk.Frame(self)
        self.controlFrame.grid(row=0, column=0)

        self.modeFrame = tk.Frame(self.controlFrame)
        self.modeFrame.grid(row=1, column=0)

        self.controlButtonsFrame = tk.Frame(self.controlFrame)
        self.controlButtonsFrame.grid(row=1, column=2)

        self.manualInstFrame = tk.Frame(self.controlButtonsFrame)
        self.manualInstFrame.grid(row=2, column=0)

        self.upperButtonFrame = tk.Frame(self.controlButtonsFrame)
        self.upperButtonFrame.grid(row=0, column=0)

        self.lowerButtonFrame = tk.Frame(self.controlButtonsFrame)
        self.lowerButtonFrame.grid(row=1, column=0)

        self.instrucctionFrame = tk.Frame(self)
        self.instrucctionFrame.grid(row=2, column=0)

        self.instrucctionBlockFrame = tk.Frame(self.instrucctionFrame)
        self.instrucctionBlockFrame.grid(row=1, column=0)

        self.memFrame = tk.Frame(self)
        self.memFrame.grid(row=0, column=2, rowspan=2)

        self.memBlockFrame = tk.Frame(self.memFrame)
        self.memBlockFrame.grid(row=1, rowspan=2)

        self.cacheFrame = tk.Frame(self)
        self.cacheFrame.grid(row=4)

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
        self.hs2.grid(row=3, column=0, sticky='we', pady=2, columnspan=3)

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
        self.cacheLabel.grid(row=0)

        self.p1cacheLabel = tk.Label(self.p1CacheFrame, text='P1')
        self.p2cacheLabel = tk.Label(self.p2CacheFrame, text='P2')
        self.p3cacheLabel = tk.Label(self.p3CacheFrame, text='P3')
        self.p4cacheLabel = tk.Label(self.p4CacheFrame, text='P4')
        self.p1cacheLabel.grid(row=0)
        self.p2cacheLabel.grid(row=0)
        self.p3cacheLabel.grid(row=0)
        self.p4cacheLabel.grid(row=0)

        # Botones
        self.initButton = tk.Button(
            self.upperButtonFrame,
            text='Iniciar'
        )
        self.initButton.grid(row=0, column=0)

        self.resetButton = tk.Button(
            self.upperButtonFrame,
            text='Reset'
        )
        self.resetButton.grid(row=0, column=1)

        self.nextButton = tk.Button(
            self.lowerButtonFrame,
            text='Siguiente'
        )
        self.nextButton.grid(row=0, column=0)

        self.playButton = tk.Button(
            self.lowerButtonFrame,
            text='Play'
        )
        self.playButton.grid(row=0, column=1)

        self.pauseButton = tk.Button(
            self.lowerButtonFrame,
            text='Pausa'
        )
        self.pauseButton.grid(row=0, column=2)

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

        # TextBox
        self.manualInstTextBoxDir = tk.Entry(
            self.manualInstFrame,
            state=tk.DISABLED,
            width=5
        )
        self.manualInstTextBoxDir.grid(row=0, column=2, padx=2)

        self.manualInstTextBoxData = tk.Entry(
            self.manualInstFrame,
            state=tk.DISABLED,
            width=5
        )
        self.manualInstTextBoxData.grid(row=0, column=3, padx=2)

        self.instProc1 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc1.grid(row=1, column=0, padx=2)

        self.instProc2 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc2.grid(row=1, column=1, padx=2)

        self.instProc3 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc3.grid(row=1, column=2, padx=2)

        self.instProc4 = tk.Text(
            self.instrucctionBlockFrame, width=20, height=10)
        self.instProc4.grid(row=1, column=3, padx=2)

        # 0000
        self.memBlock0000 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0000.grid(row=2, column=1, padx=2, pady=2)

        self.memBlock0001 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0001.grid(row=2, column=2, padx=2, pady=2)

        self.memBlock0010 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0010.grid(row=2, column=3, padx=2, pady=2)

        self.memBlock0011 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0011.grid(row=2, column=4, padx=2, pady=2)

        # 0100
        self.memBlock0100 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0100.grid(row=3, column=1, padx=2, pady=2)

        self.memBlock0101 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0101.grid(row=3, column=2, padx=2, pady=2)

        self.memBlock0110 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0110.grid(row=3, column=3, padx=2, pady=2)

        self.memBlock0111 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock0111.grid(row=3, column=4, padx=2, pady=2)

        # 1000
        self.memBlock1000 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1000.grid(row=4, column=1, padx=2, pady=2)

        self.memBlock1001 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1001.grid(row=4, column=2, padx=2, pady=2)

        self.memBlock1010 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1010.grid(row=4, column=3, padx=2, pady=2)

        self.memBlock1011 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1011.grid(row=4, column=4, padx=2, pady=2)

        # 1100
        self.memBlock1100 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1100.grid(row=5, column=1, padx=2, pady=2)

        self.memBlock1101 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1101.grid(row=5, column=2, padx=2, pady=2)

        self.memBlock1110 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1110.grid(row=5, column=3, padx=2, pady=2)

        self.memBlock1111 = tk.Text(self.memBlockFrame, height=1, width=5)
        self.memBlock1111.grid(row=5, column=4, padx=2, pady=2)

        self.p1bock1 = tk.Text(self.p1CacheFrame, width=6, height=4)
        self.p1bock2 = tk.Text(self.p1CacheFrame, width=6, height=4)
        self.p1bock3 = tk.Text(self.p1CacheFrame, width=6, height=4)
        self.p1bock4 = tk.Text(self.p1CacheFrame, width=6, height=4)
        self.p1bock1.grid(row=1)
        self.p1bock2.grid(row=2)
        self.p1bock3.grid(row=3)
        self.p1bock4.grid(row=4)

        self.p2bock1 = tk.Text(self.p2CacheFrame, width=6, height=4)
        self.p2bock2 = tk.Text(self.p2CacheFrame, width=6, height=4)
        self.p2bock3 = tk.Text(self.p2CacheFrame, width=6, height=4)
        self.p2bock4 = tk.Text(self.p2CacheFrame, width=6, height=4)
        self.p2bock1.grid(row=1)
        self.p2bock2.grid(row=2)
        self.p2bock3.grid(row=3)
        self.p2bock4.grid(row=4)

        self.p3bock1 = tk.Text(self.p3CacheFrame, width=6, height=4)
        self.p3bock2 = tk.Text(self.p3CacheFrame, width=6, height=4)
        self.p3bock3 = tk.Text(self.p3CacheFrame, width=6, height=4)
        self.p3bock4 = tk.Text(self.p3CacheFrame, width=6, height=4)
        self.p3bock1.grid(row=1)
        self.p3bock2.grid(row=2)
        self.p3bock3.grid(row=3)
        self.p3bock4.grid(row=4)

        self.p4bock1 = tk.Text(self.p4CacheFrame, width=6, height=4)
        self.p4bock2 = tk.Text(self.p4CacheFrame, width=6, height=4)
        self.p4bock3 = tk.Text(self.p4CacheFrame, width=6, height=4)
        self.p4bock4 = tk.Text(self.p4CacheFrame, width=6, height=4)
        self.p4bock1.grid(row=1)
        self.p4bock2.grid(row=2)
        self.p4bock3.grid(row=3)
        self.p4bock4.grid(row=4)

        # DropDown Menu
        self.instList = ['CALC', 'READ', 'WRITE']
        self.instVar = tk.StringVar(self)
        self.instVar.trace_add('write', self.boxEnable)
        self.instVar.set(self.instList[0])
        self.dropdown = tk.OptionMenu(
            self.manualInstFrame, self.instVar, *self.instList)
        self.dropdown.configure(state=tk.DISABLED)
        self.dropdown.grid(row=0, column=1)

        # CheckBox
        self.checkManualInst = tk.Checkbutton(
            self.manualInstFrame,
            text='Instruccion Manual',
            variable=self.checkBox_value,
            command=self.checkBox_clicked
        )
        self.checkManualInst.grid(row=0, column=0)

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
            self.dropdown.configure(state=tk.DISABLED)
            self.manualInstTextBoxDir['state'] = tk.DISABLED
            self.manualInstTextBoxData['state'] = tk.DISABLED

    def getSelected(self):
        if (self.appMode.get() == 2):
            self.ciclosSpin['state'] = 'readonly'
        else:
            self.ciclosSpin['state'] = tk.DISABLED
