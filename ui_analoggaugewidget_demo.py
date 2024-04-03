# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analoggaugewidget_demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from analoggaugewidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 712)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = AnalogGaugeWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(100, 100))
        self.widget.setMaximumSize(QSize(600, 600))
        self.widget.setBaseSize(QSize(300, 300))
        self.widget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.Parameter = QTabWidget(self.centralwidget)
        self.Parameter.setObjectName(u"Parameter")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_16 = QGridLayout(self.tab_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lcdNumber_9 = QLCDNumber(self.tab_3)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_9.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_9.setFrameShadow(QFrame.Plain)
        self.lcdNumber_9.setLineWidth(0)
        self.lcdNumber_9.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_9, 6, 2, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.tab_3)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        self.lcdNumber_4.setFont(font)
        self.lcdNumber_4.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_4.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_4.setFrameShadow(QFrame.Plain)
        self.lcdNumber_4.setLineWidth(0)
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.horizontalSlider_5 = QSlider(self.tab_3)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setMaximum(200)
        self.horizontalSlider_5.setValue(0)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_5, 1, 1, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.tab_3)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_3.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_3.setFrameShadow(QFrame.Plain)
        self.lcdNumber_3.setLineWidth(0)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_3, 1, 2, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.GaugeStartSlider = QSlider(self.tab_3)
        self.GaugeStartSlider.setObjectName(u"GaugeStartSlider")
        self.GaugeStartSlider.setMaximum(360)
        self.GaugeStartSlider.setValue(0)
        self.GaugeStartSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.GaugeStartSlider, 4, 1, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.tab_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_2.setLineWidth(0)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_2, 2, 2, 1, 1)

        self.AussenRadiusSlider = QSlider(self.tab_3)
        self.AussenRadiusSlider.setObjectName(u"AussenRadiusSlider")
        self.AussenRadiusSlider.setMaximum(1000)
        self.AussenRadiusSlider.setValue(0)
        self.AussenRadiusSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.AussenRadiusSlider, 2, 1, 1, 1)

        self.InnenRadiusSlider = QSlider(self.tab_3)
        self.InnenRadiusSlider.setObjectName(u"InnenRadiusSlider")
        self.InnenRadiusSlider.setMaximum(1000)
        self.InnenRadiusSlider.setValue(0)
        self.InnenRadiusSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.InnenRadiusSlider, 3, 1, 1, 1)

        self.lcdNumber = QLCDNumber(self.tab_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber, 3, 2, 1, 1)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ActualSlider = QSlider(self.tab_3)
        self.ActualSlider.setObjectName(u"ActualSlider")
        self.ActualSlider.setMaximum(200)
        self.ActualSlider.setValue(0)
        self.ActualSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.ActualSlider, 0, 1, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lcdNumber_8 = QLCDNumber(self.tab_3)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        self.lcdNumber_8.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_8.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_8.setFrameShadow(QFrame.Plain)
        self.lcdNumber_8.setLineWidth(0)
        self.lcdNumber_8.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_8, 5, 2, 1, 1)

        self.GaugeSizeSlider = QSlider(self.tab_3)
        self.GaugeSizeSlider.setObjectName(u"GaugeSizeSlider")
        self.GaugeSizeSlider.setMaximum(360)
        self.GaugeSizeSlider.setValue(0)
        self.GaugeSizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.GaugeSizeSlider, 5, 1, 1, 1)

        self.offsetSlider = QSlider(self.tab_3)
        self.offsetSlider.setObjectName(u"offsetSlider")
        self.offsetSlider.setMinimum(-360)
        self.offsetSlider.setMaximum(360)
        self.offsetSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.offsetSlider, 6, 1, 1, 1)

        self.lcdNumber_7 = QLCDNumber(self.tab_3)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_7.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_7.setFrameShadow(QFrame.Plain)
        self.lcdNumber_7.setLineWidth(0)
        self.lcdNumber_7.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_7, 4, 2, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.CB_ScaleText = QCheckBox(self.tab_3)
        self.CB_ScaleText.setObjectName(u"CB_ScaleText")
        self.CB_ScaleText.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ScaleText, 5, 0, 1, 1)

        self.CB_Needle = QCheckBox(self.tab_3)
        self.CB_Needle.setObjectName(u"CB_Needle")
        self.CB_Needle.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_Needle, 0, 2, 1, 1)

        self.CB_ShowBarGraph = QCheckBox(self.tab_3)
        self.CB_ShowBarGraph.setObjectName(u"CB_ShowBarGraph")
        self.CB_ShowBarGraph.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ShowBarGraph, 0, 1, 1, 1)

        self.CB_barGraph = QCheckBox(self.tab_3)
        self.CB_barGraph.setObjectName(u"CB_barGraph")
        self.CB_barGraph.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_barGraph, 0, 0, 1, 1)

        self.CB_ValueText = QCheckBox(self.tab_3)
        self.CB_ValueText.setObjectName(u"CB_ValueText")
        self.CB_ValueText.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ValueText, 2, 0, 1, 1)

        self.CB_CenterPoint = QCheckBox(self.tab_3)
        self.CB_CenterPoint.setObjectName(u"CB_CenterPoint")
        self.CB_CenterPoint.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_CenterPoint, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.CB_Grid = QCheckBox(self.tab_3)
        self.CB_Grid.setObjectName(u"CB_Grid")
        self.CB_Grid.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_Grid, 6, 0, 1, 1)

        self.CB_fineGrid = QCheckBox(self.tab_3)
        self.CB_fineGrid.setObjectName(u"CB_fineGrid")
        self.CB_fineGrid.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_fineGrid, 7, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.ActualValue = QLCDNumber(self.tab_3)
        self.ActualValue.setObjectName(u"ActualValue")
        self.ActualValue.setStyleSheet(u"QLCDNumber {\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.ActualValue.setFrameShape(QFrame.NoFrame)
        self.ActualValue.setFrameShadow(QFrame.Sunken)
        self.ActualValue.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.ActualValue, 2, 0, 1, 1)

        self.Parameter.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_15 = QGridLayout(self.tab)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.lcdNumber_Red_Needle = QLCDNumber(self.groupBox)
        self.lcdNumber_Red_Needle.setObjectName(u"lcdNumber_Red_Needle")
        self.lcdNumber_Red_Needle.setFont(font)
        self.lcdNumber_Red_Needle.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Red_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Needle.setLineWidth(0)
        self.lcdNumber_Red_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Red_Needle, 0, 2, 1, 1)

        self.GreenSlider_Needle = QSlider(self.groupBox)
        self.GreenSlider_Needle.setObjectName(u"GreenSlider_Needle")
        self.GreenSlider_Needle.setMaximum(255)
        self.GreenSlider_Needle.setValue(50)
        self.GreenSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.GreenSlider_Needle, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.lcdNumber_Green_Needle = QLCDNumber(self.groupBox)
        self.lcdNumber_Green_Needle.setObjectName(u"lcdNumber_Green_Needle")
        self.lcdNumber_Green_Needle.setFont(font)
        self.lcdNumber_Green_Needle.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Green_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Needle.setLineWidth(0)
        self.lcdNumber_Green_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Green_Needle, 1, 2, 1, 1)

        self.lcdNumber_Blue_Needle = QLCDNumber(self.groupBox)
        self.lcdNumber_Blue_Needle.setObjectName(u"lcdNumber_Blue_Needle")
        self.lcdNumber_Blue_Needle.setFont(font)
        self.lcdNumber_Blue_Needle.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Blue_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Needle.setLineWidth(0)
        self.lcdNumber_Blue_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Blue_Needle, 2, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.BlueSlider_Needle = QSlider(self.groupBox)
        self.BlueSlider_Needle.setObjectName(u"BlueSlider_Needle")
        self.BlueSlider_Needle.setMaximum(255)
        self.BlueSlider_Needle.setValue(50)
        self.BlueSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.BlueSlider_Needle, 2, 1, 1, 1)

        self.TrancSlider_Needle = QSlider(self.groupBox)
        self.TrancSlider_Needle.setObjectName(u"TrancSlider_Needle")
        self.TrancSlider_Needle.setMaximum(255)
        self.TrancSlider_Needle.setValue(255)
        self.TrancSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.TrancSlider_Needle, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_Needle = QLCDNumber(self.groupBox)
        self.lcdNumber_Trancparency_Needle.setObjectName(u"lcdNumber_Trancparency_Needle")
        self.lcdNumber_Trancparency_Needle.setFont(font)
        self.lcdNumber_Trancparency_Needle.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Trancparency_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Needle.setLineWidth(0)
        self.lcdNumber_Trancparency_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Trancparency_Needle, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.RedSlider_Needle = QSlider(self.groupBox)
        self.RedSlider_Needle.setObjectName(u"RedSlider_Needle")
        self.RedSlider_Needle.setMaximum(255)
        self.RedSlider_Needle.setValue(50)
        self.RedSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.RedSlider_Needle, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_9 = QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 1, 0, 1, 1)

        self.lcdNumber_Red_NeedleDrag = QLCDNumber(self.groupBox_2)
        self.lcdNumber_Red_NeedleDrag.setObjectName(u"lcdNumber_Red_NeedleDrag")
        self.lcdNumber_Red_NeedleDrag.setFont(font)
        self.lcdNumber_Red_NeedleDrag.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Red_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Red_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Red_NeedleDrag, 0, 2, 1, 1)

        self.GreenSlider_NeedleDrag = QSlider(self.groupBox_2)
        self.GreenSlider_NeedleDrag.setObjectName(u"GreenSlider_NeedleDrag")
        self.GreenSlider_NeedleDrag.setMaximum(255)
        self.GreenSlider_NeedleDrag.setValue(50)
        self.GreenSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.GreenSlider_NeedleDrag, 1, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_10.addWidget(self.label_17, 3, 0, 1, 1)

        self.lcdNumber_Green_NeedleDrag = QLCDNumber(self.groupBox_2)
        self.lcdNumber_Green_NeedleDrag.setObjectName(u"lcdNumber_Green_NeedleDrag")
        self.lcdNumber_Green_NeedleDrag.setFont(font)
        self.lcdNumber_Green_NeedleDrag.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Green_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Green_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Green_NeedleDrag, 1, 2, 1, 1)

        self.lcdNumber_Blue_NeedleDrag = QLCDNumber(self.groupBox_2)
        self.lcdNumber_Blue_NeedleDrag.setObjectName(u"lcdNumber_Blue_NeedleDrag")
        self.lcdNumber_Blue_NeedleDrag.setFont(font)
        self.lcdNumber_Blue_NeedleDrag.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Blue_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Blue_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Blue_NeedleDrag, 2, 2, 1, 1)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_10.addWidget(self.label_18, 2, 0, 1, 1)

        self.BlueSlider_NeedleDrag = QSlider(self.groupBox_2)
        self.BlueSlider_NeedleDrag.setObjectName(u"BlueSlider_NeedleDrag")
        self.BlueSlider_NeedleDrag.setMaximum(255)
        self.BlueSlider_NeedleDrag.setValue(50)
        self.BlueSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.BlueSlider_NeedleDrag, 2, 1, 1, 1)

        self.TrancSlider_NeedleDrag = QSlider(self.groupBox_2)
        self.TrancSlider_NeedleDrag.setObjectName(u"TrancSlider_NeedleDrag")
        self.TrancSlider_NeedleDrag.setMaximum(255)
        self.TrancSlider_NeedleDrag.setValue(255)
        self.TrancSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.TrancSlider_NeedleDrag, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_NeedleDrag = QLCDNumber(self.groupBox_2)
        self.lcdNumber_Trancparency_NeedleDrag.setObjectName(u"lcdNumber_Trancparency_NeedleDrag")
        self.lcdNumber_Trancparency_NeedleDrag.setFont(font)
        self.lcdNumber_Trancparency_NeedleDrag.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Trancparency_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Trancparency_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Trancparency_NeedleDrag, 3, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_10.addWidget(self.label_19, 0, 0, 1, 1)

        self.RedSlider_NeedleDrag = QSlider(self.groupBox_2)
        self.RedSlider_NeedleDrag.setObjectName(u"RedSlider_NeedleDrag")
        self.RedSlider_NeedleDrag.setMaximum(255)
        self.RedSlider_NeedleDrag.setValue(50)
        self.RedSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.RedSlider_NeedleDrag, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_12.addWidget(self.label_20, 1, 0, 1, 1)

        self.lcdNumber_Red_Scale = QLCDNumber(self.groupBox_3)
        self.lcdNumber_Red_Scale.setObjectName(u"lcdNumber_Red_Scale")
        self.lcdNumber_Red_Scale.setFont(font)
        self.lcdNumber_Red_Scale.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Red_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Scale.setLineWidth(0)
        self.lcdNumber_Red_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Red_Scale, 0, 2, 1, 1)

        self.GreenSlider_Scale = QSlider(self.groupBox_3)
        self.GreenSlider_Scale.setObjectName(u"GreenSlider_Scale")
        self.GreenSlider_Scale.setMaximum(255)
        self.GreenSlider_Scale.setValue(50)
        self.GreenSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.GreenSlider_Scale, 1, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 3, 0, 1, 1)

        self.lcdNumber_Green_Scale = QLCDNumber(self.groupBox_3)
        self.lcdNumber_Green_Scale.setObjectName(u"lcdNumber_Green_Scale")
        self.lcdNumber_Green_Scale.setFont(font)
        self.lcdNumber_Green_Scale.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Green_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Scale.setLineWidth(0)
        self.lcdNumber_Green_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Green_Scale, 1, 2, 1, 1)

        self.lcdNumber_Blue_Scale = QLCDNumber(self.groupBox_3)
        self.lcdNumber_Blue_Scale.setObjectName(u"lcdNumber_Blue_Scale")
        self.lcdNumber_Blue_Scale.setFont(font)
        self.lcdNumber_Blue_Scale.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Blue_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Scale.setLineWidth(0)
        self.lcdNumber_Blue_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Blue_Scale, 2, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_12.addWidget(self.label_22, 2, 0, 1, 1)

        self.BlueSlider_Scale = QSlider(self.groupBox_3)
        self.BlueSlider_Scale.setObjectName(u"BlueSlider_Scale")
        self.BlueSlider_Scale.setMaximum(255)
        self.BlueSlider_Scale.setValue(50)
        self.BlueSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.BlueSlider_Scale, 2, 1, 1, 1)

        self.TrancSlider_Scale = QSlider(self.groupBox_3)
        self.TrancSlider_Scale.setObjectName(u"TrancSlider_Scale")
        self.TrancSlider_Scale.setMaximum(255)
        self.TrancSlider_Scale.setValue(255)
        self.TrancSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.TrancSlider_Scale, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_Scale = QLCDNumber(self.groupBox_3)
        self.lcdNumber_Trancparency_Scale.setObjectName(u"lcdNumber_Trancparency_Scale")
        self.lcdNumber_Trancparency_Scale.setFont(font)
        self.lcdNumber_Trancparency_Scale.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Trancparency_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Scale.setLineWidth(0)
        self.lcdNumber_Trancparency_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Trancparency_Scale, 3, 2, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 1)

        self.RedSlider_Scale = QSlider(self.groupBox_3)
        self.RedSlider_Scale.setObjectName(u"RedSlider_Scale")
        self.RedSlider_Scale.setMaximum(255)
        self.RedSlider_Scale.setValue(50)
        self.RedSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.RedSlider_Scale, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_12, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_13 = QGridLayout(self.groupBox_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_14.addWidget(self.label_24, 1, 0, 1, 1)

        self.lcdNumber_Red_Display = QLCDNumber(self.groupBox_4)
        self.lcdNumber_Red_Display.setObjectName(u"lcdNumber_Red_Display")
        self.lcdNumber_Red_Display.setFont(font)
        self.lcdNumber_Red_Display.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Red_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Display.setLineWidth(0)
        self.lcdNumber_Red_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Red_Display, 0, 2, 1, 1)

        self.GreenSlider_Display = QSlider(self.groupBox_4)
        self.GreenSlider_Display.setObjectName(u"GreenSlider_Display")
        self.GreenSlider_Display.setMaximum(255)
        self.GreenSlider_Display.setValue(50)
        self.GreenSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.GreenSlider_Display, 1, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_14.addWidget(self.label_25, 3, 0, 1, 1)

        self.lcdNumber_Green_Display = QLCDNumber(self.groupBox_4)
        self.lcdNumber_Green_Display.setObjectName(u"lcdNumber_Green_Display")
        self.lcdNumber_Green_Display.setFont(font)
        self.lcdNumber_Green_Display.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Green_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Display.setLineWidth(0)
        self.lcdNumber_Green_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Green_Display, 1, 2, 1, 1)

        self.lcdNumber_Blue_Display = QLCDNumber(self.groupBox_4)
        self.lcdNumber_Blue_Display.setObjectName(u"lcdNumber_Blue_Display")
        self.lcdNumber_Blue_Display.setFont(font)
        self.lcdNumber_Blue_Display.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Blue_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Display.setLineWidth(0)
        self.lcdNumber_Blue_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Blue_Display, 2, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_14.addWidget(self.label_26, 2, 0, 1, 1)

        self.BlueSlider_Display = QSlider(self.groupBox_4)
        self.BlueSlider_Display.setObjectName(u"BlueSlider_Display")
        self.BlueSlider_Display.setMaximum(255)
        self.BlueSlider_Display.setValue(50)
        self.BlueSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.BlueSlider_Display, 2, 1, 1, 1)

        self.TrancSlider_Display = QSlider(self.groupBox_4)
        self.TrancSlider_Display.setObjectName(u"TrancSlider_Display")
        self.TrancSlider_Display.setMaximum(255)
        self.TrancSlider_Display.setValue(255)
        self.TrancSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.TrancSlider_Display, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_Display = QLCDNumber(self.groupBox_4)
        self.lcdNumber_Trancparency_Display.setObjectName(u"lcdNumber_Trancparency_Display")
        self.lcdNumber_Trancparency_Display.setFont(font)
        self.lcdNumber_Trancparency_Display.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Trancparency_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Display.setLineWidth(0)
        self.lcdNumber_Trancparency_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Trancparency_Display, 3, 2, 1, 1)

        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_14.addWidget(self.label_27, 0, 0, 1, 1)

        self.RedSlider_Display = QSlider(self.groupBox_4)
        self.RedSlider_Display.setObjectName(u"RedSlider_Display")
        self.RedSlider_Display.setMaximum(255)
        self.RedSlider_Display.setValue(50)
        self.RedSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.RedSlider_Display, 0, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.gridLayout_15.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.Parameter.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.lcdNumber_Red_2 = QLCDNumber(self.tab_2)
        self.lcdNumber_Red_2.setObjectName(u"lcdNumber_Red_2")
        self.lcdNumber_Red_2.setFont(font)
        self.lcdNumber_Red_2.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Red_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_2.setLineWidth(0)
        self.lcdNumber_Red_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_Red_2, 0, 2, 1, 1)

        self.MaxValueSlider = QSlider(self.tab_2)
        self.MaxValueSlider.setObjectName(u"MaxValueSlider")
        self.MaxValueSlider.setMaximum(1100)
        self.MaxValueSlider.setSingleStep(10)
        self.MaxValueSlider.setValue(1100)
        self.MaxValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MaxValueSlider, 1, 1, 1, 1)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 3, 0, 1, 1)

        self.lcdNumber_Green_2 = QLCDNumber(self.tab_2)
        self.lcdNumber_Green_2.setObjectName(u"lcdNumber_Green_2")
        self.lcdNumber_Green_2.setFont(font)
        self.lcdNumber_Green_2.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Green_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_2.setLineWidth(0)
        self.lcdNumber_Green_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_Green_2, 1, 2, 1, 1)

        self.lcdNumber_Blue_2 = QLCDNumber(self.tab_2)
        self.lcdNumber_Blue_2.setObjectName(u"lcdNumber_Blue_2")
        self.lcdNumber_Blue_2.setFont(font)
        self.lcdNumber_Blue_2.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Blue_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_2.setLineWidth(0)
        self.lcdNumber_Blue_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_Blue_2.setProperty("intValue", 11)

        self.gridLayout_7.addWidget(self.lcdNumber_Blue_2, 2, 2, 1, 1)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)

        self.MainGridSlider = QSlider(self.tab_2)
        self.MainGridSlider.setObjectName(u"MainGridSlider")
        self.MainGridSlider.setMinimum(1)
        self.MainGridSlider.setMaximum(16)
        self.MainGridSlider.setValue(11)
        self.MainGridSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MainGridSlider, 2, 1, 1, 1)

        self.TrancSlider_2 = QSlider(self.tab_2)
        self.TrancSlider_2.setObjectName(u"TrancSlider_2")
        self.TrancSlider_2.setMaximum(255)
        self.TrancSlider_2.setValue(255)
        self.TrancSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.TrancSlider_2, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_2 = QLCDNumber(self.tab_2)
        self.lcdNumber_Trancparency_2.setObjectName(u"lcdNumber_Trancparency_2")
        self.lcdNumber_Trancparency_2.setFont(font)
        self.lcdNumber_Trancparency_2.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.lcdNumber_Trancparency_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_2.setLineWidth(0)
        self.lcdNumber_Trancparency_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_Trancparency_2, 3, 2, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.MinValueSlider = QSlider(self.tab_2)
        self.MinValueSlider.setObjectName(u"MinValueSlider")
        self.MinValueSlider.setMaximum(100)
        self.MinValueSlider.setValue(0)
        self.MinValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MinValueSlider, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.Parameter.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.Parameter, 0, 4, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ActualSlider.valueChanged.connect(self.widget.update_value)
        self.ActualSlider.valueChanged.connect(self.lcdNumber_4.display)
        self.horizontalSlider_5.valueChanged.connect(self.lcdNumber_3.display)
        self.AussenRadiusSlider.valueChanged.connect(self.lcdNumber_2.display)
        self.InnenRadiusSlider.valueChanged.connect(self.lcdNumber.display)
        self.GaugeSizeSlider.valueChanged.connect(self.lcdNumber_8.display)
        self.GaugeStartSlider.valueChanged.connect(self.widget.set_start_scale_angle)
        self.GaugeSizeSlider.valueChanged.connect(self.widget.set_total_scale_angle_size)
        self.AussenRadiusSlider.valueChanged.connect(self.widget.set_gauge_color_outer_radius_factor)
        self.InnenRadiusSlider.valueChanged.connect(self.widget.set_gauge_color_inner_radius_factor)
        self.GaugeStartSlider.valueChanged.connect(self.lcdNumber_7.display)
        self.offsetSlider.valueChanged.connect(self.widget.update_angle_offset)
        self.offsetSlider.valueChanged.connect(self.lcdNumber_9.display)
        self.widget.valueChanged.connect(self.ActualSlider.setValue)
        self.RedSlider_Needle.valueChanged.connect(self.lcdNumber_Red_Needle.display)
        self.GreenSlider_Needle.valueChanged.connect(self.lcdNumber_Green_Needle.display)
        self.BlueSlider_Needle.valueChanged.connect(self.lcdNumber_Blue_Needle.display)
        self.TrancSlider_Needle.valueChanged.connect(self.lcdNumber_Trancparency_Needle.display)
        self.MinValueSlider.valueChanged.connect(self.widget.set_MinValue)
        self.MaxValueSlider.valueChanged.connect(self.widget.set_MaxValue)
        self.MaxValueSlider.valueChanged.connect(self.lcdNumber_Green_2.display)
        self.MinValueSlider.valueChanged.connect(self.lcdNumber_Red_2.display)
        self.MainGridSlider.valueChanged.connect(self.lcdNumber_Blue_2.display)
        self.TrancSlider_2.valueChanged.connect(self.lcdNumber_Trancparency_2.display)
        self.RedSlider_NeedleDrag.valueChanged.connect(self.lcdNumber_Red_NeedleDrag.display)
        self.GreenSlider_NeedleDrag.valueChanged.connect(self.lcdNumber_Green_NeedleDrag.display)
        self.BlueSlider_NeedleDrag.valueChanged.connect(self.lcdNumber_Blue_NeedleDrag.display)
        self.TrancSlider_NeedleDrag.valueChanged.connect(self.lcdNumber_Trancparency_NeedleDrag.display)
        self.RedSlider_Scale.valueChanged.connect(self.lcdNumber_Red_Scale.display)
        self.GreenSlider_Scale.valueChanged.connect(self.lcdNumber_Green_Scale.display)
        self.BlueSlider_Scale.valueChanged.connect(self.lcdNumber_Blue_Scale.display)
        self.TrancSlider_Scale.valueChanged.connect(self.lcdNumber_Trancparency_Scale.display)
        self.RedSlider_Display.valueChanged.connect(self.lcdNumber_Red_Display.display)
        self.GreenSlider_Display.valueChanged.connect(self.lcdNumber_Green_Display.display)
        self.BlueSlider_Display.valueChanged.connect(self.lcdNumber_Blue_Display.display)
        self.TrancSlider_Display.valueChanged.connect(self.lcdNumber_Trancparency_Display.display)
        self.MainGridSlider.valueChanged.connect(self.widget.set_scala_main_count)
        self.widget.valueChanged.connect(self.ActualValue.display)

        self.Parameter.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AnalogGaugeWidget_Demo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Value 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gauge Start", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"AussenRadius", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"InnenRadius", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gauge Size", None))
        self.CB_ScaleText.setText(QCoreApplication.translate("MainWindow", u"Show Scale Text", None))
        self.CB_Needle.setText(QCoreApplication.translate("MainWindow", u"Show Needle", None))
        self.CB_ShowBarGraph.setText(QCoreApplication.translate("MainWindow", u"Show BarGraph", None))
        self.CB_barGraph.setText(QCoreApplication.translate("MainWindow", u"Disable BarGraph Marker", None))
        self.CB_ValueText.setText(QCoreApplication.translate("MainWindow", u"Show Display", None))
        self.CB_CenterPoint.setText(QCoreApplication.translate("MainWindow", u"Show Center Point", None))
        self.CB_Grid.setText(QCoreApplication.translate("MainWindow", u"Show Scale Grid", None))
        self.CB_fineGrid.setText(QCoreApplication.translate("MainWindow", u"Show fine Scale Grid", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Needle: widget.set_NeedleColor(R=Red, G=Green, B=Blue, Transparency=Transparency)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"NeedleDrag: widget.set_NeedleColorDrag(R=Red, G=Green, B=Blue, Transparency=Transparency)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Skale", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Display Value", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Max Value", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Additional", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Grid Divider", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Min Value", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Min, Max Ranges", None))
    # retranslateUi

