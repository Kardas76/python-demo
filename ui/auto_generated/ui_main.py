# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1371, 887)
        MainWindow.setMinimumSize(QSize(1200, 720))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.GroupedDragging)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_main_content = QFrame(self.frame_center)
        self.frame_main_content.setObjectName(u"frame_main_content")
        self.frame_main_content.setStyleSheet(u"")
        self.frame_main_content.setFrameShape(QFrame.NoFrame)
        self.frame_main_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_main_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_main_content)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setMidLineWidth(7)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.verticalLayout_20 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.title_bar = QFrame(self.page_dashboard)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(14)
        self.frame_title.setFont(font4)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, 0, 0, 0)
        self.btn_open_charts = QPushButton(self.frame_title)
        self.btn_open_charts.setObjectName(u"btn_open_charts")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_open_charts.sizePolicy().hasHeightForWidth())
        self.btn_open_charts.setSizePolicy(sizePolicy4)
        self.btn_open_charts.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.btn_open_charts.setFont(font5)
        self.btn_open_charts.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_charts.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_charts.setStyleSheet(u"background-image: url(:/16x16/icons/16x16/cil-chart.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_open_charts.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.btn_open_charts)

        self.comboBox_dashboard_device = QComboBox(self.frame_title)
        self.comboBox_dashboard_device.setObjectName(u"comboBox_dashboard_device")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_dashboard_device.sizePolicy().hasHeightForWidth())
        self.comboBox_dashboard_device.setSizePolicy(sizePolicy5)
        self.comboBox_dashboard_device.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(16)
        self.comboBox_dashboard_device.setFont(font6)
        self.comboBox_dashboard_device.setStyleSheet(u"")
        self.comboBox_dashboard_device.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_12.addWidget(self.comboBox_dashboard_device)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_new_device_name = QLabel(self.frame_title)
        self.label_new_device_name.setObjectName(u"label_new_device_name")
        font7 = QFont()
        font7.setPointSize(8)
        self.label_new_device_name.setFont(font7)

        self.horizontalLayout_13.addWidget(self.label_new_device_name)

        self.lineEdit_history_settings_recording_name = QLineEdit(self.frame_title)
        self.lineEdit_history_settings_recording_name.setObjectName(u"lineEdit_history_settings_recording_name")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_history_settings_recording_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_history_settings_recording_name.setSizePolicy(sizePolicy6)
        self.lineEdit_history_settings_recording_name.setFont(font)

        self.horizontalLayout_13.addWidget(self.lineEdit_history_settings_recording_name)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_enable_recording = QRadioButton(self.frame_title)
        self.btn_enable_recording.setObjectName(u"btn_enable_recording")
        sizePolicy4.setHeightForWidth(self.btn_enable_recording.sizePolicy().hasHeightForWidth())
        self.btn_enable_recording.setSizePolicy(sizePolicy4)
        self.btn_enable_recording.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.btn_enable_recording.setFont(font8)
        self.btn_enable_recording.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enable_recording.setLayoutDirection(Qt.LeftToRight)
        self.btn_enable_recording.setStyleSheet(u"")
        self.btn_enable_recording.setAutoRepeat(False)

        self.verticalLayout_9.addWidget(self.btn_enable_recording)


        self.horizontalLayout_12.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_14.addWidget(self.frame_title)


        self.verticalLayout_20.addWidget(self.title_bar)

        self.dashboard_no_details = QFrame(self.page_dashboard)
        self.dashboard_no_details.setObjectName(u"dashboard_no_details")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dashboard_no_details.sizePolicy().hasHeightForWidth())
        self.dashboard_no_details.setSizePolicy(sizePolicy7)
        self.dashboard_no_details.setStyleSheet(u"")
        self.dashboard_no_details.setFrameShape(QFrame.StyledPanel)
        self.dashboard_no_details.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.dashboard_no_details)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.labelBox_interface_settings_no_details = QLabel(self.dashboard_no_details)
        self.labelBox_interface_settings_no_details.setObjectName(u"labelBox_interface_settings_no_details")
        font9 = QFont()
        font9.setPointSize(16)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.labelBox_interface_settings_no_details.setFont(font9)
        self.labelBox_interface_settings_no_details.setStyleSheet(u"")
        self.labelBox_interface_settings_no_details.setWordWrap(True)

        self.gridLayout_34.addWidget(self.labelBox_interface_settings_no_details, 1, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.dashboard_no_details)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.gridLayout_2 = QGridLayout(self.page_data)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.labelBox_history_label = QLabel(self.page_data)
        self.labelBox_history_label.setObjectName(u"labelBox_history_label")
        sizePolicy3.setHeightForWidth(self.labelBox_history_label.sizePolicy().hasHeightForWidth())
        self.labelBox_history_label.setSizePolicy(sizePolicy3)
        font10 = QFont()
        font10.setPointSize(18)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.labelBox_history_label.setFont(font10)
        self.labelBox_history_label.setStyleSheet(u"")
        self.labelBox_history_label.setWordWrap(True)

        self.gridLayout_11.addWidget(self.labelBox_history_label, 2, 0, 1, 1)

        self.frame_Interfaces_list_2 = QFrame(self.page_data)
        self.frame_Interfaces_list_2.setObjectName(u"frame_Interfaces_list_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_Interfaces_list_2.sizePolicy().hasHeightForWidth())
        self.frame_Interfaces_list_2.setSizePolicy(sizePolicy8)
        self.frame_Interfaces_list_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Interfaces_list_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_Interfaces_list_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.database_statistics_treeview = QWidget(self.frame_Interfaces_list_2)
        self.database_statistics_treeview.setObjectName(u"database_statistics_treeview")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.database_statistics_treeview.sizePolicy().hasHeightForWidth())
        self.database_statistics_treeview.setSizePolicy(sizePolicy9)

        self.gridLayout_6.addWidget(self.database_statistics_treeview, 3, 0, 1, 1)

        self.pushButton_generate_CSV = QPushButton(self.frame_Interfaces_list_2)
        self.pushButton_generate_CSV.setObjectName(u"pushButton_generate_CSV")
        sizePolicy4.setHeightForWidth(self.pushButton_generate_CSV.sizePolicy().hasHeightForWidth())
        self.pushButton_generate_CSV.setSizePolicy(sizePolicy4)
        self.pushButton_generate_CSV.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.pushButton_generate_CSV, 4, 0, 1, 1)

        self.listWidget_device_setting_entity = QListWidget(self.frame_Interfaces_list_2)
        self.listWidget_device_setting_entity.setObjectName(u"listWidget_device_setting_entity")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.listWidget_device_setting_entity.sizePolicy().hasHeightForWidth())
        self.listWidget_device_setting_entity.setSizePolicy(sizePolicy10)
        font11 = QFont()
        font11.setPointSize(12)
        self.listWidget_device_setting_entity.setFont(font11)
        self.listWidget_device_setting_entity.setFrameShape(QFrame.NoFrame)
        self.listWidget_device_setting_entity.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_device_setting_entity.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_device_setting_entity.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget_device_setting_entity.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_device_setting_entity.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_device_setting_entity.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_6.addWidget(self.listWidget_device_setting_entity, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_Interfaces_list_2, 4, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_11)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_visualisation_date_from = QLabel(self.page_data)
        self.label_visualisation_date_from.setObjectName(u"label_visualisation_date_from")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_visualisation_date_from.sizePolicy().hasHeightForWidth())
        self.label_visualisation_date_from.setSizePolicy(sizePolicy11)
        self.label_visualisation_date_from.setFont(font11)

        self.horizontalLayout_21.addWidget(self.label_visualisation_date_from)

        self.dateTimeEdit_visualisation_from = QDateTimeEdit(self.page_data)
        self.dateTimeEdit_visualisation_from.setObjectName(u"dateTimeEdit_visualisation_from")
        self.dateTimeEdit_visualisation_from.setFont(font11)
        self.dateTimeEdit_visualisation_from.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.dateTimeEdit_visualisation_from.setCalendarPopup(True)

        self.horizontalLayout_21.addWidget(self.dateTimeEdit_visualisation_from)

        self.label_visualisation_date_to = QLabel(self.page_data)
        self.label_visualisation_date_to.setObjectName(u"label_visualisation_date_to")
        sizePolicy11.setHeightForWidth(self.label_visualisation_date_to.sizePolicy().hasHeightForWidth())
        self.label_visualisation_date_to.setSizePolicy(sizePolicy11)
        self.label_visualisation_date_to.setFont(font11)

        self.horizontalLayout_21.addWidget(self.label_visualisation_date_to)

        self.dateTimeEdit_visualisation_to = QDateTimeEdit(self.page_data)
        self.dateTimeEdit_visualisation_to.setObjectName(u"dateTimeEdit_visualisation_to")
        sizePolicy5.setHeightForWidth(self.dateTimeEdit_visualisation_to.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_visualisation_to.setSizePolicy(sizePolicy5)
        self.dateTimeEdit_visualisation_to.setFont(font11)
        self.dateTimeEdit_visualisation_to.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.dateTimeEdit_visualisation_to.setCalendarPopup(True)

        self.horizontalLayout_21.addWidget(self.dateTimeEdit_visualisation_to)

        self.btn_database_statistics_reload_statistics_data = QPushButton(self.page_data)
        self.btn_database_statistics_reload_statistics_data.setObjectName(u"btn_database_statistics_reload_statistics_data")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.btn_database_statistics_reload_statistics_data.sizePolicy().hasHeightForWidth())
        self.btn_database_statistics_reload_statistics_data.setSizePolicy(sizePolicy12)
        self.btn_database_statistics_reload_statistics_data.setMinimumSize(QSize(0, 50))
        self.btn_database_statistics_reload_statistics_data.setFont(font5)
        self.btn_database_statistics_reload_statistics_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_database_statistics_reload_statistics_data.setLayoutDirection(Qt.LeftToRight)
        self.btn_database_statistics_reload_statistics_data.setStyleSheet(u"")
        self.btn_database_statistics_reload_statistics_data.setAutoRepeat(False)

        self.horizontalLayout_21.addWidget(self.btn_database_statistics_reload_statistics_data)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget_qt_chart_database_statistics = QWidget(self.page_data)
        self.widget_qt_chart_database_statistics.setObjectName(u"widget_qt_chart_database_statistics")
        sizePolicy.setHeightForWidth(self.widget_qt_chart_database_statistics.sizePolicy().hasHeightForWidth())
        self.widget_qt_chart_database_statistics.setSizePolicy(sizePolicy)
        self.widget_qt_chart_database_statistics.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.widget_qt_chart_database_statistics)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.table_view_statistics_table = QTableView(self.page_data)
        self.table_view_statistics_table.setObjectName(u"table_view_statistics_table")
        sizePolicy7.setHeightForWidth(self.table_view_statistics_table.sizePolicy().hasHeightForWidth())
        self.table_view_statistics_table.setSizePolicy(sizePolicy7)
        self.table_view_statistics_table.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.table_view_statistics_table)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_data)
        self.page_devices_settings = QWidget()
        self.page_devices_settings.setObjectName(u"page_devices_settings")
        self.gridLayout_12 = QGridLayout(self.page_devices_settings)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_2 = QFrame(self.page_devices_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_Interfaces_list = QFrame(self.frame_2)
        self.frame_Interfaces_list.setObjectName(u"frame_Interfaces_list")
        self.frame_Interfaces_list.setFrameShape(QFrame.StyledPanel)
        self.frame_Interfaces_list.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_Interfaces_list)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_add_new_interface = QPushButton(self.frame_Interfaces_list)
        self.btn_add_new_interface.setObjectName(u"btn_add_new_interface")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.btn_add_new_interface.sizePolicy().hasHeightForWidth())
        self.btn_add_new_interface.setSizePolicy(sizePolicy13)
        self.btn_add_new_interface.setMinimumSize(QSize(0, 50))
        self.btn_add_new_interface.setFont(font5)
        self.btn_add_new_interface.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_new_interface.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_new_interface.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-plus.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_add_new_interface.setAutoRepeat(False)

        self.gridLayout.addWidget(self.btn_add_new_interface, 0, 0, 1, 1)

        self.btn_remove_interface = QPushButton(self.frame_Interfaces_list)
        self.btn_remove_interface.setObjectName(u"btn_remove_interface")
        sizePolicy13.setHeightForWidth(self.btn_remove_interface.sizePolicy().hasHeightForWidth())
        self.btn_remove_interface.setSizePolicy(sizePolicy13)
        self.btn_remove_interface.setMinimumSize(QSize(0, 50))
        self.btn_remove_interface.setFont(font5)
        self.btn_remove_interface.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_interface.setLayoutDirection(Qt.LeftToRight)
        self.btn_remove_interface.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-minus.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_remove_interface.setAutoRepeat(False)

        self.gridLayout.addWidget(self.btn_remove_interface, 0, 1, 1, 1)

        self.btn_edit_interface = QPushButton(self.frame_Interfaces_list)
        self.btn_edit_interface.setObjectName(u"btn_edit_interface")
        sizePolicy13.setHeightForWidth(self.btn_edit_interface.sizePolicy().hasHeightForWidth())
        self.btn_edit_interface.setSizePolicy(sizePolicy13)
        self.btn_edit_interface.setMinimumSize(QSize(0, 50))
        self.btn_edit_interface.setFont(font5)
        self.btn_edit_interface.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_interface.setLayoutDirection(Qt.LeftToRight)
        self.btn_edit_interface.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-pencil.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_edit_interface.setAutoRepeat(False)

        self.gridLayout.addWidget(self.btn_edit_interface, 0, 2, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout)


        self.gridLayout_3.addLayout(self.formLayout, 3, 0, 1, 1)

        self.listWidget_interfaces_list = QListWidget(self.frame_Interfaces_list)
        self.listWidget_interfaces_list.setObjectName(u"listWidget_interfaces_list")
        sizePolicy.setHeightForWidth(self.listWidget_interfaces_list.sizePolicy().hasHeightForWidth())
        self.listWidget_interfaces_list.setSizePolicy(sizePolicy)
        self.listWidget_interfaces_list.setFont(font11)
        self.listWidget_interfaces_list.setFrameShape(QFrame.NoFrame)
        self.listWidget_interfaces_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_interfaces_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_interfaces_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget_interfaces_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_interfaces_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_interfaces_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.listWidget_interfaces_list, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_Interfaces_list, 3, 0, 1, 1)

        self.labelBox_interface_settings_details = QLabel(self.frame_2)
        self.labelBox_interface_settings_details.setObjectName(u"labelBox_interface_settings_details")
        sizePolicy1.setHeightForWidth(self.labelBox_interface_settings_details.sizePolicy().hasHeightForWidth())
        self.labelBox_interface_settings_details.setSizePolicy(sizePolicy1)
        self.labelBox_interface_settings_details.setFont(font9)
        self.labelBox_interface_settings_details.setStyleSheet(u"")
        self.labelBox_interface_settings_details.setWordWrap(True)

        self.gridLayout_10.addWidget(self.labelBox_interface_settings_details, 1, 1, 1, 1)

        self.labelBox_interfaces_title = QLabel(self.frame_2)
        self.labelBox_interfaces_title.setObjectName(u"labelBox_interfaces_title")
        self.labelBox_interfaces_title.setFont(font10)
        self.labelBox_interfaces_title.setStyleSheet(u"")
        self.labelBox_interfaces_title.setWordWrap(True)

        self.gridLayout_10.addWidget(self.labelBox_interfaces_title, 1, 0, 1, 1)

        self.textEdit_interface_info = QTextEdit(self.frame_2)
        self.textEdit_interface_info.setObjectName(u"textEdit_interface_info")
        self.textEdit_interface_info.setEnabled(True)
        self.textEdit_interface_info.setFont(font11)
        self.textEdit_interface_info.setStyleSheet(u"border: 0")
        self.textEdit_interface_info.setCursorWidth(0)
        self.textEdit_interface_info.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_10.addWidget(self.textEdit_interface_info, 3, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_10)


        self.gridLayout_12.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.page_devices_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_devices_list = QFrame(self.frame)
        self.frame_devices_list.setObjectName(u"frame_devices_list")
        self.frame_devices_list.setMinimumSize(QSize(0, 0))
        self.frame_devices_list.setFrameShape(QFrame.StyledPanel)
        self.frame_devices_list.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_devices_list)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget_devices_list = QListWidget(self.frame_devices_list)
        self.listWidget_devices_list.setObjectName(u"listWidget_devices_list")
        sizePolicy.setHeightForWidth(self.listWidget_devices_list.sizePolicy().hasHeightForWidth())
        self.listWidget_devices_list.setSizePolicy(sizePolicy)
        self.listWidget_devices_list.setFont(font11)
        self.listWidget_devices_list.setFrameShape(QFrame.NoFrame)
        self.listWidget_devices_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_devices_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_devices_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget_devices_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_devices_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_devices_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.listWidget_devices_list, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btn_remove_device = QPushButton(self.frame_devices_list)
        self.btn_remove_device.setObjectName(u"btn_remove_device")
        sizePolicy13.setHeightForWidth(self.btn_remove_device.sizePolicy().hasHeightForWidth())
        self.btn_remove_device.setSizePolicy(sizePolicy13)
        self.btn_remove_device.setMinimumSize(QSize(0, 50))
        self.btn_remove_device.setFont(font5)
        self.btn_remove_device.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_device.setLayoutDirection(Qt.LeftToRight)
        self.btn_remove_device.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-minus.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_remove_device.setAutoRepeat(False)

        self.gridLayout_13.addWidget(self.btn_remove_device, 0, 1, 1, 1)

        self.btn_add_new_device = QPushButton(self.frame_devices_list)
        self.btn_add_new_device.setObjectName(u"btn_add_new_device")
        sizePolicy13.setHeightForWidth(self.btn_add_new_device.sizePolicy().hasHeightForWidth())
        self.btn_add_new_device.setSizePolicy(sizePolicy13)
        self.btn_add_new_device.setMinimumSize(QSize(0, 50))
        self.btn_add_new_device.setFont(font5)
        self.btn_add_new_device.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_new_device.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_new_device.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-plus.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_add_new_device.setAutoRepeat(False)

        self.gridLayout_13.addWidget(self.btn_add_new_device, 0, 0, 1, 1)

        self.btn_edit_device = QPushButton(self.frame_devices_list)
        self.btn_edit_device.setObjectName(u"btn_edit_device")
        sizePolicy13.setHeightForWidth(self.btn_edit_device.sizePolicy().hasHeightForWidth())
        self.btn_edit_device.setSizePolicy(sizePolicy13)
        self.btn_edit_device.setMinimumSize(QSize(0, 50))
        self.btn_edit_device.setFont(font5)
        self.btn_edit_device.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_device.setLayoutDirection(Qt.LeftToRight)
        self.btn_edit_device.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/cil-pencil.png);\n"
"background-position: center;\n"
"background-repeat: None;")
        self.btn_edit_device.setAutoRepeat(False)

        self.gridLayout_13.addWidget(self.btn_edit_device, 0, 2, 1, 1)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.gridLayout_13)


        self.gridLayout_4.addLayout(self.formLayout_2, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_devices_list, 1, 0, 1, 1)

        self.labelBox_device_settings_details = QLabel(self.frame)
        self.labelBox_device_settings_details.setObjectName(u"labelBox_device_settings_details")
        sizePolicy1.setHeightForWidth(self.labelBox_device_settings_details.sizePolicy().hasHeightForWidth())
        self.labelBox_device_settings_details.setSizePolicy(sizePolicy1)
        self.labelBox_device_settings_details.setBaseSize(QSize(150, 0))
        self.labelBox_device_settings_details.setFont(font9)
        self.labelBox_device_settings_details.setStyleSheet(u"")
        self.labelBox_device_settings_details.setWordWrap(True)

        self.gridLayout_9.addWidget(self.labelBox_device_settings_details, 0, 1, 1, 1)

        self.labelBox_devices_title = QLabel(self.frame)
        self.labelBox_devices_title.setObjectName(u"labelBox_devices_title")
        self.labelBox_devices_title.setFont(font10)
        self.labelBox_devices_title.setStyleSheet(u"")
        self.labelBox_devices_title.setWordWrap(True)

        self.gridLayout_9.addWidget(self.labelBox_devices_title, 0, 0, 1, 1)

        self.textEdit_device_info = QTextEdit(self.frame)
        self.textEdit_device_info.setObjectName(u"textEdit_device_info")
        self.textEdit_device_info.setEnabled(True)
        self.textEdit_device_info.setFont(font11)
        self.textEdit_device_info.setStyleSheet(u"border: 0")
        self.textEdit_device_info.setCursorWidth(0)
        self.textEdit_device_info.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_9.addWidget(self.textEdit_device_info, 1, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_9)


        self.gridLayout_12.addWidget(self.frame, 3, 0, 1, 1)

        self.line_5 = QFrame(self.page_devices_settings)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMidLineWidth(5)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_12.addWidget(self.line_5, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_devices_settings)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_widgets_settings = QFrame(self.page_widgets)
        self.frame_widgets_settings.setObjectName(u"frame_widgets_settings")
        self.frame_widgets_settings.setEnabled(True)
        self.frame_widgets_settings.setMinimumSize(QSize(0, 150))
        self.frame_widgets_settings.setStyleSheet(u"")
        self.frame_widgets_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_widgets_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_widgets_settings)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.circular_progress_layout = QGridLayout()
        self.circular_progress_layout.setObjectName(u"circular_progress_layout")

        self.verticalLayout_10.addLayout(self.circular_progress_layout)


        self.verticalLayout_6.addWidget(self.frame_widgets_settings)

        self.stackedWidget.addWidget(self.page_widgets)

        self.horizontalLayout_17.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_main_content)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_main_content)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.btn_open_charts)
        QWidget.setTabOrder(self.btn_open_charts, self.comboBox_dashboard_device)
        QWidget.setTabOrder(self.comboBox_dashboard_device, self.lineEdit_history_settings_recording_name)
        QWidget.setTabOrder(self.lineEdit_history_settings_recording_name, self.btn_enable_recording)
        QWidget.setTabOrder(self.btn_enable_recording, self.listWidget_device_setting_entity)
        QWidget.setTabOrder(self.listWidget_device_setting_entity, self.dateTimeEdit_visualisation_from)
        QWidget.setTabOrder(self.dateTimeEdit_visualisation_from, self.dateTimeEdit_visualisation_to)
        QWidget.setTabOrder(self.dateTimeEdit_visualisation_to, self.btn_database_statistics_reload_statistics_data)
        QWidget.setTabOrder(self.btn_database_statistics_reload_statistics_data, self.pushButton_generate_CSV)
        QWidget.setTabOrder(self.pushButton_generate_CSV, self.table_view_statistics_table)
        QWidget.setTabOrder(self.table_view_statistics_table, self.btn_add_new_interface)
        QWidget.setTabOrder(self.btn_add_new_interface, self.btn_remove_interface)
        QWidget.setTabOrder(self.btn_remove_interface, self.btn_edit_interface)
        QWidget.setTabOrder(self.btn_edit_interface, self.listWidget_interfaces_list)
        QWidget.setTabOrder(self.listWidget_interfaces_list, self.textEdit_interface_info)
        QWidget.setTabOrder(self.textEdit_interface_info, self.listWidget_devices_list)
        QWidget.setTabOrder(self.listWidget_devices_list, self.btn_add_new_device)
        QWidget.setTabOrder(self.btn_add_new_device, self.btn_remove_device)
        QWidget.setTabOrder(self.btn_remove_device, self.btn_edit_device)
        QWidget.setTabOrder(self.btn_edit_device, self.textEdit_device_info)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"some_text", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_open_charts.setText("")
        self.label_new_device_name.setText(QCoreApplication.translate("MainWindow", u"Nazwa", None))
        self.btn_enable_recording.setText(QCoreApplication.translate("MainWindow", u"Rejestruj zmiany", None))
        self.labelBox_interface_settings_no_details.setText(QCoreApplication.translate("MainWindow", u"Brak szczeg\u00f3\u0142\u00f3w do wy\u015bwietlenia", None))
        self.labelBox_history_label.setText(QCoreApplication.translate("MainWindow", u"Historia", None))
        self.pushButton_generate_CSV.setText(QCoreApplication.translate("MainWindow", u"Generuj CSV", None))
        self.label_visualisation_date_from.setText(QCoreApplication.translate("MainWindow", u"Data od:", None))
        self.dateTimeEdit_visualisation_from.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy HH:mm:ss", None))
        self.label_visualisation_date_to.setText(QCoreApplication.translate("MainWindow", u"Data do:", None))
        self.dateTimeEdit_visualisation_to.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy HH:mm:ss", None))
        self.btn_database_statistics_reload_statistics_data.setText(QCoreApplication.translate("MainWindow", u"Od\u015bwie\u017c", None))
        self.btn_add_new_interface.setText("")
        self.btn_remove_interface.setText("")
        self.btn_edit_interface.setText("")
        self.labelBox_interface_settings_details.setText(QCoreApplication.translate("MainWindow", u"Szczeg\u00f3\u0142y", None))
        self.labelBox_interfaces_title.setText(QCoreApplication.translate("MainWindow", u"Interfejsy", None))
        self.btn_remove_device.setText("")
        self.btn_add_new_device.setText("")
        self.btn_edit_device.setText("")
        self.labelBox_device_settings_details.setText(QCoreApplication.translate("MainWindow", u"Szczeg\u00f3\u0142y", None))
        self.labelBox_devices_title.setText(QCoreApplication.translate("MainWindow", u"Urz\u0105dzenia", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

