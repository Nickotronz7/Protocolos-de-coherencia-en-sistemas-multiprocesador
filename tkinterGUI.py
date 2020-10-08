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

        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Separadores
            # Verticales
        self.vs1 = ttk.Separator(self.controlFrame, orient=tk.VERTICAL)
        self.vs1.grid(row=1, column=1, sticky='ns')
            # Horizontales

        # Etiquetas

        self.controlLabel = tk.Label(self.controlFrame, text='Control')
        self.controlLabel.grid(row=0, column=1)

        self.modoLabel = tk.Label(self.modeFrame, text='Modo')
        self.modoLabel.grid()

        self.instMLabel = tk.Label(self, text='Instruccion Manual')

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
        self.manualInstTextBox = tk.Entry(
            self.manualInstFrame,
            state=tk.DISABLED
        )
        self.manualInstTextBox.grid(row=0, column=1)

        # CheckBox
        self.checkManualInst = tk.Checkbutton(
            self.manualInstFrame,
            text='Instruccion Manual',
            variable=self.checkBox_value,
            command=self.checkBox_clicked
        )
        self.checkManualInst.grid(row=0, column=0)

    def checkBox_clicked(self):
        self.checkBox_value = not self.checkBox_value
        if(self.checkBox_value):
            self.manualInstTextBox['state'] = tk.NORMAL
        else:
            self.manualInstTextBox['state'] = tk.DISABLED

    def getSelected(self):
        if (self.appMode.get() == 2):
            self.ciclosSpin['state'] = 'readonly'
        else:
            self.ciclosSpin['state'] = tk.DISABLED
