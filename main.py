import logging
import sys

from ui.main_window import MainWindow

from ui.helpers.ui_helpers import (WindowProperties)

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        filename='system.log',
        filemode='a'
    )

    # sys.stdout = stream_logger.StreamToLogger(log, logginggit s.INFO)
    # sys.stderr = stream_logger.StreamToLogger(log, logging.ERROR)

    app = QApplication(sys.argv)

    pixmap = QPixmap(u':/logos/icons/images/zenex_small.png').scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    splash = QSplashScreen(pixmap)
    WindowProperties.center_window(splash)
    splash.show()
    app.processEvents()


    mainWin = MainWindow()

    splash.finish(mainWin)

    sys.exit(app.exec_())