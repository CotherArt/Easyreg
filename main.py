# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
from time import sleep
import pyperclip
import pickle

class Ui_MainWindow(object):
    registro = ''
    empleado_dic = {"empleado" : '00000', "extension" : '0000'}
    MainWindow = None
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/easyreg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_imei = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_imei.setFont(font)
        self.txt_imei.setCursorPosition(0)
        self.txt_imei.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_imei.setObjectName("txt_imei")
        self.gridLayout.addWidget(self.txt_imei, 2, 2, 1, 1)
        self.btn_copy_imei = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy_imei.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_imei.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy_imei.setIcon(icon1)
        self.btn_copy_imei.setObjectName("btn_copy_imei")
        self.gridLayout.addWidget(self.btn_copy_imei, 2, 3, 1, 1)
        self.btn_copy_modelo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy_modelo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_modelo.setText("")
        self.btn_copy_modelo.setIcon(icon1)
        self.btn_copy_modelo.setObjectName("btn_copy_modelo")
        self.gridLayout.addWidget(self.btn_copy_modelo, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.txt_dn = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_dn.setFont(font)
        self.txt_dn.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_dn.setObjectName("txt_dn")
        self.gridLayout.addWidget(self.txt_dn, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.txt_modelo = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_modelo.setFont(font)
        self.txt_modelo.setAutoFillBackground(False)
        self.txt_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_modelo.setObjectName("txt_modelo")
        self.gridLayout.addWidget(self.txt_modelo, 3, 2, 1, 1)
        self.btn_copy_dn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy_dn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_dn.setText("")
        self.btn_copy_dn.setIcon(icon1)
        self.btn_copy_dn.setObjectName("btn_copy_dn")
        self.gridLayout.addWidget(self.btn_copy_dn, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.btn_borrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_borrar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_borrar.setIcon(icon2)
        self.btn_borrar.setObjectName("btn_borrar")
        self.gridLayout.addWidget(self.btn_borrar, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_reportes = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_reportes.setObjectName("groupBox_reportes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_reportes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_datos = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_datos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_datos.setIcon(icon3)
        self.btn_datos.setObjectName("btn_datos")
        self.gridLayout_3.addWidget(self.btn_datos, 0, 4, 1, 1)
        self.btn_general = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_general.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/no_service.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_general.setIcon(icon4)
        self.btn_general.setObjectName("btn_general")
        self.gridLayout_3.addWidget(self.btn_general, 0, 0, 1, 1)
        self.btn_equiv = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_equiv.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/wrong_call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_equiv.setIcon(icon5)
        self.btn_equiv.setObjectName("btn_equiv")
        self.gridLayout_3.addWidget(self.btn_equiv, 1, 0, 1, 1)
        self.btn_sms = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_sms.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sms.setIcon(icon6)
        self.btn_sms.setObjectName("btn_sms")
        self.gridLayout_3.addWidget(self.btn_sms, 0, 5, 1, 1)
        self.btn_llamadas = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_llamadas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_llamadas.setIcon(icon7)
        self.btn_llamadas.setObjectName("btn_llamadas")
        self.gridLayout_3.addWidget(self.btn_llamadas, 0, 2, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/cancelation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon8)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_3.addWidget(self.btn_cancel, 1, 2, 1, 1)
        self.btn_tramites = QtWidgets.QPushButton(self.groupBox_reportes)
        self.btn_tramites.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/tramite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tramites.setIcon(icon9)
        self.btn_tramites.setObjectName("btn_tramites")
        self.gridLayout_3.addWidget(self.btn_tramites, 1, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_reportes, 1, 0, 1, 1)
        self.groupBox_tramites = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_tramites.setObjectName("groupBox_tramites")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_tramites)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_porta = QtWidgets.QPushButton(self.groupBox_tramites)
        self.btn_porta.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/portability.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_porta.setIcon(icon10)
        self.btn_porta.setObjectName("btn_porta")
        self.verticalLayout.addWidget(self.btn_porta)
        self.btn_barring = QtWidgets.QPushButton(self.groupBox_tramites)
        self.btn_barring.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/barring.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_barring.setIcon(icon11)
        self.btn_barring.setObjectName("btn_barring")
        self.verticalLayout.addWidget(self.btn_barring)
        self.btn_suspend = QtWidgets.QPushButton(self.groupBox_tramites)
        self.btn_suspend.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_suspend.setIcon(icon11)
        self.btn_suspend.setObjectName("btn_suspend")
        self.verticalLayout.addWidget(self.btn_suspend)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.groupBox_extra = QtWidgets.QGroupBox(self.groupBox_tramites)
        self.groupBox_extra.setObjectName("groupBox_extra")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_extra)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_copy_iccid = QtWidgets.QPushButton(self.groupBox_extra)
        self.btn_copy_iccid.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_iccid.setText("")
        self.btn_copy_iccid.setIcon(icon1)
        self.btn_copy_iccid.setObjectName("btn_copy_iccid")
        self.gridLayout_4.addWidget(self.btn_copy_iccid, 0, 2, 1, 1)
        self.txt_nip = QtWidgets.QLineEdit(self.groupBox_extra)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_nip.setFont(font)
        self.txt_nip.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_nip.setObjectName("txt_nip")
        self.gridLayout_4.addWidget(self.txt_nip, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_extra)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_extra)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.txt_iccid = QtWidgets.QLineEdit(self.groupBox_extra)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_iccid.setFont(font)
        self.txt_iccid.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_iccid.setObjectName("txt_iccid")
        self.gridLayout_4.addWidget(self.txt_iccid, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_extra)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.txt_dn2p = QtWidgets.QLineEdit(self.groupBox_extra)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_dn2p.setFont(font)
        self.txt_dn2p.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_dn2p.setObjectName("txt_dn2p")
        self.gridLayout_4.addWidget(self.txt_dn2p, 2, 1, 1, 1)
        self.btn_copy_nip = QtWidgets.QPushButton(self.groupBox_extra)
        self.btn_copy_nip.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_nip.setText("")
        self.btn_copy_nip.setIcon(icon1)
        self.btn_copy_nip.setObjectName("btn_copy_nip")
        self.gridLayout_4.addWidget(self.btn_copy_nip, 1, 2, 1, 1)
        self.btn_copy_dn2p = QtWidgets.QPushButton(self.groupBox_extra)
        self.btn_copy_dn2p.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_dn2p.setText("")
        self.btn_copy_dn2p.setIcon(icon1)
        self.btn_copy_dn2p.setObjectName("btn_copy_dn2p")
        self.gridLayout_4.addWidget(self.btn_copy_dn2p, 2, 2, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_extra)
        self.gridLayout_2.addWidget(self.groupBox_tramites, 4, 0, 1, 1)
        self.groupBox_registro = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_registro.setObjectName("groupBox_registro")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_registro)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_registro = QtWidgets.QTextEdit(self.groupBox_registro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_registro.sizePolicy().hasHeightForWidth())
        self.txt_registro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_registro.setFont(font)
        self.txt_registro.setObjectName("txt_registro")
        self.horizontalLayout_2.addWidget(self.txt_registro)
        self.btn_copy_reg = QtWidgets.QPushButton(self.groupBox_registro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copy_reg.sizePolicy().hasHeightForWidth())
        self.btn_copy_reg.setSizePolicy(sizePolicy)
        self.btn_copy_reg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_copy_reg.setIcon(icon1)
        self.btn_copy_reg.setCheckable(False)
        self.btn_copy_reg.setObjectName("btn_copy_reg")
        self.horizontalLayout_2.addWidget(self.btn_copy_reg)
        self.gridLayout_2.addWidget(self.groupBox_registro, 7, 0, 1, 1)
        self.groupBox_proced = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_proced.setObjectName("groupBox_proced")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_proced)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_vozapp = QtWidgets.QPushButton(self.groupBox_proced)
        self.btn_vozapp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/playstore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_vozapp.setIcon(icon12)
        self.btn_vozapp.setObjectName("btn_vozapp")
        self.gridLayout_5.addWidget(self.btn_vozapp, 0, 1, 1, 1)
        self.btn_confgen = QtWidgets.QPushButton(self.groupBox_proced)
        self.btn_confgen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_confgen.setIcon(icon13)
        self.btn_confgen.setObjectName("btn_confgen")
        self.gridLayout_5.addWidget(self.btn_confgen, 0, 0, 1, 1)
        self.btn_2level = QtWidgets.QPushButton(self.groupBox_proced)
        self.btn_2level.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/2level.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2level.setIcon(icon14)
        self.btn_2level.setObjectName("btn_2level")
        self.gridLayout_5.addWidget(self.btn_2level, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_proced, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 21))
        self.menubar.setObjectName("menubar")
        self.menuEmpezar = QtWidgets.QMenu(self.menubar)
        self.menuEmpezar.setObjectName("menuEmpezar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Empleado = QtWidgets.QAction(MainWindow)
        self.action_Empleado.setObjectName("action_Empleado")
        self.action_Extension = QtWidgets.QAction(MainWindow)
        self.action_Extension.setObjectName("action_Extension")
        self.actionSiempre_visible = QtWidgets.QAction(MainWindow)
        self.actionSiempre_visible.setObjectName("actionSiempre_visible")
        self.menuEmpezar.addAction(self.action_Empleado)
        self.menuEmpezar.addAction(self.action_Extension)
        self.menuOpciones.addAction(self.actionSiempre_visible)
        self.menubar.addAction(self.menuEmpezar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_dn, self.txt_imei)
        MainWindow.setTabOrder(self.txt_imei, self.txt_modelo)
        MainWindow.setTabOrder(self.txt_modelo, self.btn_general)
        MainWindow.setTabOrder(self.btn_general, self.btn_llamadas)
        MainWindow.setTabOrder(self.btn_llamadas, self.btn_datos)
        MainWindow.setTabOrder(self.btn_datos, self.btn_sms)
        MainWindow.setTabOrder(self.btn_sms, self.btn_equiv)
        MainWindow.setTabOrder(self.btn_equiv, self.btn_cancel)
        MainWindow.setTabOrder(self.btn_cancel, self.btn_tramites)
        MainWindow.setTabOrder(self.btn_tramites, self.btn_confgen)
        MainWindow.setTabOrder(self.btn_confgen, self.btn_vozapp)
        MainWindow.setTabOrder(self.btn_vozapp, self.btn_2level)
        MainWindow.setTabOrder(self.btn_2level, self.txt_iccid)
        MainWindow.setTabOrder(self.txt_iccid, self.txt_nip)
        MainWindow.setTabOrder(self.txt_nip, self.txt_dn2p)
        MainWindow.setTabOrder(self.txt_dn2p, self.btn_porta)
        MainWindow.setTabOrder(self.btn_porta, self.btn_barring)
        MainWindow.setTabOrder(self.btn_barring, self.btn_suspend)
        MainWindow.setTabOrder(self.btn_suspend, self.txt_registro)
        MainWindow.setTabOrder(self.txt_registro, self.btn_copy_reg)
        MainWindow.setTabOrder(self.btn_copy_reg, self.btn_copy_dn)
        MainWindow.setTabOrder(self.btn_copy_dn, self.btn_copy_imei)
        MainWindow.setTabOrder(self.btn_copy_imei, self.btn_copy_modelo)
        MainWindow.setTabOrder(self.btn_copy_modelo, self.btn_copy_iccid)
        MainWindow.setTabOrder(self.btn_copy_iccid, self.btn_copy_nip)
        MainWindow.setTabOrder(self.btn_copy_nip, self.btn_copy_dn2p)
        MainWindow.setTabOrder(self.btn_copy_dn2p, self.btn_borrar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easyreg"))
        self.label_2.setText(_translate("MainWindow", "IMEI:"))
        self.label.setText(_translate("MainWindow", "DN:"))
        self.label_3.setText(_translate("MainWindow", "MODELO:"))
        self.btn_borrar.setText(_translate("MainWindow", "Borrar todo"))
        self.groupBox_reportes.setTitle(_translate("MainWindow", "Reporte"))
        self.btn_datos.setText(_translate("MainWindow", "Datos"))
        self.btn_general.setText(_translate("MainWindow", "General"))
        self.btn_equiv.setText(_translate("MainWindow", "Equivocada"))
        self.btn_sms.setText(_translate("MainWindow", "SMS"))
        self.btn_llamadas.setText(_translate("MainWindow", "Llamadas"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelación"))
        self.btn_tramites.setText(_translate("MainWindow", "Tramites"))
        self.groupBox_tramites.setTitle(_translate("MainWindow", "Tramites"))
        self.btn_porta.setText(_translate("MainWindow", "Portabilidad"))
        self.btn_barring.setText(_translate("MainWindow", "Barring"))
        self.btn_suspend.setText(_translate("MainWindow", "Suspend"))
        self.groupBox_extra.setTitle(_translate("MainWindow", "Extra"))
        self.label_4.setText(_translate("MainWindow", "ICCID:"))
        self.label_5.setText(_translate("MainWindow", "NIP:"))
        self.label_6.setText(_translate("MainWindow", "DN 2P:"))
        self.groupBox_registro.setTitle(_translate("MainWindow", "Registro"))
        self.btn_copy_reg.setText(_translate("MainWindow", "Copiar"))
        self.btn_copy_reg.setShortcut(_translate("MainWindow", "Return"))
        self.groupBox_proced.setTitle(_translate("MainWindow", "Procedimiento"))
        self.btn_vozapp.setText(_translate("MainWindow", "Vozapp"))
        self.btn_confgen.setText(_translate("MainWindow", "Conf. gen"))
        self.btn_2level.setText(_translate("MainWindow", "2 nivel"))
        self.menuEmpezar.setTitle(_translate("MainWindow", "Editar"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones"))
        self.action_Empleado.setText(_translate("MainWindow", "#Empleado"))
        self.action_Extension.setText(_translate("MainWindow", "#Extension"))
        self.actionSiempre_visible.setText(_translate("MainWindow", "Siempre visible"))

    def setupFunctions(self):
        self.load_empleado()

        self.btn_general.setCheckable(True)
        self.btn_llamadas.setCheckable(True)
        self.btn_datos.setCheckable(True)
        self.btn_sms.setCheckable(True)
        self.btn_tramites.setCheckable(True)
        self.btn_confgen.setCheckable(True)
        self.btn_vozapp.setCheckable(True)
        self.btn_2level.setCheckable(True)

        # Buttons-----------------------------------
        self.btn_borrar.clicked.connect(self.reset)
        self.btn_general.clicked.connect(self.onClick_btn_general)
        self.btn_llamadas.clicked.connect(self.onClick_btn_llamadas)
        self.btn_datos.clicked.connect(self.onClick_btn_datos)
        self.btn_sms.clicked.connect(self.onClick_btn_sms)
        self.btn_tramites.clicked.connect(self.onClick_btn_tramites)

        self.action_Empleado.triggered.connect(self.onClick_empleado)
        self.action_Extension.triggered.connect(self.onClick_extension)
            # copy buttons--------------------------
        self.btn_copy_dn.clicked.connect(lambda: pyperclip.copy(self.txt_dn.text()))
        self.btn_copy_imei.clicked.connect(lambda: pyperclip.copy(self.txt_imei.text()))
        self.btn_copy_modelo.clicked.connect(lambda: pyperclip.copy(self.txt_modelo.text()))
        self.btn_copy_reg.clicked.connect(lambda: pyperclip.copy(self.txt_registro.toPlainText()))
        
        self.btn_copy_iccid.clicked.connect(lambda: pyperclip.copy(self.txt_iccid.text()))
        self.btn_copy_nip.clicked.connect(lambda: pyperclip.copy(self.txt_nip.text()))
        self.btn_copy_dn2p.clicked.connect(lambda: pyperclip.copy(self.txt_dn2p.text()))
        # Config------------------------------------
        self.btn_confgen.clicked.connect(self.update_registro)
        self.btn_vozapp.clicked.connect(self.update_registro)
        self.btn_2level.clicked.connect(self.update_registro) 

        
        self.txt_dn.textChanged.connect(self.update_registro)
        self.txt_imei.textChanged.connect(self.update_registro)
        self.txt_modelo.textChanged.connect(self.update_registro)


    def update_registro(self):
        self.registro = ''
        if self.txt_dn.text() != '':
            self.registro += 'dn:' + self.txt_dn.text()
        if self.txt_imei.text() != '':
            self.registro += '//imei:' + self.txt_imei.text()
        if self.txt_modelo.text() != '':
            self.registro += '//dn:' + self.txt_modelo.text()

        if self.btn_general.isChecked():
            self.registro += '//Cte no tiene servicio en su linea de megamobil'
        if self.btn_llamadas.isChecked():
            self.registro += '//Cte no tiene servicio de llamadas'
        if self.btn_datos.isChecked():
            self.registro += '//Cte no tiene servicio de datos'
        if self.btn_sms.isChecked():
            self.registro += '//Cte no tiene servicio de SMS'

        if self.btn_confgen.isChecked():
            self.registro += '//Se activan los datos, el roaming, se configura APN, modo de red, se fuerza el operador de red'
        if self.btn_vozapp.isChecked():
            self.registro += '//Se configura vozapp'
        if self.btn_2level.isChecked():
            self.registro += '//Se genera reporte de 2do nivel'
        self.registro += '//' + self.empleado_dic.get('empleado') + '//' + self.empleado_dic.get('extension')

        # print(self.registro)
        self.txt_registro.setText(self.registro)
        
# Button actions -----------------------------------
    def onClick_btn_general(self):
        self.groupBox_proced.setVisible(True)
        self.update_registro()

    def onClick_btn_llamadas(self):
        self.groupBox_proced.setVisible(True)
        self.update_registro()
    
    def onClick_btn_datos(self):
        self.groupBox_proced.setVisible(True)
        self.update_registro()
    
    def onClick_btn_sms(self):
        self.groupBox_proced.setVisible(True)
        self.update_registro()

    def onClick_btn_tramites(self):
        self.groupBox_tramites.setVisible(True)

    def onClick_btn_confgen(self):
        self.update_registro()

    def onClick_empleado(self):
        empleado, ok = QInputDialog.getText(self.MainWindow, '#Empleado', 'Ingresa tu numero de empleado:')
        if ok:
            self.empleado_dic['empleado'] = empleado
            self.save_empleado()
	
    def onClick_extension(self):
        extension, ok = QInputDialog.getText(self.MainWindow, '#Extension', 'Ingresa tu numero de extension:')
        if ok:
            self.empleado_dic['extension'] = extension
            self.save_empleado()

    def save_empleado(self):
        with open('empleado.uwu', 'wb') as handle:
            pickle.dump(self.empleado_dic, handle)
            self.set_menu_empezar()


    def load_empleado(self):
        from os.path import exists
        file_exists = exists('empleado.uwu')
        if not file_exists:
            self.save_empleado()
        with open('empleado.uwu', 'rb') as handle:
            self.empleado_dic = pickle.loads(handle.read())
            self.set_menu_empezar()

    def set_menu_empezar(self): # Actualiza el nombre en el menu con los actuales valores de #Empleado y  #Extension
        self.action_Extension.setText('#Extension (' + self.empleado_dic.get('extension') + ')')
        self.action_Empleado.setText('#Empleado (' + self.empleado_dic.get('empleado') + ')')

    def reset(self):
        self.txt_dn.clear()
        self.txt_imei.clear()
        self.txt_modelo.clear()
        self.txt_iccid.clear()
        self.txt_nip.clear()
        self.txt_dn2p.clear()
        self.txt_registro.clear()
        self.groupBox_proced.setVisible(False)
        self.groupBox_tramites.setVisible(False)
        
        self.btn_general.setChecked(False)
        self.btn_llamadas.setChecked(False)
        self.btn_datos.setChecked(False)
        self.btn_sms.setChecked(False)
        self.btn_tramites.setChecked(False)

        self.btn_vozapp.setChecked(False)
        self.btn_confgen.setChecked(False)
        self.btn_2level.setChecked(False)

        self.MainWindow.resize(374, 300)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.reset()
    ui.setupFunctions()
    MainWindow.show()
    sys.exit(app.exec_())
