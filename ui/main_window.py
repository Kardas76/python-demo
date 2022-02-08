import collections
import random
import sys
from datetime import date, datetime, timedelta
from enum import Enum

import pandas as pd
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QEvent,
                            QMetaObject, QObject, QPoint, QPropertyAnimation,
                            QRect, QSize, Qt, QTime, QUrl)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui.auto_generated.ui_main import *

from ui.helpers.ui_helpers import (FilterDateProxyModel, GlobalStrings,
                                   Highlighter, StylesLoader,
                                   WarningItemDelegate, WindowProperties)
from ui.styles.ui_styles import UIStyle

# from ui.auto_generated.common_docked_widget import *

class MainWindow(QMainWindow):
    WINDOW_TILTE_BAR = True

    WINDOW_STATUS = False

    InterfaceTypeRole = QtCore.Qt.UserRole + 1

    RECORDING_ENABLED = None


    mainwindow_previous_tab_name = None

    dashboard_ask_modbus_refresh_rate_ms = 1000
    dashboard_reload_refresh_rate_ms = 500

    last_device_id = None
    last_dashboard_result = None

    start_button = None

    dashboard_tableview = None

    dashboard_chart_view_real_time = None

    dashboard_chart_view_harmonics = None

    database_statistics_chart_view = None


    Dialog_with_window_properties_tuple = collections.namedtuple('Dialog_With_Window_Properties_Tuple', ['window_properties', 'dialog_window'])

    DIALOG_WINDOWSES = []


    START_SIZE = QSize(1280, 720)


    def __init__(self, parent=None):
        # QMainWindow.__init__(self, parent)

        super(MainWindow, self).__init__()

        self.integer_validator = QIntValidator()

        self.translations = self.internationalization_findQmFiles()
        self.m_translator = QtCore.QTranslator(self)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # self.ui.treeWidget_parameters_list.expandAll()

        WindowProperties.style_window(self)

        self.installEventFilter(self)

        self.setMouseTracking(True)

        # self.setWindowModality(QtCore.Qt.ApplicationModal)


        self.window_properties_initialization()
        self.window_offset_initialization()
        self.menu_initialization()
        self.window_maximalization_actions_initialization()

        self.window_slots_initialization()

        self.start_button.setFocus()
        self.start_button.click()

        self.show()

        # self.internationalization_change_language(self.translations[0])


##################### Page initialization #####################


    def internationalization_change_language(self, path):
        QtCore.QCoreApplication.instance().removeTranslator(self.m_translator)
        if self.m_translator.load(path):
            QtCore.QCoreApplication.instance().installTranslator(self.m_translator)


    def internationalization_findQmFiles(self):
        trans_dir = QtCore.QDir("./ui/forms")
        fileNames = trans_dir.entryList(["*.qm"], QtCore.QDir.Files, QtCore.QDir.Name)
        fileNames = [trans_dir.filePath(p) for p in fileNames]
        return fileNames
        

    def window_properties_initialization(self):
        self.setWindowTitle(GlobalStrings.program_tile)
        self.ui.label_title_bar_top.setText(GlobalStrings.program_tile)

        self.ui.label_top_info_1.setText(GlobalStrings.no_value_item_text)

        self.resize(MainWindow.START_SIZE)
        self.setMinimumSize(MainWindow.START_SIZE)

        WindowProperties.center_window(self)



    def window_offset_initialization(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        WindowProperties.initialize_frame_grips(self, True)


    def window_maximalization_actions_initialization(self):
        self.window_move_action_initialization()
        self.window_frame_settings()
        self.window_maximize_restore()


    def window_move_action_initialization(self):
        def moveWindow(event:QEvent):
            if self.WINDOW_STATUS == False:
                self.window_maximize_restore()

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow


    def window_frame_settings(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: self.window_maximize_restore())

        if self.WINDOW_TILTE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_btns_right.hide()

         
    def window_maximize_restore(self):
        status = self.WINDOW_STATUS
        print('window maximize restore')
        if status == True:
            self.showMaximized()
            self.WINDOW_STATUS = False
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip('Restore')
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u':/16x16/icons/16x16/cil-window-restore.png'))
            WindowProperties.set_grips_visibility(self, False)
        else:
            self.WINDOW_STATUS = True
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip('Maximize')
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u':/16x16/icons/16x16/cil-window-maximize.png'))
            WindowProperties.set_grips_visibility(self, True)


    # def window_enableMaximumSize(self, width, height):
    #     if width != '' and height != '':
    #         self.setMaximumSize(QSize(width, height))
    #         self.ui.btn_maximize_restore.hide()


    def window_slots_initialization(self):
        self.ui.btn_toggle_menu.clicked.connect(lambda: self.menu_toggleMenu(220, True))

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize_restore.clicked.connect(lambda: self.window_maximize_restore())
        self.ui.btn_close.clicked.connect(lambda: self.close())


    def menu_toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()



    def menu_initialization(self):
        self.ui.stackedWidget.setMinimumWidth(20)

        self.start_button = self.menu_addNewMenu(GlobalStrings.menu_dashboard_title, 'btn_dashboard', 'url(:/16x16/icons/16x16/cil-home.png)', True)
        
        self.menu_addNewMenu(GlobalStrings.menu_data_title, 'btn_data', 'url(:/16x16/icons/16x16/cil-chart-line.png)', True)

        self.menu_addNewMenu(GlobalStrings.menu_settings_title, 'btn_devices_settings', 'url(:/16x16/icons/16x16/cil-settings.png)', True)
        self.menu_addNewMenu(GlobalStrings.menu_display_setting, 'btn_widgets', 'url(:/16x16/icons/16x16/cil-equalizer.png)', False)


    def menu_selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                self.mainwindow_previous_tab_name = w.objectName()
                w.setStyleSheet(self.menu_selectMenu(w.styleSheet()))


    def menu_addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u'Segoe UI')
        button = QPushButton()
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(UIStyle.style_menu_button.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.menu_Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

        return button

    
    def menu_Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == 'btn_dashboard' :
            if self.mainwindow_previous_tab_name != 'btn_dashboard':
                # self.dashboard_reload_available_devices_from_settings()
                # self.start_dashboard_timers()
                pass

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
            self.menu_resetStyle('btn_dashboard')
            self.labelPage('Home')
            btnWidget.setStyleSheet(self.menu_selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == 'btn_data':
            if self.mainwindow_previous_tab_name != 'btn_data':
                # self.database_statistics_reload_device_setting_entities()
                # self.stop_dashboard_timers()
                pass

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_data)
            self.menu_resetStyle('btn_data')
            self.labelPage('Data')
            btnWidget.setStyleSheet(self.menu_selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == 'btn_devices_settings':
            if self.mainwindow_previous_tab_name != 'btn_devices_settings':
                # self.stop_dashboard_timers()
                pass

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_devices_settings)
            self.menu_resetStyle('btn_devices_settings')
            self.labelPage('Settings')
            btnWidget.setStyleSheet(self.menu_selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == 'btn_widgets':
            if self.mainwindow_previous_tab_name != 'btn_widgets':
                # self.widgets_reload_widgets()
                # self.stop_dashboard_timers()
                pass

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            self.menu_resetStyle('btn_widgets')
            self.labelPage('Settings')
            btnWidget.setStyleSheet(self.menu_selectMenu(btnWidget.styleSheet()))

        self.mainwindow_previous_tab_name = btnWidget.objectName()

    
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)   



    def menu_resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.menu_deselectMenu(w.styleSheet()))


    def menu_deselectMenu(self, getStyle):
        deselect = getStyle.replace(UIStyle.menu_selected_menu_button_style, '')
        return deselect


    def menu_selectMenu(self, getStyle):
        select = getStyle + (UIStyle.menu_selected_menu_button_style)
        return select

            


    def widgets_reload_widgets(self):
        pass


    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)


    def closeEvent(self, event):
        print('closing application...')
        # self.modbus_querrying_timer.stop()
        
        return super(MainWindow, self).closeEvent(event)


    def eventFilter(self, obj, event:QEvent):
        # print('event Type', event.type())

        if event.type() == QEvent.MouseButtonPress:
            self.dragPos = event.globalPos()

            return True

        if event.type() == QtCore.QEvent.KeyPress:
            print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

            if(event.key() == 81):
                self.close()

            return True

        if event.type() == QtCore.QEvent.Resize:
            # print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

            if self.WINDOW_TILTE_BAR:
                WindowProperties.resize_grips(self)

            # return True
        
        return QtWidgets.QWidget.eventFilter(self, obj, event)
