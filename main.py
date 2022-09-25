# This Python file uses the following encoding: utf-8

#CETTE CALCULATRICE NE PERMET PAS PLUS DE DEUX NOMBRES PAR ÉQUATION

#SOURCES UTILISÉES
#FONCTION SPLIT() : https://www.w3schools.com/python/ref_string_split.asp
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
import math


from ui_mainwindow import Ui_MainWindow

class FenetrePrincipale(QMainWindow):
    currText:str = ""
    def __init__(self, x= 0, y=0, w=640, h=480):
        super(FenetrePrincipale,self).__init__()
        self.setGeometry(x,y,w,h)
        self.setWindowTitle("Calculatrice")
        self.initUi()

    def initUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Boutons pour les chiffres
        self.ui.ZERObutton.clicked.connect(self.onClickZERO)
        self.ui.ONEbutton.clicked.connect(self.onClickONE)
        self.ui.TWObutton.clicked.connect(self.onClickTWO)
        self.ui.THREEbutton.clicked.connect(self.onClickTHREE)
        self.ui.FOURbutton.clicked.connect(self.onClickFOUR)
        self.ui.FIVEbutton.clicked.connect(self.onClickFIVE)
        self.ui.SIXbutton.clicked.connect(self.onClickSIX)
        self.ui.SEVENbutton.clicked.connect(self.onClickSEVEN)
        self.ui.EIGHTbutton.clicked.connect(self.onClickEIGHT)
        self.ui.NINEbutton.clicked.connect(self.onClickNINE)
        self.ui.POINTbutton.clicked.connect(self.onClickPOINT)

        #Boutons pour faire les équations
        self.ui.PLUSbutton.clicked.connect(self.onClickPLUS)
        self.ui.MINUSbutton.clicked.connect(self.onClickMINUS)
        self.ui.TIMESbutton.clicked.connect(self.onClickTIMES)
        self.ui.DIVIDEbutton.clicked.connect(self.onClickDIVIDE)     
        self.ui.DIVBYONEbutton.clicked.connect(self.onClickDIVBYONE)
        self.ui.PERCENTbutton.clicked.connect(self.onClickPERCENT)
        self.ui.POWERbutton.clicked.connect(self.onClickPOWER)
        self.ui.SQRTbutton.clicked.connect(self.onClickSQRT)
        self.ui.EQUALbutton.clicked.connect(self.onClickEQUAL)

        #Boutons pour modifier les inputs
        self.ui.Cbutton.clicked.connect(self.onClickC)
        self.ui.CEbutton.clicked.connect(self.onClickCE)
        self.ui.ADDorMINUSbutton.clicked.connect(self.onClickADDorMINUS)
        self.ui.BACKSPACEbutton.clicked.connect(self.onClickBACKSPACE)

        self.ui.Affichage.setText(self.currText)

    #Fonctions des boutons pour les chiffres
    def onClickZERO(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"0")

    def onClickONE(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"1")

    def onClickTWO(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"2")

    def onClickTHREE(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"3")

    def onClickFOUR(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"4")

    def onClickFIVE(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"5")

    def onClickSIX(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"6")

    def onClickSEVEN(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"7")

    def onClickEIGHT(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"8")

    def onClickNINE(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"9")

    def onClickPOINT(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+".")

    #Fonctions des boutons pour faire les équations
    def onClickPLUS(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"+")

    def onClickMINUS(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"-")

    def onClickTIMES(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"X")

    def onClickDIVIDE(self):
        currText = self.ui.Affichage.text()
        self.ui.Affichage.setText(currText+"/")

    def onClickDIVBYONE(self):
        currText = self.ui.Affichage.text()
        value = float(currText)
        result = 1/value
        self.ui.Affichage.setText(str(result))

    def onClickPERCENT(self):
        currText = self.ui.Affichage.text()

        #ADDITION
        if currText.find("+") != -1:
            currTextSplit = currText.split("+")
            value1 = float(currTextSplit[0])
            value2 = (float(currTextSplit[1])*value1)/100
            self.ui.Affichage.setText(str(value2))

        #SOUSTRACTION
        elif currText.find("-") != -1:
            currTextSplit = currText.split("-")
            value1 = float(currTextSplit[0])
            print(value1)
            value2 = (float(currTextSplit[1])*value1)/100
            self.ui.Affichage.setText(str(value2))

        #MULTIPLICATION
        elif currText.find("X") != -1:
            currTextSplit = currText.split("X")
            value = float(currTextSplit[1])
            result = value / 100
            self.ui.Affichage.setText(str(result))

        #DIVISION
        elif currText.find("/") != -1:
            currTextSplit = currText.split("/")
            value = float(currTextSplit[1])
            result = value / 100
            self.ui.Affichage.setText(str(result))

        else : self.ui.Affichage.setText("")


    def onClickPOWER(self):
        currText = self.ui.Affichage.text()
        value = float(currText)
        value = value*value
        self.ui.Affichage.setText(str(value))

    def onClickSQRT(self):
        currText = self.ui.Affichage.text()
        value = float(currText)
        value = math.sqrt(value)
        self.ui.Affichage.setText(str(value))

    def onClickEQUAL(self):
        currText = self.ui.Affichage.text()

        #ADDITION
        if currText.find("+") != -1: #si find() ne trouve rien, il retourne -1
            currTextSplit = currText.split("+")
            value1 = float(currTextSplit[0])
            value2 = float(currTextSplit[1])
            numToAdd = (value1, value2)
            result = sum(numToAdd)
            self.ui.Affichage.setText(str(result))

        #SOUSTRACTION
        elif currText.find("-") != -1:
            currTextSplit = currText.split("-")
            value1 = float(currTextSplit[0])
            value2 = float(currTextSplit[1])
            result = value1 - value2
            self.ui.Affichage.setText(str(result))

        #MULTIPLICATION
        elif currText.find("X") != -1:
            currTextSplit = currText.split("X")
            value1 = float(currTextSplit[0])
            value2 = float(currTextSplit[1])
            result = value1 * value2
            self.ui.Affichage.setText(str(result))

        #DIVISION
        elif currText.find("/") != -1:
            currTextSplit = currText.split("/")
            value1 = float(currTextSplit[0])
            value2 = float(currTextSplit[1])
            result = value1 / value2
            self.ui.Affichage.setText(str(result))

    #Fonctions des boutons pour modifier les inputs
    def onClickC(self):
        self.ui.Affichage.setText("")

    def onClickCE(self):
        self.ui.Affichage.setText("")

    def onClickADDorMINUS(self):
        currText = self.ui.Affichage.text()
        result = float(currText) * -1
        self.ui.Affichage.setText(str(result))

    def onClickBACKSPACE(self):
        currText = self.ui.Affichage.text()
        textLen = len(currText)
        newCurrText = currText[:textLen-1]
        self.ui.Affichage.setText(newCurrText)

def window():
    app = QApplication(sys.argv)
    win = FenetrePrincipale()

    app.setActiveWindow(win)
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    window()


#def onClicked():
#    print("Hello World !")
#
#def pressOnMe():
#    print("Got pressed")
#
#def releaseOnMe():
#    print("Got released")



#butt = QPushButton("Mets du beurre sur mes bagels", win)
#butt.move(20,22)
#butt.clicked.connect(onClicked)
#butt.pressed.connect(pressOnMe)
#butt.released.connect(releaseOnMe)



#def initUi(self):
#    self.ui = Ui_MainWindow()
#    self.ui.setupUi(self)
#    self.ui.hello.clicked.connect(self.onClicked)
#    for i in range(0,4):
#        getattr(self.ui,"num_" + str(i)).clicked.connect(self.onClicked)

#def onClicked(self):
#    butt = self.sender()
#    print(butt.objectName() + "World !")
