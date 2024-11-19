# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_flow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_flow(object):
    def setupUi(self, Set_flow):
        Set_flow.setObjectName("Set_flow")
        Set_flow.resize(1021, 533)
        Set_flow.setMinimumSize(QtCore.QSize(1021, 533))
        Set_flow.setMaximumSize(QtCore.QSize(1021, 533))
        Set_flow.setModal(True)
        self.pBtnUseOnOff1_set_15 = QtWidgets.QPushButton(Set_flow)
        self.pBtnUseOnOff1_set_15.setGeometry(QtCore.QRect(10, 420, 1001, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnUseOnOff1_set_15.setFont(font)
        self.pBtnUseOnOff1_set_15.setObjectName("pBtnUseOnOff1_set_15")
        self.btn_set_irrigation_time_3 = QtWidgets.QPushButton(Set_flow)
        self.btn_set_irrigation_time_3.setGeometry(QtCore.QRect(10, 80, 321, 331))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_set_irrigation_time_3.setFont(font)
        self.btn_set_irrigation_time_3.setObjectName("btn_set_irrigation_time_3")
        self.btn_set_irrigation_flux_3 = QtWidgets.QPushButton(Set_flow)
        self.btn_set_irrigation_flux_3.setGeometry(QtCore.QRect(340, 80, 331, 331))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_set_irrigation_flux_3.setFont(font)
        self.btn_set_irrigation_flux_3.setObjectName("btn_set_irrigation_flux_3")
        self.btn_set_irrigation_dripper_3 = QtWidgets.QPushButton(Set_flow)
        self.btn_set_irrigation_dripper_3.setGeometry(QtCore.QRect(680, 80, 331, 241))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_set_irrigation_dripper_3.setFont(font)
        self.btn_set_irrigation_dripper_3.setObjectName("btn_set_irrigation_dripper_3")
        self.btn_set_irrigation_unit_3 = QtWidgets.QPushButton(Set_flow)
        self.btn_set_irrigation_unit_3.setGeometry(QtCore.QRect(680, 330, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_set_irrigation_unit_3.setFont(font)
        self.btn_set_irrigation_unit_3.setObjectName("btn_set_irrigation_unit_3")
        self.lblDispDate_3 = QtWidgets.QLabel(Set_flow)
        self.lblDispDate_3.setGeometry(QtCore.QRect(10, 10, 1001, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lblDispDate_3.setFont(font)
        self.lblDispDate_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDispDate_3.setObjectName("lblDispDate_3")

        self.retranslateUi(Set_flow)
        self.pBtnUseOnOff1_set_15.clicked.connect(Set_flow.set_cancel) # type: ignore
        self.btn_set_irrigation_time_3.clicked.connect(Set_flow.set_flow_time) # type: ignore
        self.btn_set_irrigation_flux_3.clicked.connect(Set_flow.set_flow_liter) # type: ignore
        self.btn_set_irrigation_dripper_3.clicked.connect(Set_flow.set_flow_dripper) # type: ignore
        self.btn_set_irrigation_unit_3.clicked.connect(Set_flow.set_flow_unit) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Set_flow)

    def retranslateUi(self, Set_flow):
        _translate = QtCore.QCoreApplication.translate
        Set_flow.setWindowTitle(_translate("Set_flow", "Dialog"))
        self.pBtnUseOnOff1_set_15.setText(_translate("Set_flow", "취소"))
        self.btn_set_irrigation_time_3.setText(_translate("Set_flow", "시간(S)"))
        self.btn_set_irrigation_flux_3.setText(_translate("Set_flow", "유량(L)"))
        self.btn_set_irrigation_dripper_3.setText(_translate("Set_flow", "드립퍼(cc)"))
        self.btn_set_irrigation_unit_3.setText(_translate("Set_flow", "0000"))
        self.lblDispDate_3.setText(_translate("Set_flow", "관수 방법 선택"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Set_flow = QtWidgets.QDialog()
    ui = Ui_Set_flow()
    ui.setupUi(Set_flow)
    Set_flow.show()
    sys.exit(app.exec_())
