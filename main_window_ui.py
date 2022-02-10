from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # Snip...

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sample Editor"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        # Snip...