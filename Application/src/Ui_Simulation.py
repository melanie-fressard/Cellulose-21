# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Simulation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import Mplwidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1195, 860)
        MainWindow.setStyleSheet("background-color:  rgb(210, 255, 252)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.globalGridLayout = QtWidgets.QGridLayout()
        self.globalGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.globalGridLayout.setSpacing(0)
        self.globalGridLayout.setObjectName("globalGridLayout")
        self.globalVerticalLayout = QtWidgets.QVBoxLayout()
        self.globalVerticalLayout.setSpacing(40)
        self.globalVerticalLayout.setObjectName("globalVerticalLayout")
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titre.sizePolicy().hasHeightForWidth())
        self.Titre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Titre.setFont(font)
        self.Titre.setStyleSheet("font: 75 20pt \"Century Schoolbook L\";")
        self.Titre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Titre.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Titre.setScaledContents(False)
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")
        self.globalVerticalLayout.addWidget(self.Titre)
        self.horizontalLayout_animation = QtWidgets.QHBoxLayout()
        self.horizontalLayout_animation.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_animation.setSpacing(0)
        self.horizontalLayout_animation.setObjectName("horizontalLayout_animation")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_animation.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.animationSubstrat = Mplwidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.animationSubstrat.sizePolicy().hasHeightForWidth())
        self.animationSubstrat.setSizePolicy(sizePolicy)
        self.animationSubstrat.setMinimumSize(QtCore.QSize(300, 300))
        self.animationSubstrat.setMaximumSize(QtCore.QSize(400, 400))
        self.animationSubstrat.setStyleSheet("background-color: blue\n"
"")
        self.animationSubstrat.setObjectName("animationSubstrat")
        self.verticalLayout_4.addWidget(self.animationSubstrat)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_animation.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_animation.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_animation.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_animation.addItem(spacerItem4)
        self.gridLayout_donnees = QtWidgets.QGridLayout()
        self.gridLayout_donnees.setObjectName("gridLayout_donnees")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_donnees.addWidget(self.label_2, 0, 1, 1, 1)
        self.donnees_5 = QtWidgets.QHBoxLayout()
        self.donnees_5.setObjectName("donnees_5")
        self.cDiff = QtWidgets.QLabel(self.centralwidget)
        self.cDiff.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.cDiff.setObjectName("cDiff")
        self.donnees_5.addWidget(self.cDiff)
        self.cDiffVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.cDiffVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.cDiffVal.setMaximum(999.0)
        self.cDiffVal.setSingleStep(0.01)
        self.cDiffVal.setProperty("value", 0.3)
        self.cDiffVal.setObjectName("cDiffVal")
        self.donnees_5.addWidget(self.cDiffVal)
        self.gridLayout_donnees.addLayout(self.donnees_5, 4, 0, 1, 1)
        self.donnees_2 = QtWidgets.QHBoxLayout()
        self.donnees_2.setObjectName("donnees_2")
        self.nbCases = QtWidgets.QLabel(self.centralwidget)
        self.nbCases.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.nbCases.setObjectName("nbCases")
        self.donnees_2.addWidget(self.nbCases)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setProperty("value", 250)
        self.spinBox_2.setObjectName("spinBox_2")
        self.donnees_2.addWidget(self.spinBox_2)
        self.gridLayout_donnees.addLayout(self.donnees_2, 1, 0, 1, 1)
        self.donnees_4 = QtWidgets.QHBoxLayout()
        self.donnees_4.setObjectName("donnees_4")
        self.cIni = QtWidgets.QLabel(self.centralwidget)
        self.cIni.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.cIni.setObjectName("cIni")
        self.donnees_4.addWidget(self.cIni)
        self.cIniVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.cIniVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.cIniVal.setMaximum(999.0)
        self.cIniVal.setSingleStep(0.01)
        self.cIniVal.setProperty("value", 0.4)
        self.cIniVal.setObjectName("cIniVal")
        self.donnees_4.addWidget(self.cIniVal)
        self.gridLayout_donnees.addLayout(self.donnees_4, 3, 0, 1, 1)
        self.donnees_7 = QtWidgets.QHBoxLayout()
        self.donnees_7.setObjectName("donnees_7")
        self.temps = QtWidgets.QLabel(self.centralwidget)
        self.temps.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.temps.setObjectName("temps")
        self.donnees_7.addWidget(self.temps)
        self.tempsVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.tempsVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.tempsVal.setMaximum(999.0)
        self.tempsVal.setSingleStep(0.01)
        self.tempsVal.setProperty("value", 30.0)
        self.tempsVal.setObjectName("tempsVal")
        self.donnees_7.addWidget(self.tempsVal)
        self.gridLayout_donnees.addLayout(self.donnees_7, 6, 0, 1, 1)
        self.donnees_6 = QtWidgets.QHBoxLayout()
        self.donnees_6.setObjectName("donnees_6")
        self.vDiff = QtWidgets.QLabel(self.centralwidget)
        self.vDiff.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.vDiff.setObjectName("vDiff")
        self.donnees_6.addWidget(self.vDiff)
        self.vDiffVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.vDiffVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.vDiffVal.setMaximum(999.0)
        self.vDiffVal.setSingleStep(0.01)
        self.vDiffVal.setProperty("value", 5.0)
        self.vDiffVal.setObjectName("vDiffVal")
        self.donnees_6.addWidget(self.vDiffVal)
        self.gridLayout_donnees.addLayout(self.donnees_6, 5, 0, 1, 1)
        self.donnees_1 = QtWidgets.QHBoxLayout()
        self.donnees_1.setObjectName("donnees_1")
        self.largeur = QtWidgets.QLabel(self.centralwidget)
        self.largeur.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.largeur.setObjectName("largeur")
        self.donnees_1.addWidget(self.largeur)
        self.largeurVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.largeurVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.largeurVal.setMaximum(999.0)
        self.largeurVal.setSingleStep(0.01)
        self.largeurVal.setProperty("value", 80.0)
        self.largeurVal.setObjectName("largeurVal")
        self.donnees_1.addWidget(self.largeurVal)
        self.gridLayout_donnees.addLayout(self.donnees_1, 0, 0, 1, 1)
        self.donnees_3 = QtWidgets.QHBoxLayout()
        self.donnees_3.setObjectName("donnees_3")
        self.rayon = QtWidgets.QLabel(self.centralwidget)
        self.rayon.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.rayon.setObjectName("rayon")
        self.donnees_3.addWidget(self.rayon)
        self.rayonVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rayonVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.rayonVal.setMaximum(999.0)
        self.rayonVal.setSingleStep(0.01)
        self.rayonVal.setProperty("value", 25.0)
        self.rayonVal.setObjectName("rayonVal")
        self.donnees_3.addWidget(self.rayonVal)
        self.gridLayout_donnees.addLayout(self.donnees_3, 2, 0, 1, 1)
        self.donnees_8 = QtWidgets.QHBoxLayout()
        self.donnees_8.setObjectName("donnees_8")
        self.gdDelta = QtWidgets.QLabel(self.centralwidget)
        self.gdDelta.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.gdDelta.setObjectName("gdDelta")
        self.donnees_8.addWidget(self.gdDelta)
        self.gdDeltaVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gdDeltaVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.gdDeltaVal.setDecimals(2)
        self.gdDeltaVal.setMaximum(999.0)
        self.gdDeltaVal.setSingleStep(0.01)
        self.gdDeltaVal.setProperty("value", 0.3)
        self.gdDeltaVal.setObjectName("gdDeltaVal")
        self.donnees_8.addWidget(self.gdDeltaVal)
        self.gridLayout_donnees.addLayout(self.donnees_8, 7, 0, 1, 1)
        self.entreeDonnee = QtWidgets.QHBoxLayout()
        self.entreeDonnee.setObjectName("entreeDonnee")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.entreeDonnee.addItem(spacerItem5)
        self.entree = QtWidgets.QPushButton(self.centralwidget)
        self.entree.setMinimumSize(QtCore.QSize(0, 0))
        self.entree.setMaximumSize(QtCore.QSize(100, 16777215))
        self.entree.setStyleSheet("background-color: white;")
        self.entree.setObjectName("entree")
        self.entreeDonnee.addWidget(self.entree)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.entreeDonnee.addItem(spacerItem6)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setStyleSheet("background-color: white;")
        self.start.setObjectName("start")
        self.entreeDonnee.addWidget(self.start)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.entreeDonnee.addItem(spacerItem7)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setStyleSheet("background-color: white;")
        self.stop.setObjectName("stop")
        self.entreeDonnee.addWidget(self.stop)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.entreeDonnee.addItem(spacerItem8)
        self.gridLayout_donnees.addLayout(self.entreeDonnee, 9, 0, 1, 1)
        self.donnees_9 = QtWidgets.QHBoxLayout()
        self.donnees_9.setObjectName("donnees_9")
        self.ptDelta = QtWidgets.QLabel(self.centralwidget)
        self.ptDelta.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.ptDelta.setObjectName("ptDelta")
        self.donnees_9.addWidget(self.ptDelta)
        self.ptDeltaVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ptDeltaVal.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";\n"
"")
        self.ptDeltaVal.setDecimals(3)
        self.ptDeltaVal.setMaximum(999.0)
        self.ptDeltaVal.setSingleStep(0.01)
        self.ptDeltaVal.setProperty("value", 0.005)
        self.ptDeltaVal.setObjectName("ptDeltaVal")
        self.donnees_9.addWidget(self.ptDeltaVal)
        self.gridLayout_donnees.addLayout(self.donnees_9, 8, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.doubleSpinBox.setMaximum(999.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.4)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_donnees.addWidget(self.doubleSpinBox, 0, 2, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.doubleSpinBox_2.setMaximum(999.0)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 0.1)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_donnees.addWidget(self.doubleSpinBox_2, 1, 2, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.doubleSpinBox_3.setMaximum(999.0)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 0.1)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_donnees.addWidget(self.doubleSpinBox_3, 2, 2, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.doubleSpinBox_4.setMaximum(999.0)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setProperty("value", 10.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_donnees.addWidget(self.doubleSpinBox_4, 3, 2, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.doubleSpinBox_5.setMaximum(999.0)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setProperty("value", 0.2)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_donnees.addWidget(self.doubleSpinBox_5, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_donnees.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_donnees.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_donnees.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_donnees.addWidget(self.label_7, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_donnees.addWidget(self.label_6, 4, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setStyleSheet("background-color: white;\n"
"font: 75 10pt \"Century Schoolbook L\";")
        self.spinBox.setMaximum(999)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_donnees.addWidget(self.spinBox, 5, 2, 1, 1)
        self.horizontalLayout_animation.addLayout(self.gridLayout_donnees)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_animation.addItem(spacerItem9)
        self.globalVerticalLayout.addLayout(self.horizontalLayout_animation)
        self.verticalLayout_graphs = QtWidgets.QVBoxLayout()
        self.verticalLayout_graphs.setSpacing(0)
        self.verticalLayout_graphs.setObjectName("verticalLayout_graphs")
        self.horizontalLayout_forLabel = QtWidgets.QHBoxLayout()
        self.horizontalLayout_forLabel.setObjectName("horizontalLayout_forLabel")
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forLabel.addItem(spacerItem10)
        self.titreGraph_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titreGraph_1.sizePolicy().hasHeightForWidth())
        self.titreGraph_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.titreGraph_1.setFont(font)
        self.titreGraph_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titreGraph_1.setStyleSheet("font: 75 10pt \"Century Schoolbook L\";")
        self.titreGraph_1.setAlignment(QtCore.Qt.AlignCenter)
        self.titreGraph_1.setObjectName("titreGraph_1")
        self.horizontalLayout_forLabel.addWidget(self.titreGraph_1)
        spacerItem11 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forLabel.addItem(spacerItem11)
        self.titreGraph_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titreGraph_2.sizePolicy().hasHeightForWidth())
        self.titreGraph_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.titreGraph_2.setFont(font)
        self.titreGraph_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titreGraph_2.setStyleSheet("font: 75 10pt \"Century Schoolbook L\";")
        self.titreGraph_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titreGraph_2.setObjectName("titreGraph_2")
        self.horizontalLayout_forLabel.addWidget(self.titreGraph_2)
        spacerItem12 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forLabel.addItem(spacerItem12)
        self.verticalLayout_graphs.addLayout(self.horizontalLayout_forLabel)
        self.horizontalLayout_forGraphs = QtWidgets.QHBoxLayout()
        self.horizontalLayout_forGraphs.setObjectName("horizontalLayout_forGraphs")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forGraphs.addItem(spacerItem13)
        self.graph_1 = Mplwidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_1.sizePolicy().hasHeightForWidth())
        self.graph_1.setSizePolicy(sizePolicy)
        self.graph_1.setMinimumSize(QtCore.QSize(500, 300))
        self.graph_1.setMaximumSize(QtCore.QSize(600, 300))
        self.graph_1.setStyleSheet("background-color: green")
        self.graph_1.setObjectName("graph_1")
        self.horizontalLayout_forGraphs.addWidget(self.graph_1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forGraphs.addItem(spacerItem14)
        self.graph_2 = Mplwidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_2.sizePolicy().hasHeightForWidth())
        self.graph_2.setSizePolicy(sizePolicy)
        self.graph_2.setMinimumSize(QtCore.QSize(500, 300))
        self.graph_2.setMaximumSize(QtCore.QSize(600, 300))
        self.graph_2.setStyleSheet("background-color: yellow")
        self.graph_2.setObjectName("graph_2")
        self.horizontalLayout_forGraphs.addWidget(self.graph_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_forGraphs.addItem(spacerItem15)
        self.verticalLayout_graphs.addLayout(self.horizontalLayout_forGraphs)
        self.globalVerticalLayout.addLayout(self.verticalLayout_graphs)
        self.globalGridLayout.addLayout(self.globalVerticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.globalGridLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1195, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.entree.clicked.connect(MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titre.setText(_translate("MainWindow", "Cellulose 21"))
        self.label.setText(_translate("MainWindow", " Concentration de cellulose avec bactéries"))
        self.label_2.setText(_translate("MainWindow", "Masse initiale des bactérie (pg)"))
        self.cDiff.setText(_translate("MainWindow", "Concentration pour diffuser (en pg/µ²) = "))
        self.nbCases.setText(_translate("MainWindow", "Nombre de cases = "))
        self.cIni.setText(_translate("MainWindow", "Concentration initiale (en pg/µ²) = "))
        self.temps.setText(_translate("MainWindow", "Temps de simulation (en h) = "))
        self.vDiff.setText(_translate("MainWindow", "Vitesse de diffusion (en µm²/h) =  "))
        self.largeur.setText(_translate("MainWindow", "Longueur (µm) = "))
        self.rayon.setText(_translate("MainWindow", "Rayon du cercle (en µm) = "))
        self.gdDelta.setText(_translate("MainWindow", "Delta = "))
        self.entree.setText(_translate("MainWindow", "Lancer"))
        self.start.setText(_translate("MainWindow", "Continuer"))
        self.stop.setText(_translate("MainWindow", "Pause"))
        self.ptDelta.setText(_translate("MainWindow", "delta = "))
        self.ptDeltaVal.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>background-color: white;</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Vitesse d\'absorbtion (µm/h)"))
        self.label_4.setText(_translate("MainWindow", "Vitesse déplacement (µm^4)/(pg h)"))
        self.label_5.setText(_translate("MainWindow", "Vitesse max des bactérie (µm/h)"))
        self.label_7.setText(_translate("MainWindow", "Nombre bactérie initiale"))
        self.label_6.setText(_translate("MainWindow", "Constante de conversion masse/biomasse "))
        self.titreGraph_1.setText(_translate("MainWindow", "Concentration du substrat"))
        self.titreGraph_2.setText(_translate("MainWindow", "Population de bactéries"))
