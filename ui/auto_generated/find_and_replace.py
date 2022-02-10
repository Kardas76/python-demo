# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_and_replace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(569, 157)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)

        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 2)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(12)
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setFamily(u"MS Sans Serif")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.pushButton_2.setFont(font3)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.CANCELButton_3 = QPushButton(Dialog)
        self.CANCELButton_3.setObjectName(u"CANCELButton_3")
        self.CANCELButton_3.setFont(font2)

        self.verticalLayout.addWidget(self.CANCELButton_3)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label.setBuddy(self.lineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.CANCELButton_3.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Match Whole Word", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Match Case", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Replace:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Find:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Find", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Replace", None))
        self.CANCELButton_3.setText(QCoreApplication.translate("Dialog", u"&Cancel", None))
    # retranslateUi

