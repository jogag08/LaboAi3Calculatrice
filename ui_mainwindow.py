# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Affichage = QLabel(self.centralwidget)
        self.Affichage.setObjectName(u"Affichage")
        self.Affichage.setGeometry(QRect(10, 110, 441, 71))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 210, 461, 341))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PERCENTbutton = QPushButton(self.layoutWidget)
        self.PERCENTbutton.setObjectName(u"PERCENTbutton")

        self.gridLayout.addWidget(self.PERCENTbutton, 0, 0, 1, 1)

        self.CEbutton = QPushButton(self.layoutWidget)
        self.CEbutton.setObjectName(u"CEbutton")

        self.gridLayout.addWidget(self.CEbutton, 0, 1, 1, 1)

        self.Cbutton = QPushButton(self.layoutWidget)
        self.Cbutton.setObjectName(u"Cbutton")

        self.gridLayout.addWidget(self.Cbutton, 0, 2, 1, 1)

        self.BACKSPACEbutton = QPushButton(self.layoutWidget)
        self.BACKSPACEbutton.setObjectName(u"BACKSPACEbutton")

        self.gridLayout.addWidget(self.BACKSPACEbutton, 0, 3, 1, 1)

        self.DIVBYONEbutton = QPushButton(self.layoutWidget)
        self.DIVBYONEbutton.setObjectName(u"DIVBYONEbutton")

        self.gridLayout.addWidget(self.DIVBYONEbutton, 1, 0, 1, 1)

        self.POWERbutton = QPushButton(self.layoutWidget)
        self.POWERbutton.setObjectName(u"POWERbutton")

        self.gridLayout.addWidget(self.POWERbutton, 1, 1, 1, 1)

        self.SQRTbutton = QPushButton(self.layoutWidget)
        self.SQRTbutton.setObjectName(u"SQRTbutton")

        self.gridLayout.addWidget(self.SQRTbutton, 1, 2, 1, 1)

        self.DIVIDEbutton = QPushButton(self.layoutWidget)
        self.DIVIDEbutton.setObjectName(u"DIVIDEbutton")

        self.gridLayout.addWidget(self.DIVIDEbutton, 1, 3, 1, 1)

        self.SEVENbutton = QPushButton(self.layoutWidget)
        self.SEVENbutton.setObjectName(u"SEVENbutton")

        self.gridLayout.addWidget(self.SEVENbutton, 2, 0, 1, 1)

        self.EIGHTbutton = QPushButton(self.layoutWidget)
        self.EIGHTbutton.setObjectName(u"EIGHTbutton")

        self.gridLayout.addWidget(self.EIGHTbutton, 2, 1, 1, 1)

        self.NINEbutton = QPushButton(self.layoutWidget)
        self.NINEbutton.setObjectName(u"NINEbutton")

        self.gridLayout.addWidget(self.NINEbutton, 2, 2, 1, 1)

        self.TIMESbutton = QPushButton(self.layoutWidget)
        self.TIMESbutton.setObjectName(u"TIMESbutton")

        self.gridLayout.addWidget(self.TIMESbutton, 2, 3, 1, 1)

        self.FOURbutton = QPushButton(self.layoutWidget)
        self.FOURbutton.setObjectName(u"FOURbutton")

        self.gridLayout.addWidget(self.FOURbutton, 3, 0, 1, 1)

        self.FIVEbutton = QPushButton(self.layoutWidget)
        self.FIVEbutton.setObjectName(u"FIVEbutton")

        self.gridLayout.addWidget(self.FIVEbutton, 3, 1, 1, 1)

        self.SIXbutton = QPushButton(self.layoutWidget)
        self.SIXbutton.setObjectName(u"SIXbutton")

        self.gridLayout.addWidget(self.SIXbutton, 3, 2, 1, 1)

        self.MINUSbutton = QPushButton(self.layoutWidget)
        self.MINUSbutton.setObjectName(u"MINUSbutton")

        self.gridLayout.addWidget(self.MINUSbutton, 3, 3, 1, 1)

        self.ONEbutton = QPushButton(self.layoutWidget)
        self.ONEbutton.setObjectName(u"ONEbutton")

        self.gridLayout.addWidget(self.ONEbutton, 4, 0, 1, 1)

        self.TWObutton = QPushButton(self.layoutWidget)
        self.TWObutton.setObjectName(u"TWObutton")

        self.gridLayout.addWidget(self.TWObutton, 4, 1, 1, 1)

        self.THREEbutton = QPushButton(self.layoutWidget)
        self.THREEbutton.setObjectName(u"THREEbutton")

        self.gridLayout.addWidget(self.THREEbutton, 4, 2, 1, 1)

        self.PLUSbutton = QPushButton(self.layoutWidget)
        self.PLUSbutton.setObjectName(u"PLUSbutton")

        self.gridLayout.addWidget(self.PLUSbutton, 4, 3, 1, 1)

        self.ADDorMINUSbutton = QPushButton(self.layoutWidget)
        self.ADDorMINUSbutton.setObjectName(u"ADDorMINUSbutton")

        self.gridLayout.addWidget(self.ADDorMINUSbutton, 5, 0, 1, 1)

        self.ZERObutton = QPushButton(self.layoutWidget)
        self.ZERObutton.setObjectName(u"ZERObutton")

        self.gridLayout.addWidget(self.ZERObutton, 5, 1, 1, 1)

        self.POINTbutton = QPushButton(self.layoutWidget)
        self.POINTbutton.setObjectName(u"POINTbutton")

        self.gridLayout.addWidget(self.POINTbutton, 5, 2, 1, 1)

        self.EQUALbutton = QPushButton(self.layoutWidget)
        self.EQUALbutton.setObjectName(u"EQUALbutton")

        self.gridLayout.addWidget(self.EQUALbutton, 5, 3, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(200, 0, 256, 31))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.QUITbutton = QPushButton(self.layoutWidget1)
        self.QUITbutton.setObjectName(u"QUITbutton")

        self.gridLayout_2.addWidget(self.QUITbutton, 0, 2, 1, 1)

        self.MAXIMIZbutton = QPushButton(self.layoutWidget1)
        self.MAXIMIZbutton.setObjectName(u"MAXIMIZbutton")

        self.gridLayout_2.addWidget(self.MAXIMIZbutton, 0, 1, 1, 1)

        self.MINIMIZEbutton = QPushButton(self.layoutWidget1)
        self.MINIMIZEbutton.setObjectName(u"MINIMIZEbutton")

        self.gridLayout_2.addWidget(self.MINIMIZEbutton, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 459, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MAXIMIZbutton.released.connect(MainWindow.showMaximized)
        self.MINIMIZEbutton.released.connect(MainWindow.showMinimized)
        self.QUITbutton.released.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Affichage.setText(QCoreApplication.translate("MainWindow", u"Affichage", None))
        self.PERCENTbutton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.CEbutton.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Cbutton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.BACKSPACEbutton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.DIVBYONEbutton.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.POWERbutton.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.SQRTbutton.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
        self.DIVIDEbutton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.SEVENbutton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.EIGHTbutton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.NINEbutton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.TIMESbutton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.FOURbutton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.FIVEbutton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.SIXbutton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.MINUSbutton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ONEbutton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.TWObutton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.THREEbutton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.PLUSbutton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ADDorMINUSbutton.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.ZERObutton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.POINTbutton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.EQUALbutton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.QUITbutton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.MAXIMIZbutton.setText(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.MINIMIZEbutton.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
    # retranslateUi

