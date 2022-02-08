import collections
import os
import re
import sys
from enum import Enum

from app import helpers

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (ClassInfo, QCoreApplication, QDate, QDateTime,
                            QEvent, QMetaObject, QObject, QPoint,
                            QPropertyAnimation, QRect, QRegExp, QSize, Qt,
                            QTime, QUrl)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QRegExpValidator)
from PySide2.QtWidgets import *
from sqlalchemy.sql.expression import column
from ui.custom_widgets.py_grips.py_grips import PyGrips


class WindowProperties():

    SETTINGS_DIALOG_WIDTH = 600

    SETTINGS_DIALOG_HEIGHT = 800

    def center_window(current_window, parent_obj=None):
        if parent_obj is not None:
            current_window.move(parent_obj.geometry().center() - current_window.rect().center())
        else:
            mousepointer_position = QApplication.desktop().cursor().pos()
            # screen_number = QApplication.desktop().screenNumber(mousepointer_position)
            # print('Screen number: ' + str(screen_number))

            screen = QApplication.screenAt(mousepointer_position)

            position = (screen.geometry().center() - current_window.rect().center())
        
            current_window.move(position.x(), position.y())


    def style_window(window):
        WindowProperties.__setup_stylesheets(window)
        WindowProperties.__set_main_program_icon(window)


    def __setup_stylesheets(window):
        stylesheet_from_file = StylesLoader.get_qss_from_file()

        window.setStyleSheet(stylesheet_from_file)

        window_ui = None

        if hasattr(window, 'ui'):
            window_ui = window.ui
        else:
            window_ui = window            

        WindowProperties.setup_frame_main_content_style(window_ui, stylesheet_from_file)


    def initialize_frame_grips(window_UI, hide_grips):
        setattr(window_UI, 'left_grip', PyGrips(window_UI, "left", hide_grips))
        setattr(window_UI, 'right_grip', PyGrips(window_UI, "right", hide_grips))
        setattr(window_UI, 'top_grip', PyGrips(window_UI, "top", hide_grips))
        setattr(window_UI, 'bottom_grip', PyGrips(window_UI, "bottom", hide_grips))

        setattr(window_UI, 'top_left_grip', PyGrips(window_UI, "top_left", hide_grips))
        setattr(window_UI, 'top_right_grip', PyGrips(window_UI, "top_right", hide_grips))
        setattr(window_UI, 'bottom_left_grip', PyGrips(window_UI, "bottom_left", hide_grips))
        setattr(window_UI, 'bottom_right_grip', PyGrips(window_UI, "bottom_right", hide_grips))


    def set_grips_visibility(window_UI, is_visible):
        window_UI.left_grip.setVisible(is_visible)
        window_UI.right_grip.setVisible(is_visible)
        window_UI.top_grip.setVisible(is_visible)
        window_UI.bottom_grip.setVisible(is_visible)

        window_UI.top_left_grip.setVisible(is_visible)
        window_UI.top_right_grip.setVisible(is_visible)
        window_UI.bottom_left_grip.setVisible(is_visible)
        window_UI.bottom_right_grip.setVisible(is_visible)


    def resize_grips(window_UI):
        window_UI.left_grip.setGeometry(5, 10, 10, window_UI.height())
        window_UI.right_grip.setGeometry(window_UI.width() - 15, 10, 10, window_UI.height())
        window_UI.top_grip.setGeometry(5, 5, window_UI.width() - 10, 10)
        window_UI.bottom_grip.setGeometry(5, window_UI.height() - 15, window_UI.width() - 10, 10)

        window_UI.top_left_grip.setGeometry(5, 5, 15, 15)
        window_UI.top_right_grip.setGeometry(window_UI.width() - 20, 5, 15, 15)
        window_UI.bottom_left_grip.setGeometry(5, window_UI.height() - 20, 15, 15)
        window_UI.bottom_right_grip.setGeometry(window_UI.width() - 20, window_UI.height() - 20, 15, 15)


    def __set_main_program_icon(window):
        icon = QIcon()
        icon.addFile(u":/logos/icons/images/program_icon.png", QSize(64, 64), QIcon.Normal, QIcon.Off)
        window.setWindowIcon(icon)


    def setup_frame_main_content_style(window_ui, stylesheet_from_file):
        if hasattr(window_ui, 'frame_main_content'):
            window_ui.frame_main_content.setStyleSheet(stylesheet_from_file)


class DialogWindowHelper():
    Interface_type_tuple = collections.namedtuple('additional_type_tuple', ['name_gathering', 'data_function', 'role'])

    def fill_combobox_with_allowed_values(
            combobox: QComboBox,
            properties_list,
            add_no_value=False,
            sort_type=None,
            is_settings_element=False,
            additional_data_tuple=None,
            comparable_list=None
        ):

        combobox.clear()

        if properties_list is not None:
            for properties_element in properties_list:

                if is_settings_element is True:
                    properties_element = properties_element.id
                
                string_property_name = None

                if isinstance(properties_element, Enum):
                    string_property_name = properties_element.name
                else:
                    if additional_data_tuple is not None:
                        string_property_name = additional_data_tuple.name_gathering(properties_element)
                    else:
                        string_property_name = str(properties_element)

                temp_text = ''

                if comparable_list is not None:
                    temp_text += ' '
                    if properties_element in comparable_list:
                        temp_text = '[Available]'
                        print('Should be OK', properties_element)

                combobox.addItem(string_property_name + temp_text, properties_element)

                if additional_data_tuple is not None:
                    additional_data = additional_data_tuple.data_function(properties_element)
                    combobox.setItemData(combobox.findData(properties_element, QtCore.Qt.UserRole), additional_data, additional_data_tuple.role)

        if sort_type is not None:
            combobox.model().sort(0, sort_type)

        if add_no_value is True:
            combobox.insertItem(0, GlobalStrings.no_value_item_text, None)
            combobox.setCurrentIndex(combobox.findData(None, QtCore.Qt.UserRole))
        else:
            combobox.setCurrentIndex(0)


class StylesLoader():
    def get_qss_from_file():
        theme_file_path = helpers.Helpers.resource_path(u'ui/themes/main_theme.qss')

        with open(theme_file_path, "r") as f:
            style = f.read()

        return style


class NamesValidator():
    def get_name_validator():
        return QtGui.QRegExpValidator(QRegExp("^(?!\s*$).+"))


class IpAddressValidator():
    def get_address_validator():
        IpRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"

        regex_expression = QRegExp("^" + IpRange
                                + "(\\." + IpRange + ")"
                                + "(\\." + IpRange + ")"
                                + "(\\." + IpRange + ")$")

        regex_validator = QRegExpValidator(regex_expression)

        return regex_validator


class NotEmptyIntValidator(QtGui.QValidator):
    def validate(self, text, pos):
        if not bool(text):
            text = '0'
        state = QtGui.QIntValidator.Acceptable if text.isdigit() else QtGui.QIntValidator.Invalid
        return state, text, pos


class WarningItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QtWidgets.QStyleOptionViewItem.Left
        super(WarningItemDelegate, self).paint(painter, option, index)



class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        names_format = QtGui.QTextCharFormat()
        names_format.setForeground(QtCore.Qt.white)
        names_format.setFontWeight(QtGui.QFont.Bold)

        namesPatterns = [GlobalStrings.settings_info_name, GlobalStrings.settings_info_address, GlobalStrings.setting_info_interface]

        self.highlightingRules = []

        [self.highlightingRules.append((QtCore.QRegExp('\\b' + pattern + ''), names_format))
                for pattern in namesPatterns]

        properties_format = QtGui.QTextCharFormat()
        properties_format.setFontWeight(QtGui.QFont.Bold)

        propertiesPatterns = [*SettingsManager.SerialInterface.allowed_keys, *SettingsManager.TcpInterface.allowed_keys, *SettingsManager.DeviceDriverSettings.allowed_keys]

        [self.highlightingRules.append((QtCore.QRegExp('\\b' + pattern + ''), properties_format))
                for pattern in propertiesPatterns]


        warning_format = QtGui.QTextCharFormat()
        warning_format.setForeground(QtCore.Qt.yellow)
        warning_format.setFontWeight(QtGui.QFont.Bold)

        warning_patterns = [GlobalStrings.setting_info_no_interface]

        [self.highlightingRules.append((QtCore.QRegExp('' + pattern + ''), warning_format))
                for pattern in warning_patterns]

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)


class FormatHelper():
    def round_text_number_to_decimal_places(text, decimal_places):
        if decimal_places is not None:
            format_string = "{:." + str(decimal_places) + "f}"
            return format_string.format(round(float(text), decimal_places))
        else:
            return None

    def create_unit_symbol_string(unit_symbol):
        return ' [' + unit_symbol + ']'


class FilterDateProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(FilterDateProxyModel, self).__init__(parent)
        self._from_date, self._to_date = QtCore.QDate(), QtCore.QDate()

    def setRange(self, from_date, to_date):
        self._from_date = from_date
        self._to_date = to_date
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if any([not date.isValid() for date in (self._from_date, self._to_date,)]):
            return True
        ix = self.sourceModel().index(sourceRow, self.filterKeyColumn(), sourceParent)
        dt = ix.data().date()
        return self._from_date <= dt <= self._to_date



class GlobalStrings():

    no_value_item_text = '...'

    dialog_validation_name = 'Podana nazwa już istnieje'


    program_tile = 'Zen IPA Client'

    menu_dashboard_title = 'Liczniki'

    menu_data_title = 'Dane'

    menu_settings_title = 'Ustawienia połączenia'

    menu_display_setting = 'Ustawienia wyświetlania'


    dashboard_recording_button = 'Rejestruj zmiany'


    database_statistics_reload_statistics_data_button = 'Wczytaj dane / odśwież'
    database_statistics_date_from = 'Data od: '
    database_statistics_date_to = 'Data do: '
    database_statistics_zoom_reset = 'Zoom reset'


    settings_add_new_interface_bar_top = 'Dodawanie nowego interfejsu'
    settings_add_new_interface_label = 'Wpisz nową nazwę interfejsu'


    settings_remove_interface_bar_top = 'Usuwanie interfejsu'
    settings_remove_interface_bar_label = 'Na pewno chcesz usunąć inerfejs?'
    settings_remove_interface_bar_label_number_of_devices = 'Liczba urządzeń korzystających z intefejsu: '


    setting_edit_interface_bar_top = 'Edycja ustawień interfejsu'
    setting_edit_interface_bar_label = 'Zmień nazwę interfejsu'



    settings_add_new_device_bar_top = 'Dodawanie nowego urządzenia'
    settings_add_new_device_label = 'Wpisz nową nazwę urządzenia'


    settings_remove_device_bar_top = 'Usuwanie urządzenia'
    settings_remove_device_bar_label = 'Na pewno chcesz usunąć urządzenie?'


    setting_edit_device_bar_top = 'Edycja ustawień urządzenia'
    setting_edit_device_bar_label = 'Zmień nazwę urządzenia'


    settings_info_name = 'Nazwa: '
    settings_info_address = 'Adres: '

    settings_info_no_data = 'Brak danych.'


    setting_info_no_interface = 'Uwaga! Brak interfejsu.'

    setting_info_interface = 'Interfejs: '
