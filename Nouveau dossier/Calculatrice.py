
from tkinter import *

class Calculatrice():
    def __init__(self):
        self.nombre1 = 0
        self.nombre2 = 0
        self.nombrefin = 0
        self.entree = StringVar()
        self.texte = ""
        self.signe = ""
        self.entree.set("AKWABA")

    def init(self):
        self.nombre1 = 0
        self.nombre2 = 0
        self.nombrefin = 0
        self.texte = ""
        self.signe = ""

    def afficher_Nb(self):
        self.entree.set(self.texte) 

    def operation(self):
        try :
            if "+" in self.texte:
                self.Plus()
            elif "-" in self.texte:
                self.Sous()
            elif "X" in self.texte:
                self.Mult()
            elif "/" in self.texte:
                self.Div()
        except:
            self.entree.set("ERREUR")
            self.init()

    def Plus(self):     
        Nbre = self.texte.split("+")
        self.nombre1 = float(Nbre[0])
        self.nombre2 = float(Nbre[1])
        self.nombrefin = self.nombre1 + self.nombre2
        self.entree.set(str(self.nombrefin))
        self.init()

    def Sous(self): 
        Nbre = self.texte.split("-")
        self.nombre1 = float(Nbre[0])
        self.nombre2 = float(Nbre[1])
        self.nombrefin = self.nombre1 - self.nombre2
        self.entree.set(str(self.nombrefin))
        self.init()

    def Mult(self): 
        Nbre = self.texte.split("X")
        self.nombre1 = float(Nbre[0])
        self.nombre2 = float(Nbre[1])
        self.nombrefin = self.nombre1 * self.nombre2
        self.entree.set(str(self.nombrefin))
        self.init()   

    def Div(self): 
        Nbre = self.texte.split("/")
        self.nombre1 = float(Nbre[0])
        self.nombre2 = float(Nbre[1])
        self.nombrefin = self.nombre1 / self.nombre2
        self.entree.set(str(self.nombrefin))
        self.init() 

    def Percent(self): 
        Nbre = self.texte.split("%")
        self.nombre1 = float(Nbre[0])
        self.nombrefin = self.nombre1 / 100
        self.entree.set(str(self.nombrefin))
        self.init()   
               


def Boutton1 (): 
    calculatrice.texte += "1"
    calculatrice.entree.set(calculatrice.texte)

def Boutton2 (): 
    calculatrice.texte += "2"
    calculatrice.entree.set(calculatrice.texte)

def Boutton3(): 
    calculatrice.texte += "3"
    calculatrice.entree.set(calculatrice.texte)

def Boutton4(): 
    calculatrice.texte += "4"
    calculatrice.entree.set(calculatrice.texte)

def Boutton5(): 
    calculatrice.texte += "5"
    calculatrice.entree.set(calculatrice.texte)

def Boutton6(): 
    calculatrice.texte += "6"
    calculatrice.entree.set(calculatrice.texte)

def Boutton7(): 
    calculatrice.texte += "7"
    calculatrice.entree.set(calculatrice.texte)

def Boutton8(): 
    calculatrice.texte += "8"
    calculatrice.entree.set(calculatrice.texte)

def Boutton9(): 
    calculatrice.texte += "9"
    calculatrice.entree.set(calculatrice.texte)

def Boutton0(): 
    calculatrice.texte += "0"
    calculatrice.entree.set(calculatrice.texte)

def BouttonF(): 
    calculatrice.texte += "."
    calculatrice.entree.set(calculatrice.texte)

def BouttonP(): 
    calculatrice.texte += "+"
    calculatrice.entree.set(calculatrice.texte)

def BouttonS(): 
    calculatrice.texte += "-"
    calculatrice.entree.set(calculatrice.texte)

def BouttonM(): 
    calculatrice.texte += "X"
    calculatrice.entree.set(calculatrice.texte)

def BouttonD(): 
    calculatrice.texte += "/"
    calculatrice.entree.set(calculatrice.texte)

def BouttonE(): 
    calculatrice.operation()

def BouttonAC(): 
    calculatrice.entree.set("")   
    calculatrice.init()

def BouttonT(): 
    calculatrice.texte += "/100"  
    calculatrice.entree.set(calculatrice.texte,calculatrice.operation())    

fen = Tk()
fen.geometry("190x250")
fen.title("calculatrice v1.1")
fen["bg"]= "Black"
fen["relief"] = "raised"   


calculatrice = Calculatrice()


ECRAN = Entry(fen, width=26, textvariable=calculatrice.entree, bg ="white", fg="black", relief=SUNKEN, bd=7).place(x=9, y=8)


B1 = Button(fen,text="1", command=Boutton1, width=3, height=2, bg="grey", fg="white").place(x=10, y=40)
B2 = Button(fen,text="2", command=Boutton2, width=3, height=2, bg="grey", fg="white").place(x=50, y=40)
B3 = Button(fen,text="3", command=Boutton3, width=3, height=2, bg="grey", fg="white").place(x=90, y=40)
B4 = Button(fen,text="4", command=Boutton4, width=3, height=2, bg="grey", fg="white").place(x=10, y=90)
B5 = Button(fen,text="5", command=Boutton5, width=3, height=2, bg="grey", fg="white").place(x=50, y=90)
B6 = Button(fen,text="6", command=Boutton6, width=3, height=2, bg="grey", fg="white").place(x=90, y=90)
B7 = Button(fen,text="7", command=Boutton7, width=3, height=2, bg="grey", fg="white").place(x=10, y=140)
B8 = Button(fen,text="8", command=Boutton8, width=3, height=2, bg="grey", fg="white").place(x=50, y=140)
B9 = Button(fen,text="9", command=Boutton9, width=3, height=2, bg="grey", fg="white").place(x=90, y=140)
B0 = Button(fen,text="0", command=Boutton0, width=3, height=2, bg="grey", fg="white").place(x=50, y=190)
BC = Button(fen,text="AC", command=BouttonAC, width=3, height=2, bg="gold", fg="red", relief=RIDGE).place(x=10, y=190)
BF = Button(fen,text=".", command=BouttonF, width=3, height=2, bg="grey", fg="white").place(x=90, y=190)
BT = Button(fen,text="%", command=BouttonT, width=3, height=2, bg="grey", fg="blue").place(x=121, y=190)
BE = Button(fen,text="=", command=BouttonE, width=3, height=2, bg="skyblue", fg="black", relief=GROOVE).place(x=121, y=39)
BD = Button(fen,text="/", command=BouttonD, width=3, height=2, bg="gold", fg="black", relief=GROOVE).place(x=152, y=189)
BM = Button(fen,text="X", command=BouttonM, width=3, height=2, bg="gold", fg="black", relief=GROOVE).place(x=151, y=140)
BP = Button(fen,text="+", command=BouttonP, width=3, height=2, bg="gold", fg="black", relief=GROOVE).place(x=152, y=39)
BS = Button(fen,text="-", command=BouttonS, width=3, height=2, bg="gold", fg="black",relief=GROOVE).place(x=151, y=90)

fen.mainloop()
           


