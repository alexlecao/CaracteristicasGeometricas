# Mudei a Primeira Linha do Código

import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class MainProgram:
    def __init__(self, master):
        self.root = master
        self.root.title('Características Geométricas')
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(master, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(master, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.EntryFont = Font(family='Arial', size=20)
        self.ResultFont = Font(family='Arial', size=16)
        self.WarningFont = Font(size=50)

        self.WindowsZoom = 125



        self.Register = self.MainSpace.register(self.validate)

        self.root.bind('<Control-Key-1>', self.tShape)
        self.root.bind('<Control-Key-2>', self.LShape)
        self.root.bind('<Control-Key-3>', self.uShape)
        self.root.bind('<Control-Key-4>', self.cShape)
        self.root.bind('<Control-Key-5>', self.iShape)
        self.root.bind('<Control-Key-6>', self.RomanIShape)

        self.SideFramePacking()     


    def SideFramePacking(self):
        tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
        self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.tShape)
        self.tButton.image = tButtonImage
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        LButtonImage = self.CreateImage(r'Images\Buttons\LButton.png')
        self.LButton = tk.Button(self.SideFrame, image=LButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.LShape)
        self.LButton.image = LButtonImage
        self.LButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        uButtonImage = self.CreateImage(r'Images\Buttons\uButton.png')
        self.uButton = tk.Button(self.SideFrame, image=uButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.uShape)
        self.uButton.image = uButtonImage
        self.uButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        cButtonImage = self.CreateImage(r'Images\Buttons\cButton.png')
        self.cButton = tk.Button(self.SideFrame, image=cButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.cShape)
        self.cButton.image = cButtonImage
        self.cButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        iButtonImage = self.CreateImage(r'Images\Buttons\iButton.png')
        self.iButton = tk.Button(self.SideFrame, image=iButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.iShape)
        self.iButton.image = iButtonImage
        self.iButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        RomanIButtonImage = self.CreateImage(r'Images\Buttons\RomanIButton.png')
        self.RomanIButton = tk.Button(self.SideFrame, image=RomanIButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.RomanIShape)
        self.RomanIButton.image = RomanIButtonImage
        self.RomanIButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


    def ClearMainSpace(self):
        for widget in self.MainSpace.winfo_children():
            widget.destroy()


    def CreateImage(self, path):
        ImageFile = Image.open(path)
        ImageWidth, ImageHeight = ImageFile.size
        
        if self.WindowsZoom == 100:
            xSize = ImageWidth
            ySize = ImageHeight

        elif self.WindowsZoom == 125:
            xSize = ImageWidth - (ImageWidth * 0.25)
            ySize = ImageHeight - (ImageHeight * 0.25)

        TkImage = ImageTk.PhotoImage(ImageFile.resize((int(xSize), int(ySize)), Image.ANTIALIAS))
        
        return TkImage


    def validate(self, value, action):
        if action == '1':
            if value:
                try:
                    float(value)
                    return True
                    
                except ValueError:
                    return False
            
            else:
                return False
        else:
            return True


    def tShape(self, event=None):

        def Calculate(event=None):
            x = float(TopEntry.get())
            b = float(LeftEntry.get())
            y = float(RightEntry.get())
            z = float(BottomEntry.get())

            self.ClearMainSpace()

            Ycg = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)

            Iz = (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - Ycg)) ** 2)) + (((z * (y ** 3)) / (12)) + (y * z * ((Ycg - (y / 2)) ** 2)))

            if Ycg < y or Ycg == y:
                Scg = (Ycg * z * (Ycg / 2))
            
            else:
                Scg = x * (y + b - Ycg) * ((y + b - Ycg) / 2)
                

            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)

            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            ResultFrame = tk.Frame(LeftFrame, bg='#dbdbdb')
            ResultFrame.pack(side=tk.TOP)

            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=10, sticky='e')

            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=10, sticky='e')

            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=10, sticky='e')

            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            CanvasWidth = 694
            CanvasHeight = 844

            # Show Length Values On T Shape

            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')
            ValueFrame.pack(padx=(0, 400))

            xLabel = tk.Label(ValueFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            xLabel.pack(side=tk.TOP, pady=(50, 5))
            
            bLabel = tk.Label(ValueFrame, text=f'b = {b} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            bLabel.pack(side=tk.LEFT, anchor='ne', pady=100)

            yLabel = tk.Label(ValueFrame, text=f'y = {y} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            yLabel.pack(side=tk.RIGHT, anchor='w', pady=100)

            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()
            
            zLabel = tk.Label(ValueFrame, text=f'z = {z} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            zLabel.pack(side=tk.BOTTOM)

            self.ImageList = []

            justTImage = self.CreateImage('Images/Shapes/tValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=justTImage)
            self.ImageList.append(justTImage)

            # DotHeight = ((height-100) / y - 1) * 100

            # DotHeight = Ycg * CanvasHeight  / (y + b)
            # print(f'DotHeight: {DotHeight}')

            if Ycg < y:
                DotHeight = CanvasHeight - 650
                
            elif Ycg > y:
                DotHeight = CanvasHeight - 720

            elif Ycg == y:
                DotHeight = CanvasHeight - 496
                
            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 158
            y1 = DotHeight
            x2 = x1 + 9 # 9 = largura em pixel do retângulo
            y2 = CanvasHeight - 50

            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)

            ShapeCanvas.create_text(153, 844 - 50, text='Ycg', font=self.ResultFont, fill='#303030', anchor='se')


        def Discard():
            TopEntry.delete(0, tk.END)
            RightEntry.delete(0, tk.END)
            LeftEntry.delete(0, tk.END)
            BottomEntry.delete(0, tk.END)


        self.ClearMainSpace()
        
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        TopEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        TopEntry['validatecommand'] = (self.Register, '%P', '%d')
        TopEntry.pack(side=tk.TOP, pady=(50, 25)) 

        RightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        RightEntry['validatecommand'] = (self.Register, '%P', '%d')
        RightEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        LeftEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        LeftEntry['validatecommand'] = (self.Register, '%P', '%d')
        LeftEntry.pack(side=tk.LEFT, anchor='n', pady=75, padx=30)

        self.tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        tShapeLabel = tk.Label(DataFrame, image=self.tShapeImage, bd=0)
        tShapeLabel.image = self.tShapeImage
        tShapeLabel.pack()

        BottomEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        BottomEntry['validatecommand'] = (self.Register, '%P', '%d')
        BottomEntry.pack(side=tk.BOTTOM, pady=(25, 50))
        
        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


    def LShape(self, event=None):
        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        self.LShapeImage = self.CreateImage('Images/Shapes/LShape.png')
        LShapeLabel = tk.Label(DataFrame, image=self.LShapeImage, bd=0)
        LShapeLabel.image = self.LShapeImage
        LShapeLabel.pack()

        WarningLabel = tk.Label(DataFrame, text='EM BREVE', font=self.WarningFont, fg='#8c8c8c', bg='#dbdbdb')
        WarningLabel.pack()


    def uShape(self, event=None):
        def Calculate(event=None):
            x = float(xEntry.get())  
            y = float(yEntry.get())
            a = float(a1Entry.get())
            h = float(hEntry.get())

            Ycg = ((2 * (a * y * (y / 2))) + (h * x * (x / 2))) / ((2 * (a * y)) + (x * h))
         
            Iz = (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - Ycg) ** 2)))) + ((((h) * (x ** 3)) / (12)) + (x * h * ((Ycg - (x / 2)) ** 2)))
    
            Scg = (((y - Ycg) * (a + h + a)) - ((y - Ycg) * (h))) * ((y - Ycg) / 2)

            print(f'x: {x}')
            print(f'y: {y}')
            print(f'a: {a}')
            print(f'h: {h}')
            print(f'Ycg: {Ycg}')
            print(f'Iz: {Iz}')
            print(f'Scg: {Scg}')

            self.ClearMainSpace()

            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)

            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            ResultFrame = tk.Frame(LeftFrame, bg='#dbdbdb')
            ResultFrame.pack(side=tk.TOP)

            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=10, sticky='e')

            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=10, sticky='e')

            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=10, sticky='e')

            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            CanvasWidth = 702
            CanvasHeight = 840

            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')
            ValueFrame.pack(expand=True, padx=(0, 400))

            TopLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            TopLabelFrame.pack(side=tk.TOP)

            a1Label = tk.Label(TopLabelFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            a1Label.pack(side=tk.LEFT, padx=(0, 170))

            a2Label = tk.Label(TopLabelFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            a2Label.pack(side=tk.RIGHT, padx=(170, 0))
            
            YcgL = tk.Label(ValueFrame, text='Ycg', font=self.ResultFont, bg='#dbdbdb', fg='#121212')
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=70)

            RightLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            RightLabelFrame.pack(side=tk.RIGHT, anchor='w', fill=tk.Y)

            yLabel = tk.Label(RightLabelFrame, text=f'y = {y - x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            yLabel.pack(anchor='w', pady=(350, 0))

            xLabel = tk.Label(RightLabelFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            xLabel.pack(side=tk.BOTTOM, anchor='w', pady=(0, 150))

            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()

            hLabel = tk.Label(ValueFrame, text=f'h = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            hLabel.pack(side=tk.BOTTOM)

            self.ImageList = []

            uValuesImage = self.CreateImage('Images/Shapes/uValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=uValuesImage)
            self.ImageList.append(uValuesImage)

            DotImage = self.CreateImage('Images/Shapes/dot.png')

            if Ycg < x:
                DotHeight = CanvasHeight - 145
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif Ycg > x:
                DotHeight = CanvasHeight - 350
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif Ycg == x:
                DotHeight = CanvasHeight - 190
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            self.ImageList.append(DotImage)

            x1 = 15
            y1 = DotHeight
            x2 = x1 + 9
            y2 = 799

            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def Discard():
            a1Entry.delete(0, tk.END)
            a2Entry.delete(0, tk.END)
            hEntry.delete(0, tk.END)
            xEntry.delete(0, tk.END)
            yEntry.delete(0, tk.END)

        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        TopEntryFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        TopEntryFrame.pack(side=tk.TOP, pady=(50, 25))

        a1Entry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        a1Entry['validatecommand'] = (self.Register, '%P', '%d')
        a1Entry.pack(side=tk.LEFT, padx=30)

        a2Entry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        a2Entry['validatecommand'] = (self.Register, '%P', '%d')
        a2Entry.pack(side=tk.RIGHT, padx=30)        

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        xEntry['validatecommand'] = (self.Register, '%P', '%d')
        xEntry.pack(side=tk.LEFT, anchor='s', pady=(0, 140), padx=30)

        yEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        yEntry['validatecommand'] = (self.Register, '%P', '%d')
        yEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        self.uShapeImage = self.CreateImage('Images/Shapes/uShape.png')
        uShapeLabel = tk.Label(DataFrame, image=self.uShapeImage, bd=0)
        uShapeLabel.image = self.uShapeImage
        uShapeLabel.pack()

        hEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        hEntry['validatecommand'] = (self.Register, '%P', '%d')
        hEntry.pack(pady=(30, 0))

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


    def cShape(self, event=None):
        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        self.cShapeImage = self.CreateImage('Images/Shapes/cShape.png')
        cShapeLabel = tk.Label(DataFrame, image=self.cShapeImage, bd=0)
        cShapeLabel.image = self.cShapeImage
        cShapeLabel.pack()

        WarningLabel = tk.Label(DataFrame, text='EM BREVE', font=self.WarningFont, fg='#8c8c8c', bg='#dbdbdb')
        WarningLabel.pack()


    def iShape(self, event=None):
        def Calculate(event=None):
            h = float(HeightEntry.get())
            w = float(WidthEntry.get())

            Ycg = h / 2
            Iz = (w * (h ** 3)) / 12
            Scg = (w * Ycg * (Ycg / 2))

            print(f'Height {str(h)}')
            print(f'Width {str(w)}')
            print(f'Ycg {str(Ycg)}')
            print(f'Iz {str(Iz)}')
            print(f'Scg {str(Scg)}')

            self.ClearMainSpace()

            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)

            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            ResultFrame = tk.Frame(LeftFrame, bg='#dbdbdb')
            ResultFrame.pack(side=tk.TOP)
            
            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=10, sticky='e')

            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=10, sticky='e')

            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=10, sticky='e')

            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        
            CanvasWidth = 265
            CanvasHeight = 819

            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')
            ValueFrame.pack(expand=True, padx=(0, 400))

            wLabel = tk.Label(ValueFrame, text=f'x = {w} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            wLabel.pack(side=tk.TOP)

            hLabel = tk.Label(ValueFrame, text=f'x = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            hLabel.pack(side=tk.RIGHT)

            YcgL = tk.Label(ValueFrame, text='Ycg', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=20)

            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()            

            self.ImageList = []

            iValuesImage = self.CreateImage('Images/Shapes/iValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=iValuesImage)
            self.ImageList.append(iValuesImage)

            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=DotImage)

            self.ImageList.append(DotImage)

            x1 = 18
            y1 = CanvasHeight / 2
            x2 = x1 + 9
            y2 = 796

            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def Discard():
            WidthEntry.delete(0, tk.END)
            HeightEntry.delete(0, tk.END)


        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        WidthEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        WidthEntry['validatecommand'] = (self.Register, '%P', '%d')
        WidthEntry.pack(side=tk.TOP, pady=(50, 25))

        HeightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        HeightEntry['validatecommand'] = (self.Register, '%P', '%d')
        HeightEntry.pack(side=tk.RIGHT, anchor='n', pady=300, padx=30)

        self.iShapeImage = self.CreateImage('Images/Shapes/iShape.png')
        iShapeLabel = tk.Label(DataFrame, image=self.iShapeImage, bd=0)
        iShapeLabel.image = self.iShapeImage
        iShapeLabel.pack(padx=(360, 0))

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


    def RomanIShape(self, event=None):
        def Calculate(event=None):
            x = float(xEntry.get())
            y = float(yEntry.get())
            a = float(aEntry.get())
            d = float(dEntry.get())
            h = float(hEntry.get())
            x = float(xEntry.get())
            r = float(rEntry.get())

            Ycg = ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2)))) / ((a * r) + (d * h) + (y * x))
            Iz = (((r * (a ** 3)) / (12)) + ((a * r * (((Ycg - (a / 2)) ** 2))))) + (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - (Ycg)) ** 2))) + (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - Ycg) ** 2)))
            
            if Ycg == a:
                print('Primeira Fórmula')
                Scg = a * r * (a / 2)

            elif Ycg == (a + h):
                print('Segunda Fórmula')
                Scg = y * x * (y / 2)

            elif Ycg < (a + h) and Ycg > a:
                print('Terceira Fórmula')
                Scg = (a * r * (Ycg - (a / 2))) + (d * (Ycg - a) * ((Ycg - a) / 2))

            self.ClearMainSpace()

            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)

            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            ResultFrame = tk.Frame(LeftFrame, bg='#dbdbdb')
            ResultFrame.pack(side=tk.TOP)

            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=10, sticky='e')

            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=10, sticky='e')

            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=10, sticky='e')

            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            CanvasWidth = 496
            CanvasHeight = 820

            # TODO: Show Length Values on Roman I Shape

            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')
            ValueFrame.pack(expand=True, padx=(0, 400))

            xLabel = tk.Label(ValueFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            xLabel.pack(side=tk.TOP, pady=(50, 5))

            aLabel = tk.Label(ValueFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            aLabel.pack(side=tk.LEFT, pady=(0, 40))

            RightValueFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            RightValueFrame.pack(side=tk.RIGHT, fill=tk.Y)

            yLabel = tk.Label(RightValueFrame, text=f'y = {y} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            yLabel.pack(side=tk.TOP, anchor='w', pady=(100, 0))

            hLabel = tk.Label(RightValueFrame, text=f'h = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            hLabel.pack(anchor='w', pady=(290, 0))

            dLabel = tk.Label(RightValueFrame, text=f'd = {d} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            dLabel.pack(side=tk.BOTTOM, anchor='w', pady=(0, 120))

            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()

            rLabel = tk.Label(ValueFrame, text=f'r = {r} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            rLabel.pack()

            self.ImageList = []

            RomanIValuesImage = self.CreateImage('Images/Shapes/RomanIValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=RomanIValuesImage)
            self.ImageList.append(RomanIValuesImage)

            if Ycg > (h + d):
                DotHeight = CanvasHeight - 708
                
            elif Ycg == (h + d):
                DotHeight = CanvasHeight - 632
            
            elif ((y + h + d) / 2) < Ycg < (h + d):
                DotHeight = CanvasHeight - 522

            elif Ycg == ((y + h + d) / 2):
                DotHeight = CanvasHeight - 411

            elif Ycg == ((h + d) / 2):
                DotHeight = CanvasHeight - 336

            elif d < Ycg < ((y + d + h) / 2):
                DotHeight = CanvasHeight - 299
            
            elif Ycg == d:
                DotHeight = CanvasHeight - 189

            elif Ycg < d:
                DotHeight = CanvasHeight - 94

            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 283
            y1 = DotHeight
            x2 = x1 + 9
            y2 = CanvasHeight - 37

            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            ShapeCanvas.create_text(x2 + 10, y2, text='Ycg', font=self.ResultFont, fill='#303030', anchor='sw')

        def Discard():
            xEntry.delete(0, tk.END)
            yEntry.delete(0, tk.END)
            aEntry.delete(0, tk.END)
            dEntry.delete(0, tk.END)
            hEntry.delete(0, tk.END)
            rEntry.delete(0, tk.END)

        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        xEntry['validatecommand'] = (self.Register, '%P', '%d')
        xEntry.pack(side=tk.TOP, pady=(50, 25))

        LeftFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        LeftFrame.pack(side=tk.LEFT, anchor='s', pady=50, padx=30)

        yEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        yEntry['validatecommand'] = (self.Register, '%P', '%d')
        yEntry.pack(side=tk.TOP, pady=(0, 245))

        aEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        aEntry['validatecommand'] = (self.Register, '%P', '%d')
        aEntry.pack(pady=(0, 160))

        dEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        dEntry['validatecommand'] = (self.Register, '%P', '%d')
        dEntry.pack(side=tk.BOTTOM, pady=(0, 100))

        hEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        hEntry['validatecommand'] = (self.Register, '%P', '%d')
        hEntry.pack(side=tk.RIGHT, anchor='n', pady=325, padx=30)

        self.RomanIShapeImage = self.CreateImage('Images/Shapes/RomanIShape.png')
        RomanIShapeLabel = tk.Label(DataFrame, image=self.RomanIShapeImage, bd=0)
        RomanIShapeLabel.image = self.RomanIShapeImage
        RomanIShapeLabel.pack()

        rEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        rEntry['validatecommand'] = (self.Register, '%P', '%d')
        rEntry.pack(pady=(20, 0))

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
