# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eval_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 739)
        MainWindow.setMinimumSize(QtCore.QSize(720, 739))
        MainWindow.setMaximumSize(QtCore.QSize(998, 886))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Calc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelCalc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCalc.setFont(font)
        self.labelCalc.setObjectName("labelCalc")
        self.horizontalLayout_2.addWidget(self.labelCalc)
        self.textCalc = MyTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textCalc.setFont(font)
        self.textCalc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textCalc.setObjectName("textCalc")
        self.horizontalLayout_2.addWidget(self.textCalc)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelRez = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRez.setFont(font)
        self.labelRez.setObjectName("labelRez")
        self.horizontalLayout_3.addWidget(self.labelRez)
        self.txtRez = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtRez.setFont(font)
        self.txtRez.setObjectName("txtRez")
        self.horizontalLayout_3.addWidget(self.txtRez)
        self.horizontalLayout_3.setStretch(1, 10)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.checkBSel = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBSel.setFont(font)
        self.checkBSel.setChecked(True)
        self.checkBSel.setObjectName("checkBSel")
        self.gridLayout.addWidget(self.checkBSel, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelRez_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelRez_2.setMaximumSize(QtCore.QSize(59, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRez_2.setFont(font)
        self.labelRez_2.setObjectName("labelRez_2")
        self.horizontalLayout_4.addWidget(self.labelRez_2)
        self.spin_precision = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_precision.setMaximumSize(QtCore.QSize(36, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_precision.setFont(font)
        self.spin_precision.setMaximum(16)
        self.spin_precision.setObjectName("spin_precision")
        self.horizontalLayout_4.addWidget(self.spin_precision)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.groupRad = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRad.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupRad.setFont(font)
        self.groupRad.setObjectName("groupRad")
        self.radioB_rad = QtWidgets.QRadioButton(self.groupRad)
        self.radioB_rad.setGeometry(QtCore.QRect(10, 26, 89, 17))
        self.radioB_rad.setCheckable(True)
        self.radioB_rad.setChecked(False)
        self.radioB_rad.setObjectName("radioB_rad")
        self.radioB_Deg = QtWidgets.QRadioButton(self.groupRad)
        self.radioB_Deg.setGeometry(QtCore.QRect(10, 48, 89, 17))
        self.radioB_Deg.setObjectName("radioB_Deg")
        self.gridLayout.addWidget(self.groupRad, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushB_Calc = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_Calc.setFont(font)
        self.pushB_Calc.setObjectName("pushB_Calc")
        self.horizontalLayout_5.addWidget(self.pushB_Calc)
        self.pushB_Clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_Clear.setFont(font)
        self.pushB_Clear.setObjectName("pushB_Clear")
        self.horizontalLayout_5.addWidget(self.pushB_Clear)
        self.pushB_Save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_Save.setFont(font)
        self.pushB_Save.setObjectName("pushB_Save")
        self.horizontalLayout_5.addWidget(self.pushB_Save)
        self.pushB_Exit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_Exit.setFont(font)
        self.pushB_Exit.setObjectName("pushB_Exit")
        self.horizontalLayout_5.addWidget(self.pushB_Exit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 683, 1066))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushB_cons0 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons0.sizePolicy().hasHeightForWidth())
        self.pushB_cons0.setSizePolicy(sizePolicy)
        self.pushB_cons0.setObjectName("pushB_cons0")
        self.horizontalLayout_6.addWidget(self.pushB_cons0)
        self.pushB_cons1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons1.sizePolicy().hasHeightForWidth())
        self.pushB_cons1.setSizePolicy(sizePolicy)
        self.pushB_cons1.setObjectName("pushB_cons1")
        self.horizontalLayout_6.addWidget(self.pushB_cons1)
        self.pushB_cons2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons2.sizePolicy().hasHeightForWidth())
        self.pushB_cons2.setSizePolicy(sizePolicy)
        self.pushB_cons2.setObjectName("pushB_cons2")
        self.horizontalLayout_6.addWidget(self.pushB_cons2)
        self.pushB_cons3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons3.sizePolicy().hasHeightForWidth())
        self.pushB_cons3.setSizePolicy(sizePolicy)
        self.pushB_cons3.setObjectName("pushB_cons3")
        self.horizontalLayout_6.addWidget(self.pushB_cons3)
        self.pushB_cons4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons4.sizePolicy().hasHeightForWidth())
        self.pushB_cons4.setSizePolicy(sizePolicy)
        self.pushB_cons4.setObjectName("pushB_cons4")
        self.horizontalLayout_6.addWidget(self.pushB_cons4)
        self.pushB_cons5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons5.sizePolicy().hasHeightForWidth())
        self.pushB_cons5.setSizePolicy(sizePolicy)
        self.pushB_cons5.setObjectName("pushB_cons5")
        self.horizontalLayout_6.addWidget(self.pushB_cons5)
        self.pushB_cons6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons6.sizePolicy().hasHeightForWidth())
        self.pushB_cons6.setSizePolicy(sizePolicy)
        self.pushB_cons6.setObjectName("pushB_cons6")
        self.horizontalLayout_6.addWidget(self.pushB_cons6)
        self.pushB_cons7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons7.sizePolicy().hasHeightForWidth())
        self.pushB_cons7.setSizePolicy(sizePolicy)
        self.pushB_cons7.setObjectName("pushB_cons7")
        self.horizontalLayout_6.addWidget(self.pushB_cons7)
        self.pushB_cons8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons8.sizePolicy().hasHeightForWidth())
        self.pushB_cons8.setSizePolicy(sizePolicy)
        self.pushB_cons8.setObjectName("pushB_cons8")
        self.horizontalLayout_6.addWidget(self.pushB_cons8)
        self.pushB_cons9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_cons9.sizePolicy().hasHeightForWidth())
        self.pushB_cons9.setSizePolicy(sizePolicy)
        self.pushB_cons9.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.pushB_cons9.setObjectName("pushB_cons9")
        self.horizontalLayout_6.addWidget(self.pushB_cons9)
        self.pushB_conspoint = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushB_conspoint.sizePolicy().hasHeightForWidth())
        self.pushB_conspoint.setSizePolicy(sizePolicy)
        self.pushB_conspoint.setObjectName("pushB_conspoint")
        self.horizontalLayout_6.addWidget(self.pushB_conspoint)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushB_consplus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_consplus.setObjectName("pushB_consplus")
        self.horizontalLayout.addWidget(self.pushB_consplus)
        self.pushB_consminus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_consminus.setObjectName("pushB_consminus")
        self.horizontalLayout.addWidget(self.pushB_consminus)
        self.pushB_consmult = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_consmult.setObjectName("pushB_consmult")
        self.horizontalLayout.addWidget(self.pushB_consmult)
        self.pushB_consdev = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_consdev.setObjectName("pushB_consdev")
        self.horizontalLayout.addWidget(self.pushB_consdev)
        self.pushB_consdegree = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_consdegree.setObjectName("pushB_consdegree")
        self.horizontalLayout.addWidget(self.pushB_consdegree)
        self.pushBf_brackets = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_brackets.setObjectName("pushBf_brackets")
        self.horizontalLayout.addWidget(self.pushBf_brackets)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushBf_fabs = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushBf_fabs.setFont(font)
        self.pushBf_fabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushBf_fabs.setObjectName("pushBf_fabs")
        self.verticalLayout.addWidget(self.pushBf_fabs)
        self.pushBf_factorial = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_factorial.setObjectName("pushBf_factorial")
        self.verticalLayout.addWidget(self.pushBf_factorial)
        self.pushBf_exp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_exp.setObjectName("pushBf_exp")
        self.verticalLayout.addWidget(self.pushBf_exp)
        self.pushBf_log10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_log10.setObjectName("pushBf_log10")
        self.verticalLayout.addWidget(self.pushBf_log10)
        self.pushBf_log2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_log2.setObjectName("pushBf_log2")
        self.verticalLayout.addWidget(self.pushBf_log2)
        self.pushBf_loge = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_loge.setObjectName("pushBf_loge")
        self.verticalLayout.addWidget(self.pushBf_loge)
        self.pushBf_log = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_log.setObjectName("pushBf_log")
        self.verticalLayout.addWidget(self.pushBf_log)
        self.pushBf_pow = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_pow.setObjectName("pushBf_pow")
        self.verticalLayout.addWidget(self.pushBf_pow)
        self.pushBf_sqrt = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_sqrt.setObjectName("pushBf_sqrt")
        self.verticalLayout.addWidget(self.pushBf_sqrt)
        self.pushBf_sin = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_sin.setObjectName("pushBf_sin")
        self.verticalLayout.addWidget(self.pushBf_sin)
        self.pushBf_cos = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_cos.setObjectName("pushBf_cos")
        self.verticalLayout.addWidget(self.pushBf_cos)
        self.pushBf_tan = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_tan.setObjectName("pushBf_tan")
        self.verticalLayout.addWidget(self.pushBf_tan)
        self.pushBf_ctan = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_ctan.setObjectName("pushBf_ctan")
        self.verticalLayout.addWidget(self.pushBf_ctan)
        self.pushBf_asin = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_asin.setObjectName("pushBf_asin")
        self.verticalLayout.addWidget(self.pushBf_asin)
        self.pushBf_acos = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_acos.setObjectName("pushBf_acos")
        self.verticalLayout.addWidget(self.pushBf_acos)
        self.pushBf_atan = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_atan.setObjectName("pushBf_atan")
        self.verticalLayout.addWidget(self.pushBf_atan)
        self.pushBf_ctanh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_ctanh.setObjectName("pushBf_ctanh")
        self.verticalLayout.addWidget(self.pushBf_ctanh)
        self.pushBf_atan2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_atan2.setObjectName("pushBf_atan2")
        self.verticalLayout.addWidget(self.pushBf_atan2)
        self.pushBf_sinh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_sinh.setObjectName("pushBf_sinh")
        self.verticalLayout.addWidget(self.pushBf_sinh)
        self.pushBf_cosh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_cosh.setObjectName("pushBf_cosh")
        self.verticalLayout.addWidget(self.pushBf_cosh)
        self.pushBf_tanh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_tanh.setObjectName("pushBf_tanh")
        self.verticalLayout.addWidget(self.pushBf_tanh)
        self.pushBf_ctanh_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_ctanh_2.setObjectName("pushBf_ctanh_2")
        self.verticalLayout.addWidget(self.pushBf_ctanh_2)
        self.pushBf_asinh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_asinh.setObjectName("pushBf_asinh")
        self.verticalLayout.addWidget(self.pushBf_asinh)
        self.pushBf_acosh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_acosh.setObjectName("pushBf_acosh")
        self.verticalLayout.addWidget(self.pushBf_acosh)
        self.pushBf_atanh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_atanh.setObjectName("pushBf_atanh")
        self.verticalLayout.addWidget(self.pushBf_atanh)
        self.pushBf_actanh = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_actanh.setObjectName("pushBf_actanh")
        self.verticalLayout.addWidget(self.pushBf_actanh)
        self.pushBf_gamma = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_gamma.setObjectName("pushBf_gamma")
        self.verticalLayout.addWidget(self.pushBf_gamma)
        self.pushBf_lgamma = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_lgamma.setObjectName("pushBf_lgamma")
        self.verticalLayout.addWidget(self.pushBf_lgamma)
        self.pushBf_hypot = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_hypot.setObjectName("pushBf_hypot")
        self.verticalLayout.addWidget(self.pushBf_hypot)
        self.pushBf_degrees = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_degrees.setObjectName("pushBf_degrees")
        self.verticalLayout.addWidget(self.pushBf_degrees)
        self.pushBf_radians = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushBf_radians.setObjectName("pushBf_radians")
        self.verticalLayout.addWidget(self.pushBf_radians)
        self.pushB_conspi = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_conspi.setObjectName("pushB_conspi")
        self.verticalLayout.addWidget(self.pushB_conspi)
        self.pushB_conse = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushB_conse.setObjectName("pushB_conse")
        self.verticalLayout.addWidget(self.pushB_conse)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textCalc, self.checkBSel)
        MainWindow.setTabOrder(self.checkBSel, self.radioB_rad)
        MainWindow.setTabOrder(self.radioB_rad, self.radioB_Deg)
        MainWindow.setTabOrder(self.radioB_Deg, self.pushB_Calc)
        MainWindow.setTabOrder(self.pushB_Calc, self.pushB_Clear)
        MainWindow.setTabOrder(self.pushB_Clear, self.pushB_Save)
        MainWindow.setTabOrder(self.pushB_Save, self.pushB_Exit)
        MainWindow.setTabOrder(self.pushB_Exit, self.pushBf_fabs)
        MainWindow.setTabOrder(self.pushBf_fabs, self.pushBf_factorial)
        MainWindow.setTabOrder(self.pushBf_factorial, self.pushBf_exp)
        MainWindow.setTabOrder(self.pushBf_exp, self.pushBf_log)
        MainWindow.setTabOrder(self.pushBf_log, self.pushBf_pow)
        MainWindow.setTabOrder(self.pushBf_pow, self.pushBf_sqrt)
        MainWindow.setTabOrder(self.pushBf_sqrt, self.pushBf_acos)
        MainWindow.setTabOrder(self.pushBf_acos, self.pushBf_atan)
        MainWindow.setTabOrder(self.pushBf_atan, self.pushBf_atan2)
        MainWindow.setTabOrder(self.pushBf_atan2, self.pushBf_cosh)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор с выражением"))
        self.labelCalc.setText(_translate("MainWindow", "Выражение"))
        self.textCalc.setToolTip(_translate("MainWindow", "<html><head/><body><p>Поле для ввода выражения. В выражении можно задавать функции. Подробный синтаксический контроль выражения не производится. Если выражение задано неверно, или аргумент имеет недопустимое значение, то при расчете в поле <span style=\" font-weight:600; font-style:italic;\">Результат</span> выдается сообщение: <span style=\" font-weight:600;\">Ошибка в выражении и/или аргументах. </span><br/>При нажатии коавиши <span style=\" font-weight:600;\">Enter</span> просходит вычисление выражения.</p></body></html>"))
        self.labelRez.setText(_translate("MainWindow", "Результат"))
        self.txtRez.setText(_translate("MainWindow", "...."))
        self.checkBSel.setToolTip(_translate("MainWindow", "<html><head/><body><p>Если установлен этот флажок, то после рачета выражение выделяется. Если после рачета не снять выделение вручную, то при вводе данных в поле <span style=\" font-weight:600; font-style:italic;\">Выражение</span> выделяемый текст заменится на вводимый</p></body></html>"))
        self.checkBSel.setText(_translate("MainWindow", "Выделять выражение после расчета"))
        self.labelRez_2.setText(_translate("MainWindow", "Точность "))
        self.spin_precision.setToolTip(_translate("MainWindow", "<html><head/><body><p>Поле для ввода точности. Точность задается в дипозоне от 5 до 16. При этом подразумевается полная точность с учетом целой и дробной частей.</p></body></html>"))
        self.groupRad.setToolTip(_translate("MainWindow", "<html><head/><body><p>Тригонометрические функции могут вычисляться в радианах или градусах. Если есть необходимость вычислять одновременно в радианах и градусах, то можно использовать преобразование радиан в градусы или наоборот. Если задан вариант в градусах, то для расчета прямых тригонометрических функций в радианах можно использовать формулу типа <span style=\" font-weight:600;\">sin(radians(x))</span>, а для обратных <span style=\" font-weight:600;\">degrees(asin(x))</span>.  Если задан вариант в радианах, то для расчета прямых тригонометрических функций в градусах можно использовать формулу типа<span style=\" font-weight:600;\"> sin(degrees (x))</span>, а для обратных<span style=\" font-weight:600;\"> radians (asin(x))</span>.</p></body></html>"))
        self.groupRad.setTitle(_translate("MainWindow", "Тригонаметрические функции"))
        self.radioB_rad.setToolTip(_translate("MainWindow", "<html><head/><body><p>Если есть необходимость вычислять одновременно в радианах и градусах, то можно использовать преобразование радиан в градусы или наоборот. Если задан вариант в радианах, то для расчета прямых тригонометрических функций в градусах можно использовать формулу типа<span style=\" font-weight:600;\"> sin(degrees (x))</span>, а для обратных<span style=\" font-weight:600;\"> radians (asin(x))</span>.</p></body></html>"))
        self.radioB_rad.setText(_translate("MainWindow", "В радианах"))
        self.radioB_Deg.setToolTip(_translate("MainWindow", "<html><head/><body><p>Если есть необходимость вычислять одновременно в радианах и градусах, то можно использовать преобразование радиан в градусы или наоборот.  Если задан вариант в градусах, то для расчета прямых тригонометрических функций в радианах можно использовать формулу типа <span style=\" font-weight:600;\">sin(radians(x))</span>, а для обратных <span style=\" font-weight:600;\">degrees(asin(x))</span>.</p></body></html>"))
        self.radioB_Deg.setText(_translate("MainWindow", "В градусах"))
        self.pushB_Calc.setText(_translate("MainWindow", "Alt+E Вычислить"))
        self.pushB_Clear.setText(_translate("MainWindow", "Alt-C Очистить выражение"))
        self.pushB_Save.setText(_translate("MainWindow", "Alt-S Сохранить настройки"))
        self.pushB_Exit.setText(_translate("MainWindow", "Alt-F4 Выход"))
        self.pushB_cons0.setText(_translate("MainWindow", "0"))
        self.pushB_cons1.setText(_translate("MainWindow", "1"))
        self.pushB_cons2.setText(_translate("MainWindow", "2"))
        self.pushB_cons3.setText(_translate("MainWindow", "3"))
        self.pushB_cons4.setText(_translate("MainWindow", "4"))
        self.pushB_cons5.setText(_translate("MainWindow", "5"))
        self.pushB_cons6.setText(_translate("MainWindow", "6"))
        self.pushB_cons7.setText(_translate("MainWindow", "7"))
        self.pushB_cons8.setText(_translate("MainWindow", "8"))
        self.pushB_cons9.setText(_translate("MainWindow", "9"))
        self.pushB_conspoint.setText(_translate("MainWindow", "."))
        self.pushB_consplus.setText(_translate("MainWindow", "+"))
        self.pushB_consminus.setText(_translate("MainWindow", "-"))
        self.pushB_consmult.setText(_translate("MainWindow", "*"))
        self.pushB_consdev.setText(_translate("MainWindow", "/"))
        self.pushB_consdegree.setText(_translate("MainWindow", "^"))
        self.pushBf_brackets.setText(_translate("MainWindow", "()"))
        self.pushBf_fabs.setText(_translate("MainWindow", "abs(X) - модуль X"))
        self.pushBf_factorial.setText(_translate("MainWindow", "factorial(X) - факториал числа X"))
        self.pushBf_exp.setText(_translate("MainWindow", "exp(X) - e в степени X"))
        self.pushBf_log10.setText(_translate("MainWindow", "log10(X) - логарифм X по основанию 10"))
        self.pushBf_log2.setText(_translate("MainWindow", "lgb(X) - логарифм X по основанию 2"))
        self.pushBf_loge.setText(_translate("MainWindow", "ln(X) - логарифм наруральный X"))
        self.pushBf_log.setText(_translate("MainWindow", "log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм"))
        self.pushBf_pow.setText(_translate("MainWindow", "pow(X, Y) - X в степени Y. Можно использовать X^Y или X**Y"))
        self.pushBf_sqrt.setText(_translate("MainWindow", "sqrt(X) - квадратный корень из X"))
        self.pushBf_sin.setText(_translate("MainWindow", "sin(X) - синус X"))
        self.pushBf_cos.setText(_translate("MainWindow", "cos(X) - косинус X"))
        self.pushBf_tan.setText(_translate("MainWindow", "tg(X) - тангенс X"))
        self.pushBf_ctan.setText(_translate("MainWindow", "ctg(X) - котангенс X"))
        self.pushBf_asin.setText(_translate("MainWindow", "arcsin(X) - арксинус X"))
        self.pushBf_acos.setText(_translate("MainWindow", "arccos(X) - арккосинус X"))
        self.pushBf_atan.setText(_translate("MainWindow", "arctg(X) - арктангенс X"))
        self.pushBf_ctanh.setText(_translate("MainWindow", "arcctg(X) - арккотангенс X"))
        self.pushBf_atan2.setText(_translate("MainWindow", "atan2(Y, X) - арктангенс Y/X.  С учетом четверти, в которой находится точка (X, Y)"))
        self.pushBf_sinh.setText(_translate("MainWindow", "sh(X) - гиперболический синус X"))
        self.pushBf_cosh.setText(_translate("MainWindow", "ch(X) - гиперболический косинус X"))
        self.pushBf_tanh.setText(_translate("MainWindow", "th(X) - гиперболический тангенс X"))
        self.pushBf_ctanh_2.setText(_translate("MainWindow", "cth(X) - гиперболический котангенс X"))
        self.pushBf_asinh.setText(_translate("MainWindow", "arsh(X) -  обратный гиперболический синус X"))
        self.pushBf_acosh.setText(_translate("MainWindow", "arch(X) - обратный гиперболический косинус X"))
        self.pushBf_atanh.setText(_translate("MainWindow", "arth(X) - обратный гиперболический тангенс X"))
        self.pushBf_actanh.setText(_translate("MainWindow", "arcth(X) - обратный гиперболический котангенс X"))
        self.pushBf_gamma.setText(_translate("MainWindow", "gamma(X) - гамма-функция X"))
        self.pushBf_lgamma.setText(_translate("MainWindow", "lgamma(X) - натуральный логарифм гамма-функции X"))
        self.pushBf_hypot.setText(_translate("MainWindow", "hypot(X, Y) -  гипотенуза треугольника с катетами X и Y (sqrt(x * x + y * y))"))
        self.pushBf_degrees.setText(_translate("MainWindow", "degrees(X) - конвертирует радианы в градусы"))
        self.pushBf_radians.setText(_translate("MainWindow", "radians(X) - конвертирует градусы в радианы"))
        self.pushB_conspi.setText(_translate("MainWindow", "pi - число pi = 3,1415926...."))
        self.pushB_conse.setText(_translate("MainWindow", "e - число e = 2,718281...."))
from myclasses import MyTextEdit
import Eval_gui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
