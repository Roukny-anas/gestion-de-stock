# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 429)
        self.description = QtWidgets.QLineEdit(Form)
        self.description.setGeometry(QtCore.QRect(150, 180, 113, 20))
        self.description.setText("")
        self.description.setObjectName("description")
        self.threshold = QtWidgets.QLineEdit(Form)
        self.threshold.setGeometry(QtCore.QRect(150, 300, 113, 20))
        self.threshold.setText("")
        self.threshold.setObjectName("threshold")
        self.unitprice = QtWidgets.QLineEdit(Form)
        self.unitprice.setGeometry(QtCore.QRect(150, 220, 113, 20))
        self.unitprice.setText("")
        self.unitprice.setObjectName("unitprice")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.name.setText("")
        self.name.setObjectName("name")
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.search.setObjectName("search")
        self.quantity = QtWidgets.QLineEdit(Form)
        self.quantity.setGeometry(QtCore.QRect(150, 260, 113, 20))
        self.quantity.setText("")
        self.quantity.setObjectName("quantity")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search.setText(_translate("Form", "chercher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
